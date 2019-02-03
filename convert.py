
import sys
import os
# May not be needed
from helpers.processing import (process_start, strip_coords,
        get_distance, data_tracker, process_normal, lower_head)



def convert_main(input_data):

    data_length = len(input_data)
    tracker = data_tracker(input_data)

    while (tracker.index) < data_length:
        # Index value is the value currently being examined
        current_move = tracker.current_move()

        if 'G0' in current_move:
            if not tracker.found_first:
                process_start(tracker)
            elif tracker.head_raised:
                # Multiple G0 Moves
                tracker.new_code.append(tracker.current_move())
            else:
                process_normal(tracker)

        elif tracker.head_raised:
            lower_head(tracker)

        else:
            tracker.new_code.append(tracker.current_move())

        tracker.update_move(input_data)
        tracker.index += 1

    return tracker.new_code


if __name__ == "__main__":

    # file_name = sys.argv[1]
    file_name = './CJX_2_sample.gcode'
    distance_threshold = 5 # Distance in mm to raise if greater

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
