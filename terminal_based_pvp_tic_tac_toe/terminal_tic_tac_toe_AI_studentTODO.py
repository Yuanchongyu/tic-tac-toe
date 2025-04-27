import math

def print_board(board):
    print()
    for i in range(3):
        print("", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2])
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_patterns:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "Draw"
    return None

def minimax(board, is_maximizing):
    # todo
    pass

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def minimax_ab(board, is_maximizing, alpha, beta):
    # todo
    pass

def best_move_ab(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax_ab(board, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    board = [" "] * 9
    print("选择游戏模式：")
    print("1. 双人对战")
    print("2. 玩家 vs AI (Minimax)")
    print("3. 玩家 vs AI (Alpha-Beta)")
    mode = input("请输入 1、2 或 3：")

    current_player = "X"

    while True:
        print_board(board)
        if (mode == "2" or mode == "3") and current_player == "O":
            print("AI 正在思考...")
            move = best_move(board) if mode == "2" else best_move_ab(board)
        else:
            move_str = input(f"玩家 {current_player}，请选择要落子的位置 (1-9)： ")
            if not move_str.isdigit() or not (1 <= int(move_str) <= 9):
                print("无效输入，请输入 1 到 9 的数字。")
                continue
            move = int(move_str) - 1
            if board[move] != " ":
                print("该位置已被占用，请选择其他位置。")
                continue

        board[move] = current_player
        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Draw":
                print("游戏结束，平局！")
            else:
                print(f"游戏结束，玩家 {result} 获胜！")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
