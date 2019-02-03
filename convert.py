
import sys
import os
# May not be needed
from helpers.processing import (process_start, strip_coords,
        get_distance, data_tracker, process_normal, lower_head,
        standard_processing)



def convert_main(input_data):

    DISTANCE_THRESHOLD = 0.2 # Distance in mm to raise if greater
    data_length = len(input_data)
    tracker = data_tracker(input_data)
    move_dist = None

    while (tracker.index) < data_length:
        # Index value is the value currently being examined
        current_move = tracker.current_move()

        # Find distance of move
        if  (('G0' in current_move or 'G1' in current_move) and
            ('G0' in tracker.postion or 'G1'in tracker.postion)
            and tracker.found_first):
            move_dist = get_distance(tracker.postion, current_move)
            if move_dist < DISTANCE_THRESHOLD:
                tracker.new_code.append(current_move)
            else:
                standard_processing(tracker)

        else:
            standard_processing(tracker)

        tracker.update_move()
        tracker.index += 1

    return tracker.new_code


if __name__ == "__main__":

    # file_name = sys.argv[1]
    file_name = './CJX_2_sample.gcode'

    input_data = []
    with open(file_name) as f:
        input_data = f.readlines()

    # Create the new list

    new_list = convert_main(input_data)

    converted_dir = './samples'
    if not os.path.exists(converted_dir):
        os.mkdir(converted_dir)

    output_file = converted_dir.join(file_name.split('.')[:-1]) + "_converted.gcode"
    with open(output_file, 'w') as f:
        for line in new_list:
            f.write(line)
