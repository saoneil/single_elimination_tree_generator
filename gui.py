import pandas as pd
import tkinter as tk
from tkinter import ttk
import os
from division_list import get_division_list
from tkinter import messagebox


root = tk.Tk()
root.title("Division Tree")


def confirm_division_selection():
    cur_selection = file_selection.get()
    n, round_total, division_list, complete_tree_list, next_round_list, file = get_division_list(cur_selection)
    print(n)
    print(round_total)
    print(division_list)
    print(complete_tree_list)
    print(next_round_list)
    print(file)
    tabControl.select(tab1)
    




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
pattern = "Optional Pattern"

red_cur_name = tk.StringVar()
red_cur_club = tk.StringVar()
blue_cur_name = tk.StringVar()
blue_cur_club = tk.StringVar()

red_od1_name = tk.StringVar()
red_od1_club = tk.StringVar()
blue_od1_name = tk.StringVar()
blue_od1_club = tk.StringVar()
red_od2_name = tk.StringVar()
red_od2_club = tk.StringVar()
blue_od2_name = tk.StringVar()
blue_od2_club = tk.StringVar()
red_od3_name = tk.StringVar()
red_od3_club = tk.StringVar()
blue_od3_name = tk.StringVar()
blue_od3_club = tk.StringVar()

pattern_randomize = tk.Button(root, text="Generate Pattern")
red_winner = tk.Button(root, text="Red Winner")
blue_winner = tk.Button(root, text="Blue Winner")
advance_tree = tk.Button(root, text="Advance Tree")





C = tk.Canvas(tab1, bg="blue", height=250, width=300)
filename = tk.PhotoImage(file = "C:\\Users\\saone\\Documents\\Python Stuff\\prod\\single_elimination_tree_generator\\bg_image2.png")
background_label = tk.Label(tab1, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


root.configure(background='black')
root.minsize(width=1440, height=720)
root.mainloop()