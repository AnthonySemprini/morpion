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
    global grid_frame
    grid_frame = tkinter.Frame(root)
    grid_frame.pack(expand=True)
    
    for row in range(3):
        buttons_in_row = []
        for col in range(3):
            button = tkinter.Button(
                grid_frame, font=("Arial", 50), width=5, height=3,
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
    
    show_home_screen()

def start_game():
    home_frame.pack_forget()
    grid_frame.pack(expand=True)
    root.update_idletasks()  # Force la mise à jour de l'interface

def show_home_screen():
    grid_frame.pack_forget()
    home_frame.pack(expand=True)
    root.update_idletasks()  # Force la mise à jour de l'interface

# Stockages
buttons = []
current_player = 'X'
win = False

# Créer la fenêtre 
root = tkinter.Tk()

# Personnalisation de la fenêtre
root.title("TicTacToe")
root.minsize(500, 500)

# Créer la page d'accueil
home_frame = tkinter.Frame(root)
welcome_label = tkinter.Label(home_frame, text="Bienvenue au Tic-Tac-Toe!", font=("Arial", 24))
start_button = tkinter.Button(home_frame, text="Commencer le jeu", font=("Arial", 18), command=start_game)
welcome_label.pack(pady=20)
start_button.pack()

# Créer la grille mais ne pas l'afficher
draw_grid()

# Afficher la page d'accueil
show_home_screen()

root.mainloop()
