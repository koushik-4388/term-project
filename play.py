from tkinter import Tk, Label, Button, PhotoImage, messagebox, TOP, Frame,Label


from state import state



def render_board(game, frame, imgs):
    pick_img = {
        0: imgs[2],
        state.HUMAN: imgs[1],
        state.BOMB: imgs[0]
    }

    for i in range(5):
        for j in range(5):
            Button(frame, command = lambda col = j, row = i: human_move(game, frame, imgs, row, col), image=pick_img[game.gameboard.check(i, j)]).grid(row=i, column=j)

def human_move(game, frame, imgs,row, col):
     render_board(game, frame, imgs)
     try:
         game.human_choice(row,col)
         render_board(game, frame, imgs)
     except:
         if game.bombcheck(row,col):
             game.gameboard.select(row,col,4)
             render_board(game, frame, imgs)
             messagebox.showinfo("GAME OVER","You stepped on a mine\n BETTER LUCK NEXT TIME!!!!!!")
             quit()
         if game.win():
             messagebox.showinfo("YOU WON THE GAME!!!!!!","WINNER WINNER CHICKEN DINNER")
             quit()

if __name__ == "__main__":
    game = state.new()

    # create tkinter window
    win = Tk()
    text = Label(win,text = "about the game:\tcarefully avoid the mines by not tapping them\n\t\t if you do ka-boooooommm!!!!!!!!")
    text.pack()
    win.title("PPAF - MINESWEEPER--- watch your step")
    imgs = [PhotoImage(file = f) for f in ['green_blob.png', 'blue_blob.png', 'white_blob.png', 'base_line.png']]

    # align frames
    top_frame = Frame(win)
    top_frame.pack(side=TOP)
    bottom_frame = Frame(win)
    bottom_frame.pack(side=TOP)


    bbase = Label(top_frame, image=imgs[3])
    bbase.pack(side=TOP)

    render_board(game, bottom_frame, imgs)
    win.mainloop()
