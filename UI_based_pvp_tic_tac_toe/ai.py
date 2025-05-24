import math
from logic import check_winner
import random
import copy

def minimax(board, is_maximizing, size):
    winner = check_winner(board, size)
    if winner == "X": return -1
    if winner == "O": return 1
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(size * size):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False, size)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(size * size):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True, size)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def minimax_ab(board, is_maximizing, alpha, beta, size):
    winner = check_winner(board, size)
    if winner == "X": return -1
    if winner == "O": return 1
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(size * size):
            if board[i] == " ":
                board[i] = "O"
                score = minimax_ab(board, False, alpha, beta, size)
                board[i] = " "
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(size * size):
            if board[i] == " ":
                board[i] = "X"
                score = minimax_ab(board, True, alpha, beta, size)
                board[i] = " "
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board, algorithm, size):
    if algorithm == "MonteCarlo":
        return monte_carlo_move(board, size, num_simulations=500)

    best_score = -math.inf
    move = -1
    for i in range(size * size):
        if board[i] == " ":
            board[i] = "O"
            if algorithm == "Minimax":
                score = minimax(board, False, size)
            elif algorithm == "AlphaBeta":
                score = minimax_ab(board, False, -math.inf, math.inf, size)
            else:
                score = 0
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def random_playout(board, current_player, size):
    temp_board = copy.deepcopy(board)

    while True:
        winner = check_winner(temp_board, size)
        if winner:
            return winner

        available_moves = []  # 创建一个空列表，用来存放可用的位置

        for i in range(size * size):  # 遍历棋盘上的所有格子
            if temp_board[i] == " ":  # 如果该格子是空的（表示还没有落子）
                available_moves.append(i)  # 就把这个格子的索引加入到列表中
        if not available_moves:
            return "Draw"

        move = random.choice(available_moves)
        temp_board[move] = current_player
        current_player = "X" if current_player == "O" else "O"

def monte_carlo_move(board, size, num_simulations=500):
    move_scores = [0] * (size * size)

    for i in range(size * size):
        if board[i] != " ":
            continue

        win_count = 0
        for _ in range(num_simulations):
            temp_board = board[:]
            temp_board[i] = "O"
            result = random_playout(temp_board, "X", size)

            if result == "O":
                win_count += 1
            elif result == "Draw":
                win_count += 0.5

        move_scores[i] = win_count / num_simulations

    best_move_index = max(range(size * size), key=lambda x: move_scores[x])
    return best_move_index