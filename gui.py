import pandas as pd
import tkinter as tk
from tkinter import ttk
import os
from division_list import get_division_list
from tkinter import messagebox

# https://www.youtube.com/watch?v=WurCpmHtQc4

root = tk.Tk()
root.title("Division Tree")

# round specific variables
winner = 2 # 0 = red, 1 = blue
ins_cnt_2 = 0
ins_cnt_4 = 0
ins_cnt_8 = 0
ins_cnt_16 = 0
ins_cnt_32 = 0
round_counter = 0

# total_list
total_list = []
# some global variables
n = 0
round_total = 0
division_list = []
complete_tree_list = []
next_round_list = []
file = ""

def random_pattern():
    print("random pattern")
def red_winner():
    global winner
    global ins_cnt_2, ins_cnt_4, ins_cnt_8, ins_cnt_16, ins_cnt_32
    winner = 0
    if n == 2:
        total_list[2] = [total_list[ins_cnt_2][0], total_list[ins_cnt_2][1]]
        print(ins_cnt_4)
        print(total_list)
        ins_cnt_2 += 2
    elif n == 4:
        total_list[n+ins_cnt_4] = [total_list[ins_cnt_4][0], total_list[ins_cnt_4][1]]
        print(ins_cnt_4)
        print(total_list)
        ins_cnt_4 += 2
def blue_winner():
    global winner
    global ins_cnt_2, ins_cnt_4, ins_cnt_8, ins_cnt_16, ins_cnt_32
    winner = 1
    if n == 2:
        total_list[2] = [total_list[ins_cnt_2+1][0], total_list[ins_cnt_2+1][1]]
        print(ins_cnt_4)
        print(total_list)
        ins_cnt_2 += 2
    elif n == 4:
        total_list[n+ins_cnt_4] = [total_list[ins_cnt_4+1][0], total_list[ins_cnt_4+1][1]]
        print(ins_cnt_4)
        print(total_list)
        ins_cnt_4 += 2
def confirm_division_selection():
    global n, round_total, division_list, complete_tree_list, next_round_list, file
    global total_list, round_counter
    global ins_cnt_2, ins_cnt_4, ins_cnt_8, ins_cnt_16, ins_cnt_32
    
    # reset previous variables
    ins_cnt_2 = 0
    ins_cnt_4 = 0
    ins_cnt_8 = 0
    ins_cnt_16 = 0
    ins_cnt_32 = 0
    round_counter = 0
    total_list = []
    n = 0
    round_total = 0
    division_list = []
    complete_tree_list = []
    next_round_list = []
    file = ""
    
    cur_selection = file_selection.get()
    n, round_total, division_list, complete_tree_list, next_round_list, file = get_division_list(cur_selection)
    
    if n == 2:
        for i in range(n):
            total_list.append(complete_tree_list[0][i])
        for i in range(int(n/2)):
            total_list.append(complete_tree_list[1][i])
    elif n == 4:
        for i in range(n):
            total_list.append(complete_tree_list[0][i])
        for i in range(int(n/2)):
            total_list.append(complete_tree_list[1][i])
        for i in range(int(n/4)):
            total_list.append(complete_tree_list[2][i])
    elif n == 8:
        for i in range(n):
            total_list.append(complete_tree_list[0][i])
        for i in range(int(n/2)):
            total_list.append(complete_tree_list[1][i])
        for i in range(int(n/4)):
            total_list.append(complete_tree_list[2][i])
        for i in range(int(n/8)):
            total_list.append(complete_tree_list[3][i])
    elif n == 16:
        for i in range(n):
            total_list.append(complete_tree_list[0][i])
        for i in range(int(n/2)):
            total_list.append(complete_tree_list[1][i])
        for i in range(int(n/4)):
            total_list.append(complete_tree_list[2][i])
        for i in range(int(n/8)):
            total_list.append(complete_tree_list[3][i])
        for i in range(int(n/16)):
            total_list.append(complete_tree_list[4][i])
    elif n == 32:
        for i in range(n):
            total_list.append(complete_tree_list[0][i])
        for i in range(int(n/2)):
            total_list.append(complete_tree_list[1][i])
        for i in range(int(n/4)):
            total_list.append(complete_tree_list[2][i])
        for i in range(int(n/8)):
            total_list.append(complete_tree_list[3][i])
        for i in range(int(n/16)):
            total_list.append(complete_tree_list[4][i])
        for i in range(int(n/32)):
            total_list.append(complete_tree_list[5][i])
    
    dot_index = file.index('.')
    file_name_adj = file[0:dot_index]
    title.set(file_name_adj)
    
    print(total_list)
    
    red_cur_name.set("")
    red_cur_club.set("")
    blue_cur_name.set("")
    blue_cur_club.set("")
    red_od1_name.set("")
    red_od1_club.set("")
    blue_od1_name.set("")
    blue_od1_club.set("")
    red_od2_name.set("")
    red_od2_club.set("")
    blue_od2_name.set("")
    blue_od2_club.set("")
    red_od3_name.set("")
    red_od3_club.set("")
    blue_od3_name.set("")
    blue_od3_club.set("")
    
    tabControl.select(tab1)    
def advance_tree():
    global ins_cnt_2, ins_cnt_4, ins_cnt_8, ins_cnt_16, ins_cnt_32
    global winner
    if n == 2:
        if ins_cnt_2 != n:
            red_cur_name.set(total_list[ins_cnt_2][0])
            red_cur_club.set(total_list[ins_cnt_2][1])
            blue_cur_name.set(total_list[ins_cnt_2+1][0])
            blue_cur_club.set(total_list[ins_cnt_2+1][1])
        elif ins_cnt_2 == n:
            if winner == 0:
                blue_cur_name.set("Winner")
                blue_cur_club.set("<-------")
                red_cur_name.set(total_list[2][0])
                red_cur_club.set(total_list[2][1])
            elif winner == 1:
                red_cur_name.set("Winner")
                red_cur_club.set("------->")
                blue_cur_name.set(total_list[2][0])
                blue_cur_club.set(total_list[2][1])
    elif (n == 4 and ins_cnt_4 != n):
        red_cur_name.set(total_list[ins_cnt_4][0])
        red_cur_club.set(total_list[ins_cnt_4][1])
        blue_cur_name.set(total_list[ins_cnt_4+1][0])
        blue_cur_club.set(total_list[ins_cnt_4+1][1])
        
        red_od1_name.set(total_list[ins_cnt_4+2][0])
        red_od1_club.set(total_list[ins_cnt_4+2][1])
        blue_od1_name.set(total_list[ins_cnt_4+3][0])
        blue_od1_club.set(total_list[ins_cnt_4+3][1])
    elif n == 8:
        red_cur_name.set(total_list[ins_cnt_8][0])
        red_cur_club.set(total_list[ins_cnt_8][1])
        blue_cur_name.set(total_list[ins_cnt_8+1][0])
        blue_cur_club.set(total_list[ins_cnt_8+1][1])
        
        red_od1_name.set(total_list[ins_cnt_8+2][0])
        red_od1_club.set(total_list[ins_cnt_8+2][1])
        blue_od1_name.set(total_list[ins_cnt_8+3][0])
        blue_od1_club.set(total_list[ins_cnt_8+3][1])
        
        red_od2_name.set(total_list[ins_cnt_8+4][0])
        red_od2_club.set(total_list[ins_cnt_8+4][1])
        blue_od2_name.set(total_list[ins_cnt_8+5][0])
        blue_od2_club.set(total_list[ins_cnt_8+5][1])
        
        red_od3_name.set(total_list[ins_cnt_8+6][0])
        red_od3_club.set(total_list[ins_cnt_8+6][1])
        blue_od3_name.set(total_list[ins_cnt_8+7][0])
        blue_od3_club.set(total_list[ins_cnt_8+7][1])
    elif n == 16:
        red_cur_name.set(total_list[ins_cnt_16][0])
        red_cur_club.set(total_list[ins_cnt_16][1])
        blue_cur_name.set(total_list[ins_cnt_16+1][0])
        blue_cur_club.set(total_list[ins_cnt_16+1][1])
        
        red_od1_name.set(total_list[ins_cnt_16+2][0])
        red_od1_club.set(total_list[ins_cnt_16+2][1])
        blue_od1_name.set(total_list[ins_cnt_16+3][0])
        blue_od1_club.set(total_list[ins_cnt_16+3][1])
        
        red_od2_name.set(total_list[ins_cnt_16+4][0])
        red_od2_club.set(total_list[ins_cnt_16+4][1])
        blue_od2_name.set(total_list[ins_cnt_16+5][0])
        blue_od2_club.set(total_list[ins_cnt_16+5][1])
        
        red_od3_name.set(total_list[ins_cnt_16+6][0])
        red_od3_club.set(total_list[ins_cnt_16+6][1])
        blue_od3_name.set(total_list[ins_cnt_16+7][0])
        blue_od3_club.set(total_list[ins_cnt_16+7][1])
    elif n == 32:
        red_cur_name.set(total_list[ins_cnt_32][0])
        red_cur_club.set(total_list[ins_cnt_32][1])
        blue_cur_name.set(total_list[ins_cnt_32+1][0])
        blue_cur_club.set(total_list[ins_cnt_32+1][1])
        
        red_od1_name.set(total_list[ins_cnt_32+2][0])
        red_od1_club.set(total_list[ins_cnt_32+2][1])
        blue_od1_name.set(total_list[ins_cnt_32+3][0])
        blue_od1_club.set(total_list[ins_cnt_32+3][1])
        
        red_od2_name.set(total_list[ins_cnt_32+4][0])
        red_od2_club.set(total_list[ins_cnt_32+4][1])
        blue_od2_name.set(total_list[ins_cnt_32+5][0])
        blue_od2_club.set(total_list[ins_cnt_32+5][1])
        
        red_od3_name.set(total_list[ins_cnt_32+6][0])
        red_od3_club.set(total_list[ins_cnt_32+6][1])
        blue_od3_name.set(total_list[ins_cnt_32+7][0])
        blue_od3_club.set(total_list[ins_cnt_32+7][1])
    winner = 2
##
# CREATING TWO TABS
##
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.rowconfigure(root, 0, weight=1)
tabControl.add(tab1, text ='Division Tree')
tabControl.add(tab2, text ='Select Divison')
tabControl.grid(row=0, column=0, sticky='nsew')
tab1.columnconfigure( (0,1), weight=1)
tab1.rowconfigure((0,1), weight=1)


##
# SETTING UP BACKGROUND RED/BLUE
##
bg = tk.PhotoImage(file="bg_image.png")
main_title = tk.Label(tab1, image=bg)
main_title.place(x=0, y=0, relwidth=1, relheight=1)

##
# TAB2 - CONTROL
##
file_list = os.listdir(r'C:\Users\saone\Documents\Python Stuff\prod\single_elimination_tree_generator\raw_divisions')
    
desc = ttk.Label(tab2, text = "Select Division From Dropdown:")
desc.pack()
dropdown_options = file_list
file_selection = tk.StringVar(tab2)
dropdown = tk.OptionMenu(tab2, file_selection, *dropdown_options)
dropdown.pack()

confirm = tk.Button(tab2, text="Confirm Selection", command=confirm_division_selection)
confirm.pack()


##
## TAB 1, advance tree
##
title = tk.StringVar()
title.set("Division: <Name>")
title_label = tk.Label(tab1, textvariable=title, font="Verdana 45 bold", bg='black', fg='white')
title_label.place(relx=0.5, rely=0.05, anchor='n')

pattern = tk.StringVar()
pattern.set("OPTIONAL PATTERN")
pattern_label = tk.Label(tab1, textvariable = pattern, bg='black', fg='white', font='Verdana 25 bold')
pattern_label.place(relx=0.5, rely=0.52, anchor='n')

pattern_randomize = tk.Button(tab1, text="Generate Pattern", bg='black', fg='yellow', font='Verdana 10 bold', command = random_pattern)
# pattern_randomize.place(relx=0.5, rely=0.48, anchor='n')
# only intialize for black belt divisions

on_deck = tk.StringVar()
on_deck.set("              On Deck              ")
on_deck_label = tk.Label(tab1, textvariable = on_deck, bg='black', fg='white', font='Verdana 30 bold')
on_deck_label.place(relx=0.5, rely=0.65, anchor='n')

red_winner = tk.Button(tab1, text="\n \n  Red Winner \n \n", bg='black', fg='red', font='Verdana 10 bold', command = red_winner)
red_winner.place(relx=0.05, rely=0.85, anchor='n')
blue_winner = tk.Button(tab1, text="\n \n Blue Winner \n \n", bg='black', fg='dodgerblue', font='Verdana 10 bold', command = blue_winner)
blue_winner.place(relx=0.95, rely=0.85, anchor='n')

advance_tree = tk.Button(tab1, text="Advance Tree", bg='black', fg='yellow', font='Verdana 10 bold', command = advance_tree)
advance_tree.place(relx=0.5, rely=0, anchor='n')



red_cur_name = tk.StringVar()
red_cur_name.set("Red Competitior Name")
red_cur_name_label = tk.Label(tab1, textvariable=red_cur_name, bg='black', fg='white', font='Verdana 35 bold')
red_cur_name_label.place(relx=0.25, rely=0.23, anchor='n')
red_cur_club = tk.StringVar()
red_cur_club.set("Red Competitior Club")
red_cur_club_label = tk.Label(tab1, textvariable=red_cur_club, bg='black', fg='white', font='Verdana 20 bold')
red_cur_club_label.place(relx=0.25, rely=0.32, anchor='n')

blue_cur_name = tk.StringVar()
blue_cur_name.set("Blue Competitior Name")
blue_cur_name_label = tk.Label(tab1, textvariable=blue_cur_name, bg='black', fg='white', font='Verdana 35 bold')
blue_cur_name_label.place(relx=0.75, rely=0.23, anchor='n')
blue_cur_club = tk.StringVar()
blue_cur_club.set("Blue Competitior Club")
blue_cur_club_label = tk.Label(tab1, textvariable=blue_cur_club, bg='black', fg='white', font='Verdana 20 bold')
blue_cur_club_label.place(relx=0.75, rely=0.32, anchor='n')

red_od1_name = tk.StringVar()
red_od1_name.set("Red On Deck 1 Name")
red_od1_name_label = tk.Label(tab1, textvariable=red_od1_name, bg='black', fg='white', font='Verdana 12 bold')
red_od1_name_label.place(relx=0.40, rely=0.75, anchor='n')
red_od1_club = tk.StringVar()
red_od1_club.set("Red On Deck 1 Club")
red_od1_club_label = tk.Label(tab1, textvariable=red_od1_club, bg='black', fg='white', font='Verdana 6 bold')
red_od1_club_label.place(relx=0.40, rely=0.78, anchor='n')

blue_od1_name = tk.StringVar()
blue_od1_name.set("Blue On Deck 1 Name")
blue_od1_name_label = tk.Label(tab1, textvariable=blue_od1_name, bg='black', fg='white', font='Verdana 12 bold')
blue_od1_name_label.place(relx=0.60, rely=0.75, anchor='n')
blue_od1_club = tk.StringVar()
blue_od1_club.set("Blue On Deck 1 Club")
blue_od1_club_label = tk.Label(tab1, textvariable=blue_od1_club, bg='black', fg='white', font='Verdana 6 bold')
blue_od1_club_label.place(relx=0.60, rely=0.78, anchor='n')

red_od2_name = tk.StringVar()
red_od2_name.set("Red On Deck 2 Name")
red_od2_name_label = tk.Label(tab1, textvariable=red_od2_name, bg='black', fg='white', font='Verdana 12 bold')
red_od2_name_label.place(relx=0.40, rely=0.85, anchor='n')
red_od2_club = tk.StringVar()
red_od2_club.set("Red On Deck 2 Name")
red_od2_club_label = tk.Label(tab1, textvariable=red_od2_club, bg='black', fg='white', font='Verdana 6 bold')
red_od2_club_label.place(relx=0.40, rely=0.88, anchor='n')

blue_od2_name = tk.StringVar()
blue_od2_name.set("Blue On Deck 2 Name")
blue_od2_name_label = tk.Label(tab1, textvariable=blue_od2_name, bg='black', fg='white', font='Verdana 12 bold')
blue_od2_name_label.place(relx=0.60, rely=0.85, anchor='n')
blue_od2_club = tk.StringVar()
blue_od2_club.set("Blue On Deck 2 Club")
blue_od2_club_label = tk.Label(tab1, textvariable=blue_od2_club, bg='black', fg='white', font='Verdana 6 bold')
blue_od2_club_label.place(relx=0.60, rely=0.88, anchor='n')

red_od3_name = tk.StringVar()
red_od3_name.set("Red On Deck 3 Name")
red_od3_name_label = tk.Label(tab1, textvariable=red_od3_name, bg='black', fg='white', font='Verdana 12 bold')
red_od3_name_label.place(relx=0.40, rely=0.95, anchor='n')
red_od3_club = tk.StringVar()
red_od3_club.set("Red On Deck 3 Club")
red_od3_club_label = tk.Label(tab1, textvariable=red_od3_club, bg='black', fg='white', font='Verdana 6 bold')
red_od3_club_label.place(relx=0.40, rely=0.98, anchor='n')

blue_od3_name = tk.StringVar()
blue_od3_name.set("Blue On Deck 3 Name")
blue_od3_name_label = tk.Label(tab1, textvariable=blue_od3_name, bg='black', fg='white', font='Verdana 12 bold')
blue_od3_name_label.place(relx=0.60, rely=0.95, anchor='n')
blue_od3_club = tk.StringVar()
blue_od3_club.set("Blue On Deck 3 Club")
blue_od3_club_label = tk.Label(tab1, textvariable=blue_od3_club, bg='black', fg='white', font='Verdana 6 bold')
blue_od3_club_label.place(relx=0.60, rely=0.98, anchor='n')




root.minsize(width=1440, height=720)
root.mainloop()