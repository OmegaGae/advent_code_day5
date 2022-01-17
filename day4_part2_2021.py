# -*- coding: utf-8 -*-

# File Name : 2021_day4_part2.py

# Purpose :

# Creation Date : 11-01-2022

# Last Modified : Tue Jan 11 12:38:12 2022

# Created by : OmegaGae

from lib.packages.editfiles import editfile as edit
import numpy as np


class BingoLooser:
    def __init__(self, input_file: list) -> None:
        """
        Bingo Game: The goal is to find a row or cols of matrice numbers
        """

        first_data = input_file.pop(0).rstrip().split(",")

        self.random_nbrs = list(
            map(float, [first_data[p] for p in range(len(first_data))])
        )

        self.all_boards = np.array_split(
            np.loadtxt(input_file), len(np.loadtxt(input_file)) / 5
        )

        self.repertory = {}
        self.val_repertory = []
        self.all_winners = {}
        self.all_winners_ind = []
        self.rank = 0

    def add_value_inliste(self, liste_container: list, liste_to_add: list, counter=0):
        while counter < len(liste_to_add):
            liste_container.append(liste_to_add[counter])
            counter += 1
        return liste_container

    def marked_nbrs(self, rand_nber: float):

        for ind_board, board in enumerate(self.all_boards):
            temporary_repertory = [
                rand_nber for elements in board if rand_nber in elements
            ]
            self.repertory[ind_board] = self.add_value_inliste(
                self.repertory.get(ind_board, []), temporary_repertory
            )

    def yield_rand_nber(self):

        for nbr in self.random_nbrs:
            yield nbr

    def is_board_full(self):

        for ind_board, _ in enumerate(self.all_boards):

            if len(self.repertory.get(ind_board, 0)) >= len(self.all_boards[0][0]) and ind_board not in self.all_winners_ind:

                yield ind_board, self.repertory[ind_board]

    def is_winner_row(self, ind_board: int, value_rep: list):

        for row in self.all_boards[ind_board]:
            is_winner = [(True, value) for value in value_rep if value in row]

            if sum([is_winner[p].count(True) for p in range(len(is_winner))]) == len(
                row
            ):
                return True, is_winner[-1][1]
        return False, 0

    def is_winner_cols(self, ind_board: int, value_rep: list):

        self.transpose_board = [
            b
            for b in np.nditer(
                self.all_boards[ind_board], flags=["external_loop"], order="F"
            )
        ]

        for cols in self.transpose_board:
            is_winner = [(True, value) for value in value_rep if value in cols]

            if sum([is_winner[p].count(True) for p in range(len(is_winner))]) == len(
                cols
            ):
                return True, is_winner[-1][1]
        return False, 0

    def sum_winner_board(self, ind_board: int, value_rep: list):

        return sum(
            [
                b[indice]
                for b in self.all_boards[ind_board]
                for indice in range(len(self.all_boards[ind_board][0]))
                if b[indice] not in value_rep
            ]
        )

    def settings(self):

        iterator_rand_nber = iter(self.yield_rand_nber())
        iterator_board = iter(self.is_board_full())
        n = 0
        while n < 5:
            self.marked_nbrs(next(iterator_rand_nber))
            n += 1

        return iterator_rand_nber, iterator_board

    def rand_value_for_sum(self, rand_values: list, last_number_drawn: int):

        sum_rand_value = []
        for value in rand_values:
            if value != last_number_drawn:
                sum_rand_value.append(value)
            else:
                sum_rand_value.append(value)
                break 
        
        return sum_rand_value

    def winner_board(self):

        iterator_rand_nber, iterator_board = self.settings()
        
        while True:

            try:         
                ind_board, rep = next(iterator_board)
                
                state_row, is_winner_row = self.is_winner_row(ind_board, rep)
                state_cols, is_winner_cols = self.is_winner_cols(ind_board, rep)

                if state_row:
                    
                    rep_rand_nbers = self.rand_value_for_sum(
                        self.random_nbrs, is_winner_row
                    )
                   
                    self.all_winners_ind.append(ind_board)
                    self.all_winners[ind_board] = ((self.sum_winner_board(ind_board, rep_rand_nbers)) * is_winner_row,self.rank)
                    self.rank+=1
                    
                    continue

                elif state_cols:
             
                    rep_rand_nbers = self.rand_value_for_sum(
                        self.random_nbrs, is_winner_cols
                    )
                    
                    self.all_winners_ind.append(ind_board)
                    self.all_winners[ind_board] = ((self.sum_winner_board(ind_board, rep_rand_nbers) * is_winner_cols), self.rank)
                    self.rank+=1
            
                    continue

                else:
                    continue

            except StopIteration:
                iterator_board = iter(self.is_board_full()) 
                try:
                    self.marked_nbrs(next(iterator_rand_nber))
                    continue
                except StopIteration:             
                    return self.all_winners


if __name__ == "__main__":
    input_day4 = edit.Editfile("input_day4.txt").read()
    bingo_looser = BingoLooser(input_day4)
    print(bingo_looser.winner_board())








