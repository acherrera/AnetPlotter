
import sys
# May not be needed
from helpers.processing import (process_start, strip_coords,
        get_distance)

class data_tracker():

    def __init__(self):
        self.found_first = False
        self.head_raised = False
        self.index = 0
        self.move_1 = None
        self.move_2 = None
        self.move_3 = None
        self.new_code = []

    def update_move(self, raw_data):
        """
            shift moves back one
            Args:
                new_move(str): New move to add
        """
        self.move_3 = self.move_2
        self.move_2 = self.move_1
        self.move_1 = raw_data[self.index]


COMMANDS = {
    "raise_commands": [
        'G91\n',
        'G0 Z2\n',
        'G90\n'
    ],
    "lower_commands": [
        'G91\n',
        'G0 Z-2\n',
        'G90\n'
    ],
    "better_start_code": [
        'G0 Z2\n'
    ]
}




def main(input_data):

    data_length = len(input_data)
    tracker = data_tracker()

    while (tracker.index) < data_length:
        # Index value is the value currently being examined
        current_move = input_data[tracker.index]

        if 'G0' in current_move:
            if not tracker.found_first:
                process_start(input_data, new_list, tracker,
                        COMMANDS)
            else:
                case_type = find_case(input_data, tracker)

            if case_type == 1:
                process_case_1(input_data, tracker)

            elif case_type == 2:
                process_case_2(input_data, tracker)

            elif case_type ==3 :
                process_case_3(input_data, tracker)

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
    new_list = []

    main(input_data)

    output_file = '.'.join(file_name.split('.')[:-1]) + "_converted.gcode"
    with open(output_file, 'w') as f:
        for line in new_list:
            f.write(line)

