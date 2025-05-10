import tkinter as tk
from tkinter import messagebox
from ai import best_move
from logic import check_winner

class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("井字棋游戏 | Tic-Tac-Toe")
        self.set_window_size(400, 450)
        self.root.configure(bg="#f0f8ff")  # 设置背景色

        self.board = [" "] * 9
        self.buttons = []
        self.current_player = "X"
        self.mode = tk.StringVar(value="")
        self.algorithm = tk.StringVar(value="Minimax")

        self.setup_mode_selection()

    def set_window_size(self, width, height):
        self.window_width = width
        self.window_height = height
        self.root.geometry(f"{width}x{height}")


    def setup_mode_selection(self):
        self.clear_window()
        self.set_window_size(400, 450)
        tk.Label(self.root, text="选择游戏模式:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Button(self.root, text="玩家 vs 玩家", font=("Arial", 12), width=20, command=lambda: self.start_game("PvP")).pack(pady=50)
        tk.Button(self.root, text="玩家 vs AI", font=("Arial", 12), width=20, command=self.setup_ai_algorithm_selection).pack(pady=5)

    def setup_ai_algorithm_selection(self):
        self.clear_window()
        self.set_window_size(400, 450)
        tk.Label(self.root, text="选择 AI 算法:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
        tk.Button(self.root, text="Minimax", font=("Arial", 12), width=20, command=lambda: self.start_game("PvAI", "Minimax")).pack(pady=50)
        tk.Button(self.root, text="Alpha-Beta 剪枝", font=("Arial", 12), width=20, command=lambda: self.start_game("PvAI", "AlphaBeta")).pack(pady=5)


    def start_game(self, mode, algorithm="Minimax"):
        self.mode.set(mode)
        self.algorithm.set(algorithm)

        self.clear_window()
        self.set_window_size(400, 450)

        self.status_label = tk.Label(self.root, text="玩家 X 的回合", font=("Arial", 16), bg="#f0f8ff")
        self.status_label.pack(pady=10)

        self.frame = tk.Frame(self.root, bg="#f0f8ff")
        self.frame.pack()

        for i in range(9):
            btn = tk.Button(self.frame, text=" ", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        self.reset_button = tk.Button(self.root, text="重新开始", font=("Arial", 12), command=self.setup_mode_selection)
        self.reset_button.pack(pady=10)

    def player_move(self, index):
        if self.board[index] != " ":
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        winner = check_winner(self.board)
        if winner:
            self.end_game(winner)
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"玩家 {self.current_player} 的回合")

        if self.mode.get() == "PvAI" and self.current_player == "O":
            self.root.after(50, self.ai_move)

    def ai_move(self):
        move = best_move(self.board, self.algorithm.get())
        if move != -1:
            self.player_move(move)

    def end_game(self, result):
        if result == "Draw":
            messagebox.showinfo("游戏结束", "平局！")
        else:
            messagebox.showinfo("游戏结束", f"玩家 {result} 获胜！")
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def reset_game(self):
        self.setup_mode_selection()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.buttons = []
        self.board = [" "] * 9
