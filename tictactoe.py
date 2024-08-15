import tkinter
from tkinter import messagebox

def print_winner(winning_buttons):
    global win

    if win is False:
        win = True
        for btn in winning_buttons:
            btn.config(bg="lightgreen")
        messagebox.showinfo("Félicitations!", f"Le joueur {current_player} a gagné le jeu!")
        reset_game()

def switch_player():
    global current_player
    current_player = '0' if current_player == 'X' else 'X'

def check_win(clicked_row, clicked_col):
    winning_buttons = []

    # Victoire horizontale
    if all(buttons[clicked_row][i]['text'] == current_player for i in range(3)):
        winning_buttons = [buttons[clicked_row][i] for i in range(3)]
        print_winner(winning_buttons)

    # Victoire verticale
    elif all(buttons[i][clicked_col]['text'] == current_player for i in range(3)):
        winning_buttons = [buttons[i][clicked_col] for i in range(3)]
        print_winner(winning_buttons)

    # Victoire diagonale
    elif all(buttons[i][i]['text'] == current_player for i in range(3)):
        winning_buttons = [buttons[i][i] for i in range(3)]
        print_winner(winning_buttons)

    # Victoire diagonale inversée
    elif all(buttons[i][2-i]['text'] == current_player for i in range(3)):
        winning_buttons = [buttons[i][2-i] for i in range(3)]
        print_winner(winning_buttons)

    # Match nul
    elif not win and all(buttons[row][col]['text'] != "" for row in range(3) for col in range(3)):
        messagebox.showinfo("Match nul", "Match nul!")
        reset_game()

def place_symbol(row, column):
    if not win and buttons[row][column]['text'] == "":
        buttons[row][column].config(text=current_player)
        check_win(row, column)
        if not win:
            switch_player()

def draw_grid():
    for row in range(3):
        buttons_in_row = []
        for col in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50), width=5, height=3,
                command=lambda r=row, c=col: place_symbol(r, c)
            )
            button.grid(row=row, column=col)
            buttons_in_row.append(button)
        buttons.append(buttons_in_row)

def reset_game():
    global win, current_player
    win = False
    current_player = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="SystemButtonFace")

# Stockages
buttons = []
current_player = 'X'
win = False

# Créer la fenêtre 
root = tkinter.Tk()

# Personnalisation de la fenêtre
root.title("TicTacToe")
root.minsize(500, 500)

draw_grid()
root.mainloop()
