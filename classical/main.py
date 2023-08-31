from random import randint
from time import sleep

make_matrix =  lambda: [["#" for _ in range(3)] for _ in range(3)]


def show_game():
    for row in matrix:
        print(" | ".join(row))
        print("-" * 9)


def player_choice():
    while True:
        row = int(input("Select some row: ")) -1
        column = int(input("Select some column: ")) -1

        if matrix[row][column] != "#":
            print("Please select a valid option.")
        else:
            matrix[row][column] = "x"
            break


def machine_choice():
    while True:
        row = randint(0, 2)
        column = randint(0, 2)
        if matrix[row][column] == "#":
            matrix[row][column] = "o"
            break


def check_draw():
    global matrix
    counter = 0
    for row in matrix:
        for element in row:
            if element == "#":
                counter += 1
                break
    if counter == 0:
        print("It's a draw! Restarting the game...")
        sleep(3)
        matrix = make_matrix()


def check_finish_game():
    global matrix
    check_draw()
    
    def check_horizontal():
        global matrix
        for row in matrix:
            if row.count("x") == 3:
                return "User wins"
            elif row.count("o") == 3:
                return "Machine wins"
        return "Not yet"
    
    def check_vertical():
        global matrix
        for column in range(3):
            if matrix[0][column] == matrix[1][column] == matrix[2][column]:
                if matrix[0][column] == "x":
                    return "User wins"
                elif matrix[0][column] == "o":
                    return "Machine wins"
        return "Not yet"
    
    def check_diagonal():
        global matrix
        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            if matrix[0][0] == "x":
                return "User wins"
            elif matrix[0][0] == "o":
                return "Machine wins"
        elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
            if matrix[0][2] == "x":
                return "User wins"
            elif matrix[0][2] == "o":
                return "Machine wins"
        return "Not yet"
    
    if check_horizontal() == "User wins" or check_vertical() == "User wins" or check_diagonal() == "User wins":
        print("You win! Restarting the game...")
        sleep(3)
        matrix = make_matrix()

    elif check_horizontal() == "Machine wins" or check_vertical() == "Machine wins" or check_diagonal() == "Machine wins":
        print("The machine wins! Restarting the game...")
        sleep(3)
        matrix = make_matrix()



# Main game
matrix = make_matrix()
while True:
    show_game()
    player_choice()
    check_finish_game()
    machine_choice()
    check_finish_game()
    