import tkinter as ttk
app = ttk.Tk()
app.title('CALCULATOR')
app.geometry('600x400')
ttk.Label(app, text= 'Developed by : Rewtesh Singh').place(x=100,y=100)




f1 = ttk.Variable(app)
f1.set(' ')
f2 = ttk.Variable(app)
f2.set(' ')
result = ttk.Variable(app)
ttk.Entry(app, textvariable=f1, font= ('Arial',22)).place(x=100,y=150)
ttk.Entry(app, textvariable=f2, font=('Arial',22)).place(x=100,y=200)
ttk.Label(app, text='RESULT :').place(x=110,y=250)
ttk.Label(app, textvariable=result,font=('Arial',22)).place(x=100,y=300)
def calc1(op):
    print('I will calculate')
    result.set(eval(f1.get()+op+f2.get()))



ttk.Button(app, text='+', command=lambda:calc1('+'), font = ('Arial',22)).place(x=100,y=360)
ttk.Button(app, text='-', command=lambda:calc1('-'), font=('Arial',22)).place(x=200,y=360)
ttk.Button(app, text='*', command=lambda:calc1('*'), font= ('Arial',22)).place(x=300,y=360)
ttk.Button(app, text='/', command=lambda:calc1('/'), font=('Arial',22)).place(x=400,y=360) 




app.mainloop()