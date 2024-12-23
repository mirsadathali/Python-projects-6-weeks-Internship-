import tkinter as tk
import random

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Puzzle")

        self.grid_size = 4
        self.score = 0
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.tiles = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                label = tk.Label(self.frame, text='', font=('Helvetica', 24), width=4, height=2, bg='lightgray', borderwidth=1, relief="solid")
                label.grid(row=i, column=j, padx=5, pady=5)
                row.append(label)
            self.tiles.append(row)

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=('Helvetica', 16))
        self.score_label.pack(pady=10)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.start_game)
        self.restart_button.pack()

        self.root.bind("<Up>", lambda event: self.move("up"))
        self.root.bind("<Down>", lambda event: self.move("down"))
        self.root.bind("<Left>", lambda event: self.move("left"))
        self.root.bind("<Right>", lambda event: self.move("right"))

    def start_game(self):
        self.score = 0
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.add_new_tile()
        self.add_new_tile()
        self.update_ui()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        original_grid = [row[:] for row in self.grid]
        if direction == "up":
            self.grid = self.transpose(self.grid)
            for i in range(self.grid_size):
                self.grid[i] = self.merge(self.grid[i])
            self.grid = self.transpose(self.grid)
        elif direction == "down":
            self.grid = self.transpose(self.grid)
            for i in range(self.grid_size):
                self.grid[i] = self.merge(self.grid[i][::-1])[::-1]
            self.grid = self.transpose(self.grid)
        elif direction == "left":
            for i in range(self.grid_size):
                self.grid[i] = self.merge(self.grid[i])
        elif direction == "right":
            for i in range(self.grid_size):
                self.grid[i] = self.merge(self.grid[i][::-1])[::-1]

        if original_grid != self.grid:
            self.add_new_tile()
            self.update_ui()
            if self.check_game_over():
                self.show_game_over()

    def merge(self, row):
        non_zero = [value for value in row if value != 0]
        merged = []
        skip = False
        for j in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if j + 1 < len(non_zero) and non_zero[j] == non_zero[j + 1]:
                merged.append(non_zero[j] * 2)
                self.score += non_zero[j] * 2
                skip = True
            else:
                merged.append(non_zero[j])
        merged.extend([0] * (self.grid_size - len(merged)))
        return merged

    def transpose(self, matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def update_ui(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                self.tiles[i][j].config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))
        self.score_label.config(text=f"Score: {self.score}")

    def get_tile_color(self, value):
        colors = {
            0: "lightgray",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e"
        }
        return colors.get(value, "#3c3a32")

    def check_game_over(self):
        if any(0 in row for row in self.grid):
            return False
        for i in range(self.grid_size):
            for j in range(self.grid_size - 1):
                if self.grid[i][j] == self.grid[i][j + 1] or self.grid[j][i] == self.grid[j + 1][i]:
                    return False
        return True

    def show_game_over(self):
        game_over_popup = tk.Toplevel(self.root)
        game_over_popup.title("Game Over")
        tk.Label(game_over_popup, text=f"Game Over! Your score: {self.score}", font=('Helvetica', 16)).pack(pady=20)
        tk.Button(game_over_popup, text="Restart", command=lambda: [game_over_popup.destroy(), self.start_game()]).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
