"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    ## Count the number of X and O in the board
    n_x = 0
    n_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                n_x += 1
            elif board[i][j] == O:
                n_o += 1
    
    ## X plays in odd turns (i.e., turns where the amount of X and O at the board are the equal)
    if n_x == n_o:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ## Declaring a set of actions
    actions = {}

    for i in range(3):
        for j in range(3):

            ## Put an action in the set, if the position is EMPTY
            if board[i][j] == EMPTY:
                actions.append((i, j))
    
    return actions


    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    ## Check if the position related in the action is already taken
    if board[action[0]][action[1]] != EMPTY:
        print("Action not valid")
        raise NotImplementedError

    ## If it is not already taken ("EMPTY")
    else:
        #Creates a copy of the board
        board_copy = copy.deepcopy(board)

        ## Check whos turn it is to define the move
        move = ""
        if player(board_copy) == X:
            move = X
        else:
            move = O

        ## Apply the move at the desired position
        for i in range(3):
            for j in range(3):
                if i == action[0] and j == action[1]:
                    board_copy[i][j] = move

        # returns the copy of the board
        return board_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    ## Define all win possibilities by the positions taken by any player
    win_possibilities = {
                        {(0,0), (0,1), (0,2)},
                        {(1,0), (1,1), (1,2)},
                        {(2,0), (2,1), (2,2)},

                        {(0,0), (1,0), (2,0)},
                        {(0,1), (1,1), (2,1)},
                        {(0,2), (1,2), (2,2)},
                        
                        {(0,0), (1,1), (2,2)},
                        {(2,0), (1,1), (0,2)}
                        }


    # Take the positions taken by each player
    x_positions = {}
    o_positions = {}

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_positions.append((i, j))
            elif board[i][j] == O:
                o_positions.append((i,j))

    # The winner is the one who meets any of the win possibilitie.
    if x_positions in win_possibilities:
        return X
    elif o_positions in win_possibilities:
        return O
    else:
        return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    ## If there is a winner, the game is over
    if winner(board) != None:
        return True
    
    else:

        ## Count the number of X and O in the board
        n_x = 0
        n_o = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    n_x += 1
                elif board[i][j] == O:
                    n_o += 1

        ## If the board is totally filled, the game is over and its a tie (since there is no winner). Else it is still going
        if n_x + n_o == 9:
            return True
        else:
            return False


    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError

def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = -100
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = +100
        for action in action(board):
            v = min(v, max_value(result(board, action)))
        return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    ## Take all possible actions
    actions = actions(board)
   
    ## The best action for max player
    if player(board) == X:

        ## create a list of  the min values of all possible states (it means, the min value of each possible state if both players play optimally)
        states_min_values = []
        for action in actions:
            states_min_values.append(min_value(result(board, action)))
        
        ## picks the state that has the max value in the list
        max_value = max(states_min_values)
        pos_max_value = index(max_value)
        best_x_action = action[pos_max_value]

        return best_x_action


        ## The best action for min player
    elif player(board) == O:

        ## create a list of the max values of all possible states (it means, the max value of each possible state if both players play optimally)
        states_max_values = []
        for action in actions:
            states_max_values.append(max_value(result(board, action)))
        
        ## picks the state that has the min value in the list
        min_value = min(states_max_values)
        pos_min_value = index(min_value)
        best_o_action = action[pos_min_value]

        return best_o_action


        
        
    raise NotImplementedError
