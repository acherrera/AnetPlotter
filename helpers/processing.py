
from math import sqrt

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


def process_start(input_data, new_list,  tracker, commands):
    """
        Handle the updat of the first command
    """
    tracker.found_first = True
    tracker.head_raised = False
    value = input_data[tracker.index]

    split_command = value.split(' ')
    move_part = str(' '.join(split_command[:-1]))
    Z_move = 'G0 ' + split_command[-1]
    move_part += '\n'
    better_start_code = commands['better_start_code']

    better_start_code.append(move_part)
    better_start_code.append(Z_move)
    for i in better_start_code:
        tracker.new_code.append(i)


def find_case(input_data, tracker_obj):
    """
        Find the type of case for the given input
        Args:
            input_data: (list) ist of input commands
            tracker_obj: (tracker object) keeps track of data related to the
            process
    """

        # Head not raise - move head up
        # Next three moves
        # Case 1: Short travel, long feed
        ## Move 1-2: G0 move < 1mm
        ## Move 2-3: G1 move > 1mm 
        ## Do not raise

        # Case 2: Long travel, multiple short feed
        ## Move 1-2 G0 move > 1mm
        ## Move 2-3 G1 move < 1mm
        ## Move 3-4 G1 move *any
        ## Raise

        # Case 3: Long/short, short feed, long/short travel
        ## Move 1-2 G0 move *any
        ## Move 2-3 G1 move < 1mm
        ## Move 3-4 G0 move *any
        ## Very tricky case. Raise on first G0, continue to look
        ## For this pattern until there is a G1 move > 1mm. Lower at 
        ## This point.

