from tkinter import *
from tkinter import ttk
import time
import random

# main window------------------------------------------------------------------
root = Tk()
root.title("ABC Pairs Game")
root.resizable(0, 0)
root.geometry("545x485")
root.configure(bg="#2e8b57")
backB = PhotoImage(file="bg.png")
first = None


# variables--------------------------------------------------------------------
buttons = Button(root)
buttons2 = Button(root)
picture = 0
score = 0
sc_l = Label(root)
start_t = 0
remaining = 0
label_s = Label(root)
lab_l = Label(root)
label_L = Label(root)
count_l = Label(root)
count = 0
w_label = Label(root)
b_try = Button(root)
w_frame = Frame(root)
button_e = Button(root)
b_next = Button(root)
b_pre = Button(root)
picture2 = 0
count_l2 = Label(root)

count_00 = 0
count_01 = 0
count_02 = 0
count_03 = 0
count_10 = 0
count_11 = 0
count_12 = 0
count_13 = 0
count_20 = 0
count_21 = 0
count_22 = 0
count_23 = 0

# pictures---------------------------------------------------------------------
le_im = PhotoImage(file="level.png")
st = PhotoImage(file="start.png")
level1 = PhotoImage(file="level1.png")
again = PhotoImage(file="try.png")
cover = PhotoImage(file="cover.png")
so_im = PhotoImage(file="score.png")
im1 = PhotoImage(file="dog.png")
im2 = PhotoImage(file="money.png")
im3 = PhotoImage(file="heart.png")
rules = PhotoImage(file="rul.png")
ex = PhotoImage(file="exit.png")
ru = PhotoImage(file="scorein.png")
nextl = PhotoImage(file="nextl.png")
level2 = PhotoImage(file="level2.png")
b_p = PhotoImage(file="pre.png")
im4 = PhotoImage(file="pizza.png")
im5 = PhotoImage(file="burger.png")
im6 = PhotoImage(file="sun.png")
dark = PhotoImage(file="dark.png")
frame_s = Frame(root, bg="#FFFFFF")
frame_s.grid(row=2, column=2)
l_rules = Label(root, image=ru)
l_rules.grid(row=1, column=0, columnspan=5)
c_frame = Label(root, image=cover)
c_frame.grid(row=0, column=0, columnspan=5)
style = ttk.Style()
style.configure("TLabel", foreground="green", font=("American Typewriter", 35))


# start game -------------------------------------------------------------------
def game_start():
    global lab_l
    global buttons

    picture_list()
    create_score_level()
    l_rules.destroy()
    create_buttons()
    c_frame.destroy()
    start_time()
    countdown(60)
    bu_st.destroy()
    frame_s.destroy()
    lab_l.config(image=level1)
    for row in buttons:
        for button in row:
            button.config(state=NORMAL)

bu_st = Button(frame_s, image=st, state=NORMAL,command=game_start)
bu_st.pack()


# level _1 try again --------------------------------------------------------------
def try_again1():

    global buttons
    global picture
    global score
    global sc_l
    global start_t
    global remaining
    global lab_l
    global count_l
    global count
    global w_label
    global b_try
    global w_frame
    global button_e
    global b_pre
    global buttons2

    global count_00
    global count_01
    global count_02
    global count_03
    global count_10
    global count_11
    global count_12
    global count_13
    global count_20
    global count_21
    global count_22
    global count_23

    for row in range(3):
        for column in range(4):
            buttons[row][column].destroy()

    w_frame.destroy()
    w_label.destroy()
    button_e.destroy()
    b_try.destroy()
    b_pre.destroy()


    picture = 0
    score = 0
    start_t = 0
    remaining = 0
    count = 0
    count_l = Label(root)
    count_00 = 0
    count_01 = 0
    count_02 = 0
    count_03 = 0
    count_10 = 0
    count_11 = 0
    count_12 = 0
    count_13 = 0
    count_20 = 0
    count_21 = 0
    count_22 = 0
    count_23 = 0

    sc_l["text"] = score
    picture_list()
    create_buttons()
    start_time()
    countdown(60)
    lab_l.config(image=level1)

    for row in buttons:
        for button in row:
            button.config(state=NORMAL)


# level _1 try again -------------------------------------------------------
def try_again1_2():

    global buttons
    global picture
    global score
    global sc_l
    global start_t
    global remaining
    global lab_l
    global count_l
    global count
    global w_label
    global b_try
    global w_frame
    global button_e
    global b_pre
    global buttons2
    global count_00
    global count_01
    global count_02
    global count_03
    global count_10
    global count_11
    global count_12
    global count_13
    global count_20
    global count_21
    global count_22
    global count_23

    for row in range(3):
        for column in range(4):
            buttons2[row][column].destroy()

    w_frame.destroy()
    w_label.destroy()
    button_e.destroy()
    b_try.destroy()
    b_pre.destroy()


    picture = 0
    score = 0
    start_t = 0
    remaining = 0
    count = 0
    count_l = Label(root)
    count_00 = 0
    count_01 = 0
    count_02 = 0
    count_03 = 0
    count_10 = 0
    count_11 = 0
    count_12 = 0
    count_13 = 0
    count_20 = 0
    count_21 = 0
    count_22 = 0
    count_23 = 0

    sc_l["text"] = score
    picture_list()
    create_buttons()
    start_time()
    countdown(60)
    lab_l.config(image=level1)

    for row in buttons:
        for button in row:
            button.config(state=NORMAL)


# create buttons for level 1 -------------------------------------------------------
def create_buttons():
    global buttons

    buttons = [[Button(root, image=backB,
                       command=lambda row=row, column=column: choose_tiles(row, column))
                for column in range(4)]
               for row in range(3)]

    for row in range(3):
        for column in range(4):
            buttons[row][column].grid(row=row, column=column, padx=8, pady=8)



# pictures list for level 1 --------------------------------------------------------
def picture_list():

    global picture

    picture = [im1, im1, im1, im1, im2, im2, im2, im2, im3, im3, im3, im3]

    random.shuffle(picture)

    picture = [picture[:4],
               picture[4:8],
               picture[8:12]]



# selecting the tiles and matching function -------------------------------------------
def choose_tiles(row, column):
    global picture
    global sc_l
    global start_t
    global first
    global score
    global remaining
    global count
    global buttons
    global count_00

    buttons[row][column].config(image=picture[row][column])
    buttons[row][column].config(state=DISABLED)

    if not first:
        first = (row, column)
        tile_count(row,column)
    else:
        a, b = first
        if picture[row][column] == picture[a][b]:
            score += 20
            sc_l["text"] = score
            root.after(800, match_tiles_1, row, column, a, b)
            picture[row][column] = ''
            picture[a][b] = ''
            if not any(picture[0]):
                if not any(picture[1]):
                    if not any(picture[2]):
                        end = time.time()
                        duration = int(end - start_t)
                        remaining = 60-duration
                        total_score = remaining+score
                        win_frame(total_score)
        else:
            root.after(1000, hide_tiles, row, column, a, b)
            if count > 2:
                minus_score(a, b)

            count += 1
        first = None


# darking the tile if  matched_level_1-----------------------------------------------
def match_tiles_1(row, column, a, b):
    global buttons

    buttons[row][column].config(image=dark)
    buttons[a][b].config(image=dark)



#hiding the tile if not matched_level_1-------------------------------------------
def hide_tiles(row, column, a, b):
    global buttons

    buttons[row][column].config(image=backB, state=NORMAL)
    buttons[a][b].config(image=backB, state=NORMAL)


# counting the click of the buttons-----------------------------------------------------------
def tile_count(row, column):
    global count_00
    global count_01
    global count_02
    global count_03
    global count_10
    global count_11
    global count_12
    global count_13
    global count_20
    global count_21
    global count_22
    global count_23

    if row == 0 and column == 0:
         count_00 += 1
    elif row == 0 and column == 1:
         count_01 += 1
    elif row == 0 and column == 2:
         count_02 += 1
    elif row == 0 and column == 3:
         count_03 += 1
    elif row == 1 and column == 0:
         count_10 += 1
    elif row == 1 and column == 1:
         count_11 += 1
    elif row == 1 and column == 2:
        count_12 += 1
    elif row == 1 and column == 3:
        count_13 += 1
    elif row == 2 and column == 0:
        count_20 += 1
    elif row == 2 and column == 1:
        count_21 += 1
    elif row == 2 and column == 2:
        count_22 += 1
    elif row == 2 and column == 3:
        count_23 += 1


# minus score by click count------------------------------------------------------
def minus_score(a,b):

    global score
    global count_00
    global count_01
    global count_02
    global count_03
    global count_10
    global count_11
    global count_12
    global count_13
    global count_20
    global count_21
    global count_22
    global count_23
    global sc_l

    if a == 0 and b == 0:
         s = count_00 * 5
         score -= s
         sc_l["text"] = score
    elif a == 0 and b == 1:
         s = count_01 * 5
         score -= s
         sc_l["text"] = score
    elif a == 0 and b == 2:
         s = count_02 * 5
         score -= s
         sc_l["text"] = score
    elif a == 0 and b == 3:
         s = count_03 * 5
         score -= s
         sc_l["text"] = score
    elif a == 1 and b == 0:
         s = count_10 * 5
         score -= s
         sc_l["text"] = score
    elif a == 1 and b == 1:
         s = count_11 * 5
         score -= s
         sc_l["text"] = score
    elif a == 1 and b == 2:
         s = count_12 * 5
         score -= s
         sc_l["text"] = score
    elif a == 1 and b == 3:
         s = count_13 * 5
         score -= s
         sc_l["text"] = score
    elif a == 2 and b == 0:
         s = count_20 * 5
         score -= s
         sc_l["text"] = score
    elif a == 2 and b == 1:
         s = count_21 * 5
         score -= s
         sc_l["text"] = score
    elif a == 2 and b == 2:
         s = count_22 * 5
         score -= s
         sc_l["text"] = score
    elif a == 2 and b == 3:
         s = count_23 * 5
         score -= s
         sc_l["text"] = score


# start time-----------------------------------------------------------------------
def start_time():
    global start_t
    start_t = time.time()


# creating the lable for score and level-------------------------------------------
def create_score_level():
    global sc_l
    global label_s
    global lab_l
    global label_L

    label_s = Label(root, image=so_im, bg="#000000", fg="#000000")
    label_s.grid(column=0, row=3, padx=5, pady=10)

    sc_l = ttk.Label(root, width=3)
    sc_l.grid(row=3,column=1)

    lab_l = Label(root)
    lab_l.grid(column=3, row=3)

    label_L = Label(root, image=le_im, bg="#000000", fg="#000000")
    label_L.grid(column=2, row=3, padx=5, pady=10)

    rules_b = Button(root,image=rules,command=rules_f)
    rules_b.grid(row=4, column=0)



# win and loss label for level_1-----------------------------------------------------
def  win_frame(total_score):

    global b_next
    global w_label
    global button_e
    global w_frame
    global b_try
    global remaining

    w_frame = Frame(root,height=300, width=300)
    w_frame.grid(row=0, column=0, rowspan=2, columnspan=4, pady=30)

    if total_score >= 50:

        w_label = Label(w_frame, text="YOU WON! \nTotal Score is {} \n({} Bonus)".format(total_score, remaining),
                        bg="#2e8b57", fg="#ffffff", font=("American Typewriter", 35))
        w_label.pack()
        b_next = Button(root,image=nextl,command=level_2)
        b_next.grid(row=1, column=1, rowspan=2, columnspan=2)
        button_e = Button(root, image=ex, command=exit)
        button_e.grid(row=4, column=3)

    else:
        b_try = Button(root,image=again,command=try_again1)
        b_try.grid(row=1, column=1, rowspan=2, columnspan=2)

        button_e = Button(root,image=ex,command=exit)
        button_e.grid(row=4, column=3)

        w_label = Label(w_frame, text="YOU LOST! \nTotal Score is {} \n({} Bonus)".format(total_score, remaining),
                        bg="#2e8b57", fg="#ffffff", font=("American Typewriter", 35))
        w_label.pack()


# exit function-----------------------------------------------------------------------
def exit():
    global root
    root.quit()


# countdown for level_1----------------------------------------------------------------
def countdown(count_t):
    global remaining
    global count_l
    global b_try
    global w_frame
    global button_e
    global w_label
    global buttons

    count_l = ttk.Label(root, width=2)
    count_l.grid(row=0, column=6)
    count_l['text'] = count_t


    if count_t > remaining:
        root.after(1000,countdown, count_t - 1)

    if count_t == 0:
        for row in buttons:
            for button in row:
                button.config(state=DISABLED)
        w_frame = Frame(root, height=300, width=300)
        w_frame.grid(row=0, column=0, rowspan=2, columnspan=4, pady=30)
        b_try = Button(root, image=again,command=try_again1)
        b_try.grid(row=1, column=1, rowspan=2, columnspan=2)

        button_e = Button(root, image=ex, command=exit)
        button_e.grid(row=4, column=3)

        w_label = Label(w_frame, text="YOU LOST! \nOUT OF TIME \nTRY AGAIN",
                        bg="#2e8b57", fg="#ffffff", font=("American Typewriter", 35))
        w_label.pack()



# level_2 ----------------------------------------------------------------------------
def level_2():

    global buttons
    global sc_l
    global count_l
    global w_label
    global b_try
    global w_frame
    global button_e
    global b_next
    global picture2
    global score

    w_frame.destroy()
    w_label.destroy()
    button_e.destroy()
    b_next.destroy()
    b_try.destroy()

    for row in range(3):
        for column in range(4):
            buttons[row][column].destroy()


    count_l = Label(root)
    score = 0
    countdown3(8)

    picture_list2()
    create_buttons2()
    buttons2[0][0].config(image=picture2[0][0])
    buttons2[0][1].config(image=picture2[0][1])
    buttons2[0][2].config(image=picture2[0][2])
    buttons2[0][3].config(image=picture2[0][3])
    buttons2[1][0].config(image=picture2[1][0])
    buttons2[1][1].config(image=picture2[1][1])
    buttons2[1][2].config(image=picture2[1][2])
    buttons2[1][3].config(image=picture2[1][3])
    buttons2[2][0].config(image=picture2[2][0])
    buttons2[2][1].config(image=picture2[2][1])
    buttons2[2][2].config(image=picture2[2][2])
    buttons2[2][3].config(image=picture2[2][3])

    for row in buttons2:
        for button in row:
            button.config(state=DISABLED)
    sc_l["text"] = score
    lab_l.config(image=level2)


# level2_2---------------------------------------------------------------------------
def level_2_2():
    global buttons2
    global sc_l
    global count_l
    global w_label
    global b_try
    global w_frame
    global button_e
    global b_next
    global picture2
    global score

    w_frame.destroy()
    w_label.destroy()
    button_e.destroy()
    b_next.destroy()
    b_try.destroy()

    for row in range(3):
        for column in range(4):
            buttons2[row][column].destroy()


    count_l = Label(root)
    score = 0
    countdown3(8)

    picture_list2()
    create_buttons2()
    buttons2[0][0].config(image=picture2[0][0])
    buttons2[0][1].config(image=picture2[0][1])
    buttons2[0][2].config(image=picture2[0][2])
    buttons2[0][3].config(image=picture2[0][3])
    buttons2[1][0].config(image=picture2[1][0])
    buttons2[1][1].config(image=picture2[1][1])
    buttons2[1][2].config(image=picture2[1][2])
    buttons2[1][3].config(image=picture2[1][3])
    buttons2[2][0].config(image=picture2[2][0])
    buttons2[2][1].config(image=picture2[2][1])
    buttons2[2][2].config(image=picture2[2][2])
    buttons2[2][3].config(image=picture2[2][3])

    for row in buttons2:
        for button in row:
            button.config(state=DISABLED)
    sc_l["text"] = score
    lab_l.config(image=level2)


# countdown for 8 sec----------------------------------------------------------
def countdown3(count_t):

    global remaining
    global count_l
    global b_try
    global w_frame
    global button_e
    global w_label
    global buttons2
    global start_t
    global count
    global count_00
    global count_01
    global count_02
    global count_03
    global count_10
    global count_11
    global count_12
    global count_13
    global count_20
    global count_21
    global count_22
    global count_23


    count_l = ttk.Label(root, width=2)
    count_l.grid(row=0, column=6)
    count_l['text'] = count_t

    if count_t > 0:
        root.after(1000, countdown3, count_t - 1)

    if count_t == 0:
        start_t = 0
        remaining = 0
        count_l = Label(root)
        count_00 = 0
        count_01 = 0
        count_02 = 0
        count_03 = 0
        count_10 = 0
        count_11 = 0
        count_12 = 0
        count_13 = 0
        count_20 = 0
        count_21 = 0
        count_22 = 0
        count_23 = 0

        for row in range(3):
            for column in range(4):
                buttons2[row][column].destroy()

        create_buttons2()
        countdown2(60)
        start_time()


# picture list for level_2----------------------------------------------------------
def picture_list2():
    global picture2

    picture2 = [im4, im4, im4, im4, im5, im5, im5, im5, im6, im6, im6, im6]

    random.shuffle(picture2)

    picture2 = [picture2[:4],
               picture2[4:8],
               picture2[8:12]]



# creating buttons for level_2--------------------------------------------------------
def create_buttons2():
    global buttons2

    buttons2 = [[Button(root, image=backB,
                       command=lambda row=row, column=column: choose_tiles2(row, column))
                for column in range(4)]
               for row in range(3)]

    for row in range(3):
        for column in range(4):
            buttons2[row][column].grid(row=row, column=column, padx=8, pady=8)



# selectng the tiles and matching function -------------------------------------------
def choose_tiles2(row, column):

    global picture2
    global sc_l
    global start_t
    global first
    global score
    global remaining
    global count
    global buttons2
    global count_00

    buttons2[row][column].config(image=picture2[row][column])
    buttons2[row][column].config(state=DISABLED)
    if not first:
        first = (row, column)
        tile_count(row,column)
    else:
        a, b = first
        if picture2[row][column] == picture2[a][b]:
            score += 20
            sc_l["text"] = score
            picture2[row][column] = ''
            picture2[a][b] = ''
            root.after(800, match_tiles_2, row, column, a, b)
            if not any(picture2[0]):
                if not any(picture2[1]):
                    if not any(picture2[2]):
                        end = time.time()
                        duration = end - start_t
                        remaining = int(60-duration)
                        total_score = remaining + score
                        win_frame2(total_score)
        else:
            root.after(1000, hide_tiles2, row, column, a, b)
            minus_score(a,b)
        first = None

# darking the tile if  matched_level_2-----------------------------------------------
def match_tiles_2(row, column, a, b):
    global buttons2

    buttons2[row][column].config(image=dark)
    buttons2[a][b].config(image=dark)



# hiding the tile if not matched_level_2-----------------------------------------------
def hide_tiles2(row, column, a, b):
    global buttons2

    buttons2[row][column].config(image=backB, state=NORMAL)
    buttons2[a][b].config(image=backB, state=NORMAL)



# win and loss label for level_2-----------------------------------------------------
def win_frame2(total_score):

    global w_label
    global b_next
    global button_e
    global w_frame
    global b_try
    global b_pre
    global remaining


    w_frame = Frame(root, height=300, width=300)
    w_frame.grid(row=0, column=0, rowspan=2, columnspan=4, pady=30)

    if total_score >= 100:

        w_label = Label(w_frame, text="YOU WON! \nTotal Score is {} \n({} Bonus)".format(total_score, remaining),
                        bg="#2e8b57", fg="#ffffff", font=("American Typewriter", 35))
        w_label.pack()
        button_e = Button(root, image=ex,command=exit)
        button_e.grid(row=4, column=3)
        b_pre = Button(root, image=b_p,command=try_again1_2)
        b_pre.grid(row=1, column=1, rowspan=2, columnspan=2)

    else:
        b_try = Button(root, image=again,command=level_2_2)
        b_try.grid(row=1, column=1, rowspan=2, columnspan=2)
        button_e = Button(root, image=ex, command=exit)
        button_e.grid(row=4, column=3)
        w_label = Label(w_frame, text="YOU LOST! \nTotal Score is {} \n({} Bonus)".format(total_score, remaining),
                        bg="#2e8b57", fg="#ffffff", font=("American Typewriter", 35))
        w_label.pack()



# countdown for level_2----------------------------------------------------------------
def countdown2(count_t):

    global remaining
    global count_l
    global b_try
    global w_frame
    global button_e
    global w_label
    global buttons2

    count_l = ttk.Label(root, width=2)
    count_l.grid(row=0, column=6)
    count_l['text'] = count_t

    if count_t > remaining:
        root.after(1000, countdown2, count_t - 1)

    if count_t == 0:
        for row in buttons2:
            for button in row:
                button.config(state=DISABLED)
        w_frame = Frame(root, height=300, width=300)
        w_frame.grid(row=0, column=0, rowspan=2, columnspan=4, pady=30)
        b_try = Button(root, image=again, command=level_2_2)
        b_try.grid(row=1, column=1, rowspan=2, columnspan=2)

        button_e = Button(root, image=ex, command=exit)
        button_e.grid(row=4, column=3)

        w_label = Label(w_frame, text="YOU LOST! \nOUT OF TIME \nTRY AGAIN",
                        bg="#2e8b57", fg="#ffffff", font=("American Typewriter", 35))
        w_label.pack()


# new window for rules--------------------------------------------------------------------
def rules_f():

    rule_root = Tk()
    rule_root.title("ABC Pairs Game Rules")
    rule_root.resizable(0, 0)
    rule_root.geometry("500x450")
    rule_root.configure(bg="#2e8b57")
    rule_l = Label(rule_root,height=100,width=100,text="\nLevel 1 - You will have 60 seconds \nto match 6 pairs and 3 different \npictures - Score Max 50 "
                                                       "\n\nLevel 2 - Grid will be revealed initially \nfor 8 seconds and then you "
                                                       "\nwill have 60 seconds to match 6 \npairs and 3 different  \npictures - Score Max 100",
                                                        bg="#2e8b57",
                                                        fg="#ffffff",
                                                       font=("American Typewriter", 26))
    rule_l.pack()
    rule_root.mainloop()


root.mainloop()