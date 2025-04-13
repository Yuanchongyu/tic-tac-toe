def print_board(board):
    """
    打印棋盘。
    board 是一个长度为9的列表，每3个元素表示一行。
    不使用 join，让代码更容易理解。
    """
    print()
    for i in range(3):
        # 打印一行中的三个格子
        print("", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2])
        
        # 打印分隔线（除了最后一行）
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    """
    检查是否有玩家赢了，或平局，或尚未结束。
    返回值：
        'X'  表示 X 获胜
        'O'  表示 O 获胜
        'Draw' 表示平局
        None 表示暂未分出胜负
    """
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),  # 行
        (0,3,6), (1,4,7), (2,5,8),  # 列
        (0,4,8), (2,4,6)            # 对角线
    ]
    for a,b,c in win_patterns:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]  # 'X' 或 'O'

    if " " not in board:  # 没有空位了，平局
        return "Draw"
    return None


def main():
    board = [" "] * 9  # 9 个空格，代表 3×3 棋盘
    current_player = "X"  # 先手玩家用 'X'
    
    print("欢迎来到井字棋游戏（双人对战）！")
    print("棋盘位置对应：")
    print("""
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    """)
    print("玩家 X 先行，输入 1-9 选择落子位置。\n")

    while True:
        print_board(board)
        move_str = input(f"玩家 {current_player}，请选择要落子的位置 (1-9)： ")

        # 输入校验
        if not move_str.isdigit():
            print("输入无效，请输入数字 1-9。")
            continue
        
        move = int(move_str)
        if move < 1 or move > 9:
            print("输入无效，请输入数字 1-9。")
            continue
        
        if board[move - 1] != " ":
            print("该位置已经被占用，请重新选择。")
            continue
        
        # 执行落子
        board[move - 1] = current_player

        # 检查结果
        result = check_winner(board)
        if result == "X":
            print_board(board)
            print("游戏结束，玩家 X 获胜！")
            break
        elif result == "O":
            print_board(board)
            print("游戏结束，玩家 O 获胜！")
            break
        elif result == "Draw":
            print_board(board)
            print("游戏结束，平局！")
            break

        # 切换玩家
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()


# [" ", "X", " ", " ", "O", " ", " ", " ", " ", " "]
