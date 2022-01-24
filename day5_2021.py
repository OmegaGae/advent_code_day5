# -*- coding: utf-8 -*-

# File Name : day5_2021.py

# Purpose :

# Creation Date : 11-01-2022

# Last Modified : Thu Jan 13 18:25:58 2022

# Created by : OmegaGae

from lib.packages.editfiles import editfile as edit
import numpy as np


def format_data_input(lines: list):

    start_position = []
    end_position = []
    filter_for_start = []
    filter_for_end = []
    x = 0
    y = 1
    for line in lines:

        filter_for_end.append(line.rstrip().split("->")[1].split(","))
        filter_for_start.append(line.rstrip().split("->")[0].split(","))
        s_position = [
            float(filter_for_start[i][e])
            for i in range(len(filter_for_start))
            for e in range(2)
        ]
        e_position = [
            float(filter_for_end[i][e])
            for i in range(len(filter_for_end))
            for e in range(2)
        ]

        while (x and y) < len(s_position):
            start_position.append((s_position[x], s_position[y]))
            end_position.append((e_position[x], e_position[y]))

            x += 2
            y += 2

    return start_position, end_position


class Plan:
    def __init__(self, max_x: int, max_y: int) -> None:

        self._nber_of_row = max_y
        self._nber_of_cols = max_x
        self.map = self._matrice()

    def _matrice(self):
        return np.zeros((self._nber_of_row, self._nber_of_cols))

    def find_interval_points(self, x1: float, y1: float, x2: float, y2: float):

        x = x1
        y = y1

        if x1 > x2 and y1 > y2:

            while (x and y) != (x2 and y2):

                if x == x2 and y != y2:
                    self.map[y, x] += 1.0
                    y -= 1
                elif y == y2 and x != x2:
                    self.map[y, x] += 1.0
                    x -= 1
                elif (x and y) != (x2 and y2):
                    x -= 1
                    y -= 1

        elif x1 < x2 and y1 < y2:

            while (x and y) != (x2 and y2):

                if x == x2 and y != y2:
                    self.map[y, x] += 1.0
                    y += 1
                elif y == y2 and x != x2:
                    self.map[y, x] += 1.0
                    x += 1
                elif (x and y) != (x2 and y2):
                    x += 1
                    y += 1

        elif x1 < x2 and y1 > y2:

            while (x and y) != (x2 and y2):

                if x == x2 and y != y2:
                    self.map[y, x] += 1.0
                    y -= 1
                elif y == y2 and x != x2:
                    self.map[y, x] += 1.0
                    x += 1
                elif (x and y) != (x2 and y2):
                    x += 1
                    y -= 1

        elif x1 > x2 and y1 < y2:

            while (x and y) != (x2 and y2):

                if x == x2 and y != y2:
                    self.map[y, x] += 1.0
                    y += 1
                elif y == y2 and x != x2:
                    self.map[y, x] += 1.0
                    x -= 1
                elif (x and y) != (x2 and y2):
                    x -= 1
                    y += 1

        else:

            while (x or y) != (x2 or y2):

                if x == x2 and y < y2:
                    self.map[y, x] += 1.0
                    y += 1
                elif x == x2 and y > y2:
                    self.map[y, x] += 1.0
                    y -= 1
                elif y == y2 and x < x2:
                    self.map[y, x] += 1.0
                    x += 1
                elif y == y2 and x > x2:
                    self.map[y, x] += 1.0
                    x -= 1
                else:
                    break

        return

    def draw_line(self, starting_point: tuple, end_point: tuple):

        self.map[starting_point[1], starting_point[0]] += 1
        self.map[end_point[1], end_point[0]] += 1

        self.find_interval_points(
            starting_point[0], starting_point[1], end_point[0], end_point[1]
        )

    def overlap_lines(self):
        """
        Do a loop in map to count the number of point which have a value strictly higher than 1
        """
        count = 0
        return sum([count + 1 for plan_y in self.map for x in plan_y if x > 1])


def higher_points():
    """
    Find the higher point from input it will be use by Plan in init
    """


def main(start_point: list, end_point: list):
    """
    code to be exe
    """
    # Call higher_point output will be use for Plan
    # Create a empty field which have the same size as input
    field_hydrothermal = Plan()
    # Draw the lines on the field --> loop
    # count the overlapping lines and return count


if __name__ == "__main__":

    input_dum = edit.Editfile("dummy_day5.txt").read()
    print(input_dum)
    start_point, end_point = format_data_input(input_dum)
    main(start_point, end_point)
