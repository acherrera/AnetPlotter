from math import sqrt


class data_tracker():

    def __init__(self, input_data):
        self.found_first = False
        self.head_raised = False
        self.index = 0
        self.move_1 = None
        self.move_2 = None
        self.move_3 = None
        self.new_code = []
        self.old_code = input_data
        self.RAISE_COMMANDS = [
                    'G91\n',
                    'G0 Z2\n',
                    'G90\n'
                ]
        self.LOWER_COMMANDS = [
                    'G91\n',
                    'G0 Z-2\n',
                    'G90\n'
                ]
        self.BETTER_START_CODE = [
                    'G0 Z2\n'
                ]



    def current_move(self):
        return self.old_code[self.index]

    def update_move(self, raw_data):
        """
            shift moves back one
            Args:
                new_move(str): New move to add
        """
        self.move_3 = self.move_2
        self.move_2 = self.move_1
        self.move_1 = raw_data[self.index]


def strip_coords(command):
    """
        Should return the x and y position of the command. Note that this assumes
        only need Z and Y

        Args:
            command: (str): gcode command to parse out data
    """
    command_list = command.split(' ')
    x_value = 0.0
    y_value = 0.0
    for portion in command_list:
        if 'X' in portion:
            x_value = float(portion.replace('X', ''))
        elif 'Y' in portion:
            y_value = float(portion.replace('Y', ''))

    return (x_value, y_value)


def get_distance(command1, command2):
    """
        Should return the distance between two gcode commands

        Args:
            command1: (str): gcode command to parse out data
            command2: (str): gcode command to parse out data

    """
    coords1 = strip_coords(command1)
    coords2 = strip_coords(command2)
    x_sqrd = (coords1[0] - coords2[0])**2
    y_sqrd = (coords1[1] - coords2[1])**2
    distance = sqrt(x_sqrd + y_sqrd)
    return distance


def process_start(tracker):
    """
        Handle the updat of the first command
    """
    tracker.found_first = True
    tracker.head_raised = False
    value = tracker.current_move()

    split_command = value.split(' ')
    move_part = str(' '.join(split_command[:-1]))
    Z_move = 'G0 ' + split_command[-1]
    move_part += '\n'
    better_start_code = tracker.BETTER_START_CODE

    # Build out the new commands to add
    better_start_code.append(move_part)
    better_start_code.append(Z_move)

    # Add the new commands
    for i in better_start_code:
        tracker.new_code.append(i)


def process_normal(tracker):
    tracker.head_raised = True
    for i in tracker.RAISE_COMMANDS:
        tracker.new_code.append(i)
    tracker.new_code.append(tracker.current_move())


def lower_head(tracker):
    tracker.head_raised = False
    for i in tracker.LOWER_COMMANDS:
        tracker.new_code.append(i)
    tracker.new_code.append(tracker.current_move())
