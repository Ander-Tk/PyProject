from tkinter import *
import calendar
import time

t = time.localtime()
yearInt = t.tm_year #Ou usar: yearInt = t.[0] 

cal = calendar.calendar(yearInt)
root = Tk()
#root.geometry('545x595') - Tamanho inicial
root.minsize(width=545, height=595) #Tamanho mínimo
root.maxsize(width=545, height=595) #Tamanho máximo
root.title('Calendário')
root.config(bg='#94918a')

aYear = Label(root, text=yearInt, bg='#4a4947', fg='white', font=('Courier', 35) )
aYear.grid(row=1, column=1, ipadx=215)

labelCal = Label(root, text=cal, padx=20, font=('Courier New', 8), justify=LEFT)
labelCal.grid(row=2, column=1)

root.mainloop()
