import tkinter as ttk

from sympy import im
import pandas as pd
import warnings
warnings.filterwarnings

app= ttk.Tk()
app.title('Recommendation System')
app.geometry('400x400')

result = ttk.Variable(app)
box = ttk.Listbox(app,height=10)
box.place(x=10,y=10)

def get_movie():
    pass

ttk.Button(app,text='Find recommendations',font=('Arial',22),command = get_movie).place(x=220,y=50)
ttk.Label(app,textvariable=result,font=('Arial',22)).place(x=200,y=100)

app.mainloop()