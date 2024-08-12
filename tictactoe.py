import tkinter

def draw_grid():
    for i in range(3):
        for j in range(3):
            button = tkinter.Button(root)
            button.grid(row=j, column=i)

# cree fenetre
root = tkinter.Tk()

# personnalisation fenetre
root.title("TicTacToe")
root.minsize(500,500)

draw_grid()

root.mainloop()

