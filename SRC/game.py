from tkinter import *
from tic_tac_toe import minmax_player, alpha_beta_player, random_player, TicTacToe
from test_game import gen_state
import time


ttt = TicTacToe()
root = None
buttons = []
frames = []
x_pos = []
o_pos = []
count = 0
sym = ""

def create_frames(root):
    """
    This function creates the necessary structure of the game.
    """
    frame1 = Frame(root, bg='black', height=300, width=300)  # Setting background color and size
    frame2 = Frame(root, bg='black', height=300, width=300)  # Setting background color and size
    frame3 = Frame(root, bg='black', height=300, width=300)  # Setting background color and size
    frame4 = Frame(root, bg='black')  # Setting background color

    create_buttons(frame1)
    create_buttons(frame2)
    create_buttons(frame3)

    buttonExit = Button(
        frame4, height=2, width=20,
        text="Exit", bg='red', fg='white', font=("Arial", 15), # Background and text color
        command=lambda: exit_game(root))
    buttonExit.pack(side=LEFT)

    frame4.pack(side=BOTTOM)
    frame3.pack(side=BOTTOM)
    frame2.pack(side=BOTTOM)
    frame1.pack(side=BOTTOM)

    frames.extend([frame1, frame2, frame3])  # Extending the list with frames

    for x in frames:
        buttons_in_frame = []
        for y in x.winfo_children():
            buttons_in_frame.append(y)
        buttons.append(buttons_in_frame)

    buttonReset = Button(
        frame4, height=2, width=20,
        text="Reset", bg='blue', fg='white', font=("Arial", 15),  # Background and text color
        command=lambda: reset_game())
    buttonReset.pack(side=LEFT)


def create_buttons(frame):
    """
    This function creates the buttons to be pressed/clicked during the game.
    """
    button0 = Button(frame, height=6, width=15, text=" ", bg='white', font=("Arial", 23),
                     command=lambda: on_click(button0))
    button0.pack(side=LEFT)

    button1 = Button(frame, height=6, width=15, text=" ", bg='white', font=("Arial", 23),
                     command=lambda: on_click(button1))
    button1.pack(side=LEFT)
    
    button2 = Button(frame, height=6, width=15, text=" ", bg='white', font=("Arial", 23),
                     command=lambda: on_click(button2))
    button2.pack(side=LEFT)


def on_click(button):
    """
    This function determines the action of any button.
    """
    global ttt, choices, count, sym, result, x_pos, o_pos

    if count % 2 == 0:
        sym = "X"
    else:
        sym = "O"
    count += 1

    button.config(
        text=sym,
        state='disabled',
        disabledforeground="red")  # For cross

    x, y = get_coordinates(button)
    x += 1
    y += 1
    x_pos.append((x, y))
    state = gen_state(to_move='O', x_positions=x_pos,
                      o_positions=o_pos)
    try:
        choice = choices.get()
        if "Random" in choice:
            start_time = time.time()
            a, b = random_player(ttt, state)
            end_time = time.time()
            time_taken = end_time - start_time
            time_label.config(text=f"Random move took: {time_taken:.6f} seconds")
        elif "Pro" in choice:
            start_time = time.time()
            a, b = minmax_player(ttt, state)
            end_time = time.time()
            time_taken = end_time - start_time
            time_label.config(text=f"Pro move took: {time_taken:.6f} seconds")
        else:
            start_time = time.time()
            a, b = alpha_beta_player(ttt, state)
            end_time = time.time()
            time_taken = end_time - start_time
            time_label.config(text=f"Legend move took: {time_taken:.6f} seconds")
    except (ValueError, IndexError, TypeError) as e:
        if check_victory(button):
            result.set("You win :)")
            disable_game()
            return
        else:    
            disable_game()
            result.set("It's a draw :|")
            return
    if 1 <= a <= 3 and 1 <= b <= 3:
        o_pos.append((a, b))
        button_to_change = get_button(a - 1, b - 1)
        if count % 2 == 0:  # Used again, will become handy when user is given the choice of turn.
            sym = "X"
        else:
            sym = "O"
        count += 1

        if check_victory(button):
            result.set("You win :)")
            disable_game()
        else:
            button_to_change.config(text=sym, state='disabled',
                                    disabledforeground="black")
            if check_victory(button_to_change):
                result.set("You lose :(")
                disable_game()


def check_victory(button):
    """
    This function checks various winning conditions of the game.
    """
    # check if previous move caused a win on vertical line
    global buttons
    x, y = get_coordinates(button)
    tt = button['text']
    if buttons[0][y]['text'] == buttons[1][y]['text'] == buttons[2][y]['text'] != " ":
        buttons[0][y].config(text="|" + tt + "|")
        buttons[1][y].config(text="|" + tt + "|")
        buttons[2][y].config(text="|" + tt + "|")
        return True

    # check if previous move caused a win on horizontal line
    if buttons[x][0]['text'] == buttons[x][1]['text'] == buttons[x][2]['text'] != " ":
        buttons[x][0].config(text="--" + tt + "--")
        buttons[x][1].config(text="--" + tt + "--")
        buttons[x][2].config(text="--" + tt + "--")
        return True

    # check if previous move was on the main diagonal and caused a win
    if x == y and buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != " ":
        buttons[0][0].config(text="\\" + tt + "\\")
        buttons[1][1].config(text="\\" + tt + "\\")
        buttons[2][2].config(text="\\" + tt + "\\")
        return True

    # check if previous move was on the secondary diagonal and caused a win
    if x + y == 2 and buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != " ":
        buttons[0][2].config(text="/" + tt + "/")
        buttons[1][1].config(text="/" + tt + "/")
        buttons[2][0].config(text="/" + tt + "/")
        return True

    return False


def get_coordinates(button):
    """
    This function returns the coordinates of the button clicked.
    """
    global buttons
    for x in range(len(buttons)):
        for y in range(len(buttons[x])):
            if buttons[x][y] == button:
                return x, y


def get_button(x, y):
    """
    This function returns the button memory location corresponding to a coordinate.
    """
    global buttons
    return buttons[x][y]


def reset_game():
    """
    This function will reset all the tiles to the initial null value.
    """
    global x_pos, o_pos, frames, count

    count = 0
    x_pos = []
    o_pos = []
    result.set("Your Turn!")
    for x in frames:
        for y in x.winfo_children():
            y.config(text=" ", state='normal')


def disable_game():
    """
    This function deactivates the game after a win, loss or draw.
    """
    global frames
    for x in frames:
        for y in x.winfo_children():
            y.config(state='disabled')


def exit_game(root):
    """
    This function will exit the game by killing the root.
    """
    root.destroy()


if __name__ == "__main__":
    global result, choices

    root = Tk()
    root.title("TicTacToe")
    root.attributes('-fullscreen', True)  # Set to full screen
    result = StringVar()
    result.set("Your Turn!")
    w = Label(root, textvariable=result, fg='yellow', bg='black', font=('Arial', 20))  # Text color, background, and font
    w.pack(side=BOTTOM)
    create_frames(root)
    choices = StringVar(root)
    choices.set("Vs Random")
    menu = OptionMenu(root, choices, "Vs Random", "Vs Pro", "Vs Legend")
    menu.config(font=("Arial", 16), bg='grey', fg='white')
    menu.pack()
    time_label = Label(root, text="", fg="blue")  # Create a label to display time
    time_label.pack()
    root.mainloop()