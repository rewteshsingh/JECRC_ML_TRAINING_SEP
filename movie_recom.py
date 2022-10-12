import tkinter as ttk
from click import command
from numpy import imag
import pandas as pd
import warnings
from pytest import Item

from tables import Cols
warnings.filterwarnings('ignore')
import os
print('Location is:',os.getcwd(), '\n\n\n')



app = ttk.Tk()
app.title('RECOMMENDATION SYSTEM.BASEapk')
app.geometry('600x600')

Cols=['user_id','movie_id','rating','ts']
df=pd.read_csv('u.data',sep='\t',names=Cols).drop('ts',axis=1)
item_cols = ['movie_id','title']+ [str(i) for i in range(22)]
df1=pd.read_csv('u.item',sep='|',names= item_cols,encoding="ISO-8859-1")[['movie_id','title']]
movie = pd.merge(df,df1,on = 'movie_id')

result =  ttk.Variable(app)


frame = ttk.Frame(app)
frame.place(x=10,y=10)


box = ttk.Listbox(frame,height=10,width=50)
for title in movie['title'].unique():
   
    box.insert(ttk.END, title)
#box.grid(row = 0, column=0)  
box.pack(side='left',fill='y')
  
#box.place(x=10,y=10) 

scroll = ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(command=box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right',fill='y')


def get_movie():
    movie_selected = box.get(box.curselection())
    print('movie_selected:',movie_selected)

    # Create Pivot Table 
    movie_pivot = movie.pivot_table(index= 'user_id',columns= 'title',values = 'rating')               
                    
     # Find Similarity For Selected Movie 
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df = pd.DataFrame(corrs, columns = ['Correlation'])
    corrs_df['rating'] = movie.groupby('title')['rating'].mean()
    corrs_df['count'] = movie['title'].value_counts()               
                    
     # Find Top 2-3 Recommendations 
    top_recom = list(corrs_df[corrs_df['count']>50].sort_values(
         by='Correlation',ascending=False).head(3).index)

         #important
    if movie_selected in top_recom:
            top_recom.remove(movie_selected)
            print('Recommendation:',top_recom)

            if top_recom:
                result.set(top_recom[0])
            else:
                result.set('sorry no recommendation found!!')    

ttk.Button(app,text='FIND RECOMMENDATION ',font=('Arial',10),command=get_movie).place(x=15,y=190)
ttk.Label(app,textvariable=result,font=('Arial',13)).place(x=20,y=230)




app.mainloop()