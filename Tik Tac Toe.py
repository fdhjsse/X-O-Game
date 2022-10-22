from tkinter import *
import random

command_list = []


def next_turn(r, c):
    global player
    global command_list
    global game_started
    command_list.append((r, c))
    if buttons[r][c]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[r][c]['text'] = player
            game_started = True
            if check_winner() is False:
                player = players[1]
                player_label.configure(text=(player + "'s turn"))
            elif check_winner() is True:
                player_label.configure(text=(player + " WINS!"))
            elif check_winner() == 'Tie':
                player_label.configure(text='TIE!')

        else:
            buttons[r][c]['text'] = player

            if check_winner() is False:
                player = players[0]
                player_label.configure(text=(player + "'s turn"))
            elif check_winner() is True:
                player_label.configure(text=(player + " WINS!"))
            elif check_winner() == 'Tie':
                player_label.configure(text='TIE!', bg='yellow')


def check_winner():
    # rows wise
    for r in range(3):
        if buttons[r][0]['text'] == buttons[r][1]['text'] == buttons[r][2]['text'] != "":
            buttons[r][0].configure(bg='green')
            buttons[r][1].configure(bg='green')
            buttons[r][2].configure(bg='green')
            return True

    # column wise
    for c in range(3):
        if buttons[0][c]['text'] == buttons[1][c]['text'] == buttons[2][c]['text'] != "":
            buttons[0][c].configure(bg='green')
            buttons[1][c].configure(bg='green')
            buttons[2][c].configure(bg='green')
            return True

    # diagonal wise
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].configure(bg='green')
        buttons[1][1].configure(bg='green')
        buttons[2][2].configure(bg='green')
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].configure(bg='green')
        buttons[1][1].configure(bg='green')
        buttons[2][0].configure(bg='green')
        return True

    if empty_space():
        return False
    return "Tie"


def empty_space():
    for r in range(3):
        for c in range(3):
            if buttons[r][c]['text'] == '':
                return True
    return False


def new_game():
    global player

    player = random.choice(players)

    player_label.configure(text=player + "'s turn")

    for r in range(3):
        for c in range(3):
            buttons[r][c].configure(text="", bg='grey')


def undo():
    global player
    if check_winner() is False and len(command_list) != 0:
        undo_row, undo_column = command_list[-1][0], command_list[-1][1]
        buttons[undo_row][undo_column]['text'] = ''
        if player == players[1]:
            player = players[0]
            player_label.configure(text=(player + "'s turn"))
        else:
            player = players[1]
            player_label.configure(text=(player + "'s turn"))
        command_list.pop()


mainWindow = Tk()
mainWindow.title("Tic-Tac-Toe")
mainWindow.configure(background='grey')
players = ["X", "O"]

# pick a random player.
player = random.choice(players)

# end button
end_button = Button(mainWindow, text="Close", background='red', font=('consolas', 20), command=mainWindow.destroy)
end_button.pack(anchor='w')

player_label = Label(mainWindow, text=player + "'s turn", font=('consolas', 40))
player_label.pack(side='top')

reset_button = Button(mainWindow, text='New Game', font=('consolas', 20), command=new_game)
reset_button.pack(side='top')


# undo button
undo_button = Button(mainWindow, text='Undo', font=('consolas', 20), command=undo)
undo_button.pack(side='top', anchor='e')

# Buttons structure
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Game Board.
board = Frame(mainWindow)
board.configure(background='grey')
board.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(board, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda bt_row=row, bt_column=column:
                                      next_turn(bt_row, bt_column))
        buttons[row][column].grid(row=row, column=column)
        buttons[row][column].configure(background='grey')


mainWindow.mainloop()