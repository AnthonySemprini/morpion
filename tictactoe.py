import tkinter


def place_symbole(row, column):
    print(f"Clic sur la ligne {row}, colonne {column}")

    clicked_button = buttons[column][row]
    clicked_button.config(text="X")

def draw_grid():
    for column in range(3):
        button_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbole(r, c)
            )
            button.grid(row=row, column=column)
            button_in_cols.append(button)
        buttons.append(button_in_cols)

# stockage
buttons = []

# cree fenetre
root = tkinter.Tk()

# personnalisation fenetre
root.title("TicTacToe")
root.minsize(500,500)

draw_grid()

root.mainloop()

