import tkinter as tk
from tkinter import messagebox
from ai import best_move  # 确保 ai.py 中包含 Monte Carlo 支持
from logic import check_winner

class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("井字棋游戏 | Tic-Tac-Toe")
        self.set_window_size(800, 800)
        self.root.configure(bg="#f0f8ff")

        self.buttons = []
        self.current_player = "X"
        self.mode = tk.StringVar(value="")
        self.algorithm = tk.StringVar(value="Minimax")
        self.board_size = 3
        self.setup_board_size()

    def set_window_size(self, width, height):
        self.window_width = width
        self.window_height = height
        self.root.geometry(f"{width}x{height}")

    def setup_mode_selection(self, size):
        self.board_size = size
        self.board = [" "] * size * size

        self.clear_window()
        self.set_window_size(800, 800)
        self.current_player = "X"

        tk.Label(self.root, text="选择游戏模式:", font=("Arial", 14), bg="#10f8ef").pack(pady=10)
        tk.Button(self.root, text="玩家 vs 玩家", font=("Arial", 12), width=20,
                  command=lambda: self.start_game("PvP")).pack(pady=50)
        tk.Button(self.root, text="玩家 vs AI", font=("Arial", 12), width=20,
                  command=self.setup_ai_algorithm_selection).pack(pady=5)

    def setup_board_size(self):
        self.clear_window()
        self.set_window_size(800, 800)
        self.current_player = "X"

        tk.Label(self.root, text="选择棋盘大小:", font=("Arial", 14), bg="#10f8ef").pack(pady=10)
        tk.Button(self.root, text="3 * 3", font=("Arial", 12), width=20,
                  command=lambda: self.setup_mode_selection(3)).pack(pady=50)
        tk.Button(self.root, text="4 * 4", font=("Arial", 12), width=20,
                  command=lambda: self.setup_mode_selection(4)).pack(pady=5)


    def setup_ai_algorithm_selection(self):
        self.clear_window()
        self.set_window_size(800, 800)
        tk.Label(self.root, text="选择 AI 算法:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)

        tk.Button(self.root, text="Minimax", font=("Arial", 12), width=20,
                  command=lambda: self.start_game("PvAI", "Minimax")).pack(pady=20)
        tk.Button(self.root, text="Alpha-Beta 剪枝", font=("Arial", 12), width=20,
                  command=lambda: self.start_game("PvAI", "AlphaBeta")).pack(pady=20)
        tk.Button(self.root, text="Monte Carlo", font=("Arial", 12), width=20,
                  command=lambda: self.start_game("PvAI", "MonteCarlo")).pack(pady=20)

    def start_game(self, mode, algorithm="Minimax"):
        self.mode.set(mode)
        self.algorithm.set(algorithm)

        self.clear_window()
        self.set_window_size(800, 800)

        self.status_label = tk.Label(self.root, text="玩家 X 的回合", font=("Arial", 16), bg="#f0f8ff")
        self.status_label.pack(pady=10)

        self.frame = tk.Frame(self.root, bg="#f0f8ff")
        self.frame.pack()

        for i in range(self.board_size * self.board_size):
            btn = tk.Button(self.frame, text=" ", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=i // self.board_size, column=i % self.board_size)
            self.buttons.append(btn)

        self.reset_button = tk.Button(self.root, text="重新开始", font=("Arial", 12), command=self.setup_board_size)
        self.reset_button.pack(pady=10)

    def player_move(self, index):
        if self.board[index] != " ":
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        winner = check_winner(self.board, self.board_size)
        if winner:
            self.end_game(winner)
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(text=f"玩家 {self.current_player} 的回合")

        if self.mode.get() == "PvAI" and self.current_player == "O":
            self.root.after(50, self.ai_move)

    def ai_move(self):
        move = best_move(self.board, self.algorithm.get(), self.board_size)
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
        self.board = [" "] * self.board_size * self.board_size










# import tkinter as tk
# from tkinter import messagebox
# from ai import best_move
# from logic import check_winner

# class TicTacToeUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("井字棋游戏 | Tic-Tac-Toe")
#         self.set_window_size(800, 800)
#         self.root.configure(bg="#f0f8ff")

#         self.board = []
#         self.buttons = []
#         self.current_player = "X"
#         self.mode = tk.StringVar(value="")
#         self.algorithm = tk.StringVar(value="Minimax")
#         self.board_size = 3

#         self.setup_board_size_selection()

#     def set_window_size(self, width, height):
#         self.root.geometry(f"{width}x{height}")

#     def setup_board_size_selection(self):
#         self.clear_window()
#         tk.Label(self.root, text="选择棋盘大小:", font=("Arial", 14), bg="#10f8ef").pack(pady=10)
#         btn_3x3 = tk.Button(
#             self.root,
#             text="3 x 3",
#             font=("Arial", 12),
#             width=20,
#             command=lambda: self.setup_mode_selection(3)
#         )
#         btn_3x3.pack(pady=10)

#         btn_4x4 = tk.Button(
#             self.root,
#             text="4 x 4",
#             font=("Arial", 12),
#             width=20,
#             command=lambda: self.setup_mode_selection(4)
#         )
#         btn_4x4.pack(pady=10)



#     def setup_mode_selection(self,size):
#         self.board_size = size

#         self.clear_window()
#         self.current_player = "X"
#         tk.Label(self.root, text="选择游戏模式:", font=("Arial", 14), bg="#10f8ef").pack(pady=10)
#         tk.Button(self.root, text="玩家 vs 玩家", font=("Arial", 12), width=20,
#                   command=lambda: self.start_game("PvP")).pack(pady=50)
#         tk.Button(self.root, text="玩家 vs AI", font=("Arial", 12), width=20,
#                   command=self.setup_ai_algorithm_selection).pack(pady=5)

#     def setup_ai_algorithm_selection(self):
#         self.clear_window()
#         tk.Label(self.root, text="选择 AI 算法:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
#         tk.Button(self.root, text="Minimax", font=("Arial", 12), width=20,
#                   command=lambda: self.start_game("PvAI", "Minimax")).pack(pady=20)
#         tk.Button(self.root, text="Alpha-Beta 剪枝", font=("Arial", 12), width=20,
#                   command=lambda: self.start_game("PvAI", "AlphaBeta")).pack(pady=20)
#         tk.Button(self.root, text="Monte Carlo", font=("Arial", 12), width=20,
#                   command=lambda: self.start_game("PvAI", "MonteCarlo")).pack(pady=20)

#     def start_game(self, mode, algorithm="Minimax"):
#         self.mode.set(mode)
#         self.algorithm.set(algorithm)

#         self.clear_window()
#         size = self.board_size
#         self.board = [" "] * (size * size)
#         self.set_window_size(800, 800)

#         self.status_label = tk.Label(self.root, text="玩家 X 的回合", font=("Arial", 16), bg="#f0f8ff")
#         self.status_label.pack(pady=10)

#         self.frame = tk.Frame(self.root, bg="#f0f8ff")
#         self.frame.pack()

#         self.buttons = []
#         for i in range(size * size):
#             btn = tk.Button(self.frame, text=" ", font=("Arial", 24), width=5, height=2,
#                             command=lambda i=i: self.player_move(i))
#             btn.grid(row=i // size, column=i % size)
#             self.buttons.append(btn)

#         self.reset_button = tk.Button(self.root, text="重新开始", font=("Arial", 12), command=self.setup_board_size_selection)
#         self.reset_button.pack(pady=10)

#     def player_move(self, index):
#         if self.board[index] != " ":
#             return

#         self.board[index] = self.current_player
#         self.buttons[index].config(text=self.current_player)

#         winner = check_winner(self.board, self.board_size)
#         if winner:
#             self.end_game(winner)
#             return

#         self.current_player = "O" if self.current_player == "X" else "X"
#         self.status_label.config(text=f"玩家 {self.current_player} 的回合")

#         if self.mode.get() == "PvAI" and self.current_player == "O":
#             self.root.after(50, self.ai_move)

#     def ai_move(self):
#         move = best_move(self.board, self.algorithm.get(), self.board_size.get())
#         if move != -1:
#             self.player_move(move)

#     def end_game(self, result):
#         if result == "Draw":
#             messagebox.showinfo("游戏结束", "平局！")
#         else:
#             messagebox.showinfo("游戏结束", f"玩家 {result} 获胜！")
#         for btn in self.buttons:
#             btn.config(state=tk.DISABLED)

#     def reset_game(self):
#         self.setup_mode_selection()

#     def clear_window(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()
#         self.buttons = []
#         self.board = []
