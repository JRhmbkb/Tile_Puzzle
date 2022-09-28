
import copy
import math
from queue import PriorityQueue
import random


############################################################
#Tile Puzzle
############################################################

#Write a top-level function create_tile_puzzle(rows, cols) that returns
#a new TilePuzzle of the specified dimensions, initialized to the starting
#configuration. Tiles 1 through r · c − 1 should be arranged starting from
#the top-left corner in row-major order, and tile 0 should be located in the
#lower-right corner.


def create_tile_puzzle(rows, cols):
    #create the default size of the board with all 0s array of list
    board =  [ [0]*cols for i in range(rows)]

    #assign each position the corresponding number
    num = 1
    
    for row in range(rows):
        for col in range(cols):
            board[row][col] = num
            num = num + 1 

    #assign the last position (right bottom cornor) as 0
    board[rows-1][cols-1] = 0

    #return the finished board as an object
    return TilePuzzle(board)
    
class TilePuzzle(object):
    
    # Required


    #write an initialization method that stores an input board of this form described
    #above for future use. You additionally may wish to store the dimensions
    #of the board as separate internal variables, as well as the location of the
    #empty tile.
    def __init__(self, board):
        
        #store the input board
        self.board = board
        #store the row
        self.row = len(board)
        #store the column
        self.col = len(board[0])
        #store the location of the empty tile
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    self.empty = (i,j)

    #In the TilePuzzle class, write a method get_board(self) that returns
    #the internal representation of the board stored during initialization.
    def get_board(self):
        
        return self.board

    #In the TilePuzzle class, write a method perform_move(self,
    #direction) that attempts to swap the empty tile with its neighbor in
    #the indicated direction, where valid inputs are limited to the strings "up",
    #"down", "left", and "right". If the given direction is invalid, or if the
    #move cannot be performed, then no changes to the puzzle should be made.
    #The method should return a Boolean value indicating whether the move
    #was successful.
    def perform_move(self, direction):
        
        #first we need to get where the 0 is
        for row in range(self.row):
            for col in range(self.col):
                if self.board[row][col] == 0:
                    row_index = row
                    col_index = col

        # if it's moving up, then we will move the one BELOW the empty one UP
        if direction == 'up':
            #make sure it's not out of boundary
            if row_index - 1 >= 0:
                #swap
                self.board[row_index][col_index] = self.board[row_index-1][col_index]
                self.board[row_index-1][col_index] = 0
                return True
            else:
                return False

        #if it's moving down, then will move the empty to the down
        elif direction == 'down':
            #make sure it's not out of boundary
            if row_index + 1 < self.row:
                #swap
                self.board[row_index][col_index] = self.board[row_index+1][col_index]
                self.board[row_index+1][col_index] = 0
                return True
            else:
                return False
        #if it's moving left, then will move the empty to the left
        elif direction == 'left':
            #make sure it's not out of boundary
            if col_index - 1 >= 0:
                #swap
                self.board[row_index][col_index] = self.board[row_index][col_index - 1]
                self.board[row_index][col_index - 1] = 0
                return True
            else:
                return False

        
        #if it's moving right, then will move the empty to the right
        elif direction == 'right':
            #make sure it's not out of boundary
            if col_index + 1 < self.col:
                #swap
                self.board[row_index][col_index] = self.board[row_index][col_index + 1]
                self.board[row_index][col_index + 1] = 0
                return True
            else:
                return False
        #any other invalide input of direction would result in False return
        else:
            return False


    #write a method scramble(self, num_moves)
    #which scrambles the puzzle by calling perform_move(self, direction)
    #the indicated number of times, each time with a random direction. This
    #method of scrambling guarantees that the resulting configuration will
    #be solvable, which may not be true if the tiles are randomly permuted.
    #Hint: The random module contains a function random.choice(seq) which
    #returns a random element from its input sequence

    def scramble(self, num_moves):
        
        direction_to_pick = ['up','down','left','right']

        #use for loop to run this random picking function num_moves times
        for i in range(num_moves):
            direction_to_go = random.choice(direction_to_pick)

            #if direction is up, then perform move on self with string up
            if direction_to_go == 'up':
                self.perform_move('up')
            #if direction is down, then perform move on self with string down
            elif direction_to_go == 'down':
                self.perform_move('down')
             #if direction is left, then perform move on self with string left
            elif direction_to_go == 'left':
                self.perform_move('left')
             #if direction is right, then perform move on self with string right
            elif direction_to_go == 'right':
                self.perform_move('right')


    #In the TilePuzzle class, write a method is_solved(self) that returns
    #whether the board is in its starting configuration.

    def is_solved(self):
        
        #original stage, bascially just create a new one (since the new one IS the original stage)
        solution = create_tile_puzzle(self.row, self.col)

        #if it's all sorted, then return true, otherwise return false
        if self.board == solution.get_board():
            return True
        else:
            return False

    #In the TilePuzzle class, write a method copy(self) that returns a new
    #TilePuzzle object initialized with a deep copy of the current board.
    #Changes made to the original puzzle should not be reflected in the copy,
    #and vice versa.

    def copy(self):
        #do deepcopy to get another complete different new copy of the self. 
        board_copy = copy.deepcopy(self)
        return board_copy


    #In the TilePuzzle class, write a method successors(self) that yields
    #all successors of the puzzle as (direction, new-puzzle) tuples. The second
    #element of each successor should be a new TilePuzzle object whose board
    #is the result of applying the corresponding move to the current board. The
    #successors may be generated in whichever order is most convenient, as long
    #as successors corresponding to unsuccessful moves are not included in the
    #output.

    def successors(self):
        
        #all the dirctions to pick from 
        direction_to_pick = ['up','down','left','right']
        #create the data structure needed and pair up with its corresponding direction: up, down, left, and right.
        for direction_to_go in direction_to_pick:
            successor = copy.deepcopy(self)
            if successor.perform_move(direction_to_go):
                yield (direction_to_go, successor) #return the data structure 


    # Required
    def find_solutions_iddfs(self):
        
        #base condition, if it's solved then yield empoty and return 
        if self.is_solved():
            yield []
            return

        #if the input is not the solution, then start with deepth of 1
        depth = 1
        #define a variable named solved, when true, meaning we found the solution; when false, meaning we have not found the solution yet
        solved = False

        # now we want to explore/search all the possible solutions
        while self.is_solved() is False:
            for to_explore in self.iddfs_helper(depth, []):
                yield to_explore
                solved = True

            if solved:
                break
            depth = depth + 1


    #yields all solutions to the current board of length no more than limit
    #which are continuations of the provided move list. Your main method will
    #then call this helper function in a loop, increasing the depth limit by one at
    #each iteration, until one or more solutions have been found. Note that this
    #helper function should find all solutions within the step limit based on the
    #moves already taken.

    def iddfs_helper(self, limit, moves):
        
        #if this reaches more than limit needed, then stop
        if limit <= 0:
            return

        #otherwise go down 1 level deeper
        limit = limit - 1
        for direction_to_go, board_layout in self.successors():

            current_direction_to_go = direction_to_go
            current_board_layout = board_layout
            # if the board layout is the solution, then we retrun all the moves and the current direction_to_go
            if board_layout.is_solved():
                yield moves +[current_direction_to_go]
            # if the current_board_layout is NOT the solution, then we should recurrsively go to all the next deeper level
            else:
                for next_board_layout in current_board_layout.iddfs_helper(limit, moves + [current_direction_to_go]):
                    yield next_board_layout

    # Required
    def find_solution_a_star(self):


        #import the priorityQueue since we are dealing with A* search
        frontier = PriorityQueue()
        frontier.put((self.cal_heuristic(), 0, [], self))
        
        #set should be used to avoid repeatation
        visited = set()
        visited.add(tuple(tuple(i) for i in self.board))

        while not frontier.empty():
            cur_fn, cur_gn, cur_directions_to_go, cur_board_layout = frontier.get()
            for next_direction_to_go, next_board_layout in cur_board_layout.successors():

                #get the possible solution 
                possible_solution = cur_directions_to_go + [next_direction_to_go]
                #if it's solved, then return the possible solution
                if next_board_layout.is_solved():
                    return possible_solution
                #if not, then add it to visit and frontier
                else:
                    new_board_layout = tuple(tuple(i) for i in next_board_layout.get_board())
                    if new_board_layout not in visited:
                        #add the next board layout to the visited list 
                        visited.add(new_board_layout)
                        #put the new elements to the frontier
                        frontier.put((next_board_layout.cal_heuristic() + cur_gn + 1, cur_gn + 1, possible_solution, next_board_layout))
        return [] #return empty list if it's empty 


    # lets also define a helper function for heuristic
    #Recall that the Manhattan distance between two locations (r1, c1) and
    #(r2, c2) on a board is defined to be the sum of the componentwise distances:
    #|r1 − r2| + |c1 − c2|. The Manhattan distance heuristic for an entire puzzl
    #is then the sum of the Manhattan distances between each tile and its solved
    #location.
    def cal_heuristic(self):

        ret = 0 # set return value as 0 for now
        
        #loop through the whole board to calculate the sum of the Manhattan distance
        for i in range(self.row):
            for j in range(self.col):

                #make sure the current postion [i,j] is not the empty one
                if self.board[i][j] != 0:
                    
                    #i, j are the current location
                    current_x = i
                    current_y = j
                    #use divider and modulus to find the theoritcal location
                    sol_x = (self.board[i][j] - 1)/(self.col)
                    sol_y = (self.board[i][j] - 1)%(self.col)
                    #calculate the distance base on the formula
                    distance = abs(current_x - sol_x) + abs(current_y - sol_y)
                    #sum into ret
                    ret = ret + distance
        
        return ret
