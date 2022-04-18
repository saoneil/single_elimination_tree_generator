import pandas as pd
import tkinter as tk

root = tk.Tk()
root.title("Division Tree")





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






# root.minsize(width=720, height=360)
# root.mainloop()
