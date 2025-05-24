# 判断一组格子是否都相同且非空
def all_same(cells):
    first = cells[0]
    if first == " ":
        return False
    for cell in cells:
        if cell != first:
            return False
    return True

def check_winner(board, size):
    # 检查每一行
    for row in range(size):
        cells = []
        for col in range(size):
            index = row * size + col
            cells.append(board[index])
        if all_same(cells):
            return cells[0]

    # 检查每一列
    for col in range(size):
        cells = []
        for row in range(size):
            index = row * size + col
            cells.append(board[index])
        if all_same(cells):
            return cells[0]

    # 检查主对角线（左上到右下）
    diag1 = []
    for i in range(size):
        index = i * size + i
        diag1.append(board[index])
    if all_same(diag1):
        return diag1[0]

    # 检查副对角线（右上到左下）
    diag2 = []
    for i in range(size):
        index = i * size + (size - 1 - i)
        diag2.append(board[index])
    if all_same(diag2):
        return diag2[0]

    # 检查是否平局
    is_draw = True
    for cell in board:
        if cell == " ":
            is_draw = False
            break
    if is_draw:
        return "Draw"

    # 游戏未结束
    return None