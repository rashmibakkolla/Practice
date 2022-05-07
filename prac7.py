from tkinter import *
import tkinter as tk
from tkinter import ttk
root= tk.Tk()
root.title=("Experiment 7")
main= ttk.Frame(root)
main.pack(side="left",fill='both', expand=True)

tk.Button(main,text='').pack(side='top',fill='both',expand=True)
R1=ttk.Radiobutton(main,text='one').pack(side='left')
R2=ttk.Radiobutton(main,text='Two').pack(side='left')
R3=ttk.Radiobutton(main,text='Three').pack(side='left')

name=tk.StringVar()
name_label=ttk.Label(root,text='name:').pack(side='top',pady=(0,10))
entry=ttk.Entry(root,width=25,textvariable=name).pack(side='top')

okay_btn=ttk.Button(root,text="Okay").pack(side='left',padx=(0,10),pady=(10,0))
cancel_btn=ttk.Button(root,text="Cancel").pack(side='left',padx=(4,10),pady=(10,0))
root.mainloop()
