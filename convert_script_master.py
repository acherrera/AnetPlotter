
from math import sqrt
import sys



# file_name = sys.argv[1]
file_name = './CJX_2.gcode'
distance_threshold = 5 # Distance in mm to raise if greater

input_data = []
with open(file_name) as f:
    input_data = f.readlines()

# Create the new list
new_list = []


raise_commands = [
    'G91\n',
    'G0 Z2\n',
    'G90\n'
]

lower_commands = [
    'G91\n',
    'G0 Z-2\n',
    'G90\n'
]
better_start_code = [
    'G0 Z2\n'
]


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



found_first = False
previous_move = False # was previous command a move?


for index, value in enumerate(input_data):

    
    if 'G0' in value:         
        if not found_first:
            # Need to treat first movement special
            split_command = value.split(' ')
            move_part = str(' '.join(split_command[:-1]))
            Z_move = 'G0 ' + split_command[-1]
            move_part += '\n'

            better_start_code.append(move_part)
            better_start_code.append(Z_move)
            for i in better_start_code:
                new_list.append(i)
            found_first = True
            previous_move = False # Assume print start after this - no move


        elif (not previous_move):
            # check distance of move - ignore small moves
            previous_command = input_data[index-1]
            distance = get_distance(value, previous_command)
            
            # Distance less than threshold - don't raise
            if distance < distance_threshold:
                new_list.append(value)
        
            # Other raise betwee moves
            else:
                for command in raise_commands:
                    new_list.append(command)
                previous_move = True
                new_list.append(value)
            
        else:
            new_list.append(value)
        
                    
    else:
       
        if previous_move:
            for command in lower_commands:
                new_list.append(command)
            previous_move = False
            new_list.append(value)
        else:
            new_list.append(value)

output_file = '.'.join(file_name.split('.')[:-1]) + "_converted.gcode"
with open(output_file, 'w') as f:
    for line in new_list:
        f.write(line)
