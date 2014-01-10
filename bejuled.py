 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import random, copy, time

class Board(object):
    """ The main board """
    TIME_GAP = 1

    def __init__(self):
        self.grid = [[Item() for i in range(9)] for j in range(9)]

    def __str__(self):
        rep =   "  │1│2│3│4│5│6│7│8│9│\n"
        rep +=  "──┼─┴─┴─┴─┴─┴─┴─┴─┴─┤\n"
        i = 1
        for row in self.grid:
            rep += str(i) + "¯│"
            j = 0
            for item in row:
                rep += str(item)
                if j != len(row)-1:
                    rep += " "
                j += 1
            rep += "│\n"
            i += 1
        rep +=  "¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ "
        return rep

    def update(self):
        print(self)
        time.sleep(self.TIME_GAP)
        while self.del_3():
            print(self)
            time.sleep(self.TIME_GAP)
            self.fall()
            print(self)
            time.sleep(self.TIME_GAP)

    def del_3(self):
        global score
        self.grid_copy = copy.deepcopy(self.grid)

        change = False

        i = 0
        for row in self.grid:
            j = 0
            for item in row:
                if 0 < j < 8:
                    if str(item) == str(row[j-1]) and \
                       str(item) == str(row[j+1]):
                        self.grid_copy[i][j-1] = " "
                        self.grid_copy[i][j] = " "
                        self.grid_copy[i][j+1] = " "
                        score += 3
                        change = True
                j += 1
            i +=1

        i = 0
        for row in self.grid:
            j = 0
            for column in row:
                if 0 < j < 8:
                    i_before = self.grid[j+1][i]
                    item = self.grid[j][i]
                    i_after = self.grid[j-1][i]
                    if str(item) == str(i_before) and \
                       str(item) == str(i_after):
                        self.grid_copy[j-1][i] = " "
                        self.grid_copy[j][i] = " "
                        self.grid_copy[j+1][i] = " "
                        score += 3
                        change = True
                j += 1
            i += 1

        self.grid = self.grid_copy
        return change

    def fall(self):
        flattened = []
        for row in self.grid:
            for item in row:
                flattened.append(item)

        while " " in flattened:
            i = 0
            for row in self.grid:
                j = 0
                for item in row:
                    if item == " ":
                        if i != 0:
                            self.grid[i][j] = self.grid[i-1][j]
                            self.grid[i-1][j] = " "
                        else:
                            self.grid[i][j] = Item()
                    j += 1
                i += 1

            flattened = []
            for row in self.grid:
                for item in row:
                    flattened.append(item)

    def call_swap(self, first_x, first_y, second_x, second_y):
        swap(self.grid, first_x, first_y, second_x, second_y)

class Item(object):
    """ Each piece on the grid """
    PIECES = ("♣", "♦", "♥", "♠", "☺", "☻", "•", "○")

    def __init__(self):
        self.piece = random.choice(self.PIECES)

    def __str__(self):
        return self.piece

def user_response(msg):
    response = ""
    while response == "":
        response = input(msg)
    return response

def user_int_response(msg):
    error  = True
    while error:
        try:
            response = int(user_response(msg))
            error = False
        except TypeError:
            error = True
    return response

def swap(grid, first_x, first_y, second_x, second_y):
    first_item = grid[first_y][first_x]
    second_item = grid[second_y][second_x]
    grid[first_y][first_x] = second_item
    grid[second_y][second_x] = first_item
    return grid

def input_coords():
    first_x = user_int_response("input the first x coord: ")
    first_y = user_int_response("input the first y coord: ")
    second_x = user_int_response("input the second x coord: ")
    second_y = user_int_response("input the second y coord: ")
    if ((first_x + 1 == second_x or first_x - 1 == second_x) \
       and first_y == second_y) or \
       ((first_y + 1 == second_y or first_y - 1 == second_y) \
       and first_x == second_x):
        return first_x-1, first_y-1, second_x-1, second_y-1

def print_score():
    print("Score: ", score)

global score
score = 0
main_board = Board()
win = False
while win == False:
    main_board.update()
    print_score()
    first_x, first_y, second_x, second_y = input_coords()
    main_board.call_swap(first_x, first_y, second_x, second_y)
