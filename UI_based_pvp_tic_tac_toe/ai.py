import math
from logic import check_winner

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "X": return -1
    if winner == "O": return 1
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def minimax_ab(board, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X": return -1
    if winner == "O": return 1
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax_ab(board, False, alpha, beta)
                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax_ab(board, True, alpha, beta)
                board[i] = " "
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board, algorithm):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if algorithm == "Minimax":
                score = minimax(board, False)
            elif algorithm == "AlphaBeta":
                score = minimax_ab(board, False, -math.inf, math.inf)
            else:
                score = 0
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move