from copy import deepcopy

#MP3 Project: KenKen solver using DFS algorithm
#Ella Mohanram
#March 1, 2023

#solves kenken puzzle using DFS algorithm
class KenKen:
    #constructor function that intializes class attributes
    def __init__(self):
        self.cages = []
        self.side_length = 0
        self.priority_queue = []

    #checks if numbers in all cages satisfy expression given
    #param play_board: current board of numbers being checked
    #return: boolean value of whether numbers available in the board satisfy the cages
    def check_all_cages(self, play_board):
        valid_solution = True

        for cage in self.cages:
            number = cage[0]
            operator = cage[1]
            cage_boxes = cage[2]

            max_cage_box = max(cage_boxes)
            if max_cage_box <= len(play_board):
                valid_solution_state = self.check_cages(play_board, number, operator, cage_boxes)
                if valid_solution_state == False:
                    valid_solution = False
                    return valid_solution
            else:
                valid_solution = False
                return valid_solution

        return valid_solution

    # checks if numbers in board do not repeat in rows or columns
    # param play_board: current board of numbers being checked
    # return: boolean value of whether numbers available in the board repeat in rows or columns
    def check_repeat(self, play_board):
        is_repeat = False
        rows = []

        for i in range(0, len(play_board), self.side_length):
            row = play_board[i: i + self.side_length]
            rows.append(row)
            if len(row) != len(set(row)):
                is_repeat = True

        for i in range(0, len(rows)):
            column = []
            for row in rows:
                column.append(row[i])
            if len(column) != len(set(column)):
                is_repeat = True

        return is_repeat

    # checks if numbers in one cage satisfy expression given
    # param play_board: current board of numbers being checked
    # param number: number expression must satisfy with numbers in cages
    # param operator: type of mathematical operator numbers are combined
    # param cage_boxes: values of numbers in play_board
    # return: boolean value of whether numbers in one cage available satisfy expression given
    def check_cages(self, play_board, number, operator, cage_boxes):
        valid_solution = False
        if operator == '-' or operator == '/':
            first_cage_value = play_board[cage_boxes[0] - 1]
            second_cage_value = play_board[cage_boxes[1] - 1]

        if operator == '+':
            sum = 0
            for box_number in cage_boxes:
                sum += play_board[box_number - 1]
            if sum == number:
                valid_solution = True
        elif operator == '*':
            product = 1
            for box_number in cage_boxes:
                product = product * play_board[box_number - 1]
            if product == number:
                valid_solution = True
        elif operator == '-':
            if (first_cage_value - second_cage_value == number) or (second_cage_value - first_cage_value == number):
                valid_solution = True
        elif operator == '/':
            if (first_cage_value/second_cage_value == number) or (second_cage_value/first_cage_value == number):
                valid_solution = True

        return valid_solution

    #finds array of numbers that solves the kenken puzzle
    #return: array of solved kenken puzzle, else empty array
    def game(self):
        stack = []
        upper_limit = self.side_length ** 2

        neighbors = [i for i in range(1, self.side_length + 1)]
        for neighbor in neighbors:
            stack.append([neighbor])

        while len(stack) > 0:
            current_path = stack[-1]
            stack.pop(-1)
            print(current_path)

            if len(current_path) == upper_limit:
                if (self.check_repeat(current_path) == False) and (self.check_all_cages(current_path) == True):
                    return current_path
            else:
                for neighbor in neighbors:
                    current_path_copy = deepcopy(current_path)
                    current_path_copy.append(neighbor)
                    if len(current_path_copy) <= upper_limit:
                        stack.append(current_path_copy)

        return []

    #takes user input and returns solved kenken puzzle
    #returns: solution to kenken puzzle in board form
    def run(self):
        self.side_length = int(input('Enter how many boxes per side: '))

        game_board = ""
        for i in range(1, self.side_length ** 2 + 1):
            game_board += str(i) + ' '
            if i % self.side_length == 0:
                game_board += '\n'

        number_of_cages = int(input('Enter number of cages in KenKen board: '))
        while len(self.cages) != number_of_cages:
            print(game_board)
            input_boxes = input('Enter boxes in cage separated by space: ')
            cage_boxes = input_boxes.split()
            for i in range(len(cage_boxes)):
                cage_boxes[i] = int(cage_boxes[i])

            number, operator = input(
                'Enter expression of cage, with the number and operator separated by a space: ').split()
            new_box = [int(number), operator, cage_boxes]

            self.cages.append(new_box)

        solution = self.game()
        print("Solution: ")
        for i in range(0, len(solution), self.side_length):
            row = solution[i: i + self.side_length]
            row = ' '.join(str(num) for num in row)
            print(row)

kenken = KenKen()
kenken.run()