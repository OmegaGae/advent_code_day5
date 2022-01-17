
"""--------------------------------------------------------------------------

 * File Name : 2021_day2.py

 * Purpose : 

 * Creation Date : 29-12-2021

 * Last Modified : Wed Dec 29 19:26:04 2021

 * Created by : OmegaGae

-----------------------------------------------------------------------------"""

from lib.packages.editfiles import editfile as edit


def position(sonar_sweep: list):
    position_x = 0
    position_y = 0

    for mvt in sonar_sweep:

        mvt_direction = mvt.rstrip().split()[0]
        mvt_distance = mvt.rstrip().split()[1]

        if mvt_direction == 'forward':
            position_x += int(mvt_distance)
        
        elif mvt_direction == 'down':
            position_y += int(mvt_distance)
        else:
            position_y -= int(mvt_distance)

    return position_x * position_y


def real_position(sonar_sweep: list):
    position_x = 0
    depth =0
    aim = 0

    for mvt in sonar_sweep:

        mvt_direction = mvt.rstrip().split()[0]
        mvt_distance = mvt.rstrip().split()[1]
        
        if mvt_direction == 'forward':
            position_x += int(mvt_distance)
            depth = depth + aim * int(mvt_distance)
    
        elif mvt_direction == 'down':
            aim += int(mvt_distance)
        else:
            aim -= int(mvt_distance)
    
    return position_x * depth


if __name__ == '__main__':
    input_sw = edit.Editfile('input_day2.txt')
    print(real_position(input_sw.read()))
 





















