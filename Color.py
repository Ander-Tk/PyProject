from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('ChooseColors')
root.iconbitmap('RainbowPy.ico')
#root.geometry('454x480') - Tamanho inicial
root.minsize(width=454, height=480) #Tamanho mínimo
root.maxsize(width=454, height=480) #Tamanho máximo
def cor():
     global clr
     clr = colorchooser.askcolor(title='Selecionar Cor')
     root.configure(bg=clr[1])
     visor.delete(0, END)
     visor.insert(0, clr[1])

visor = Entry(root, width=30, borderwidth=6, font=('Courier', 15), justify='center')
visor.grid(row=0, column=0, columnspan=5, ipady=8, ipadx=40)
btn = Button(root, text="Alterar Cor", pady=10, font=('', 10), command=cor).grid(row=1, column=2, pady=20, ipadx = 50)

def savecolor(num):
     global clr
     if num == 1:
          btnSave1 = Button(root, pady=9, padx=8, bg=clr[1], text=clr[1], font=('', 8), command=lambda:savecolor(1)).grid(row=3, column=1, pady=20, ipadx=30)
     elif num == 2:
          btnSave2 = Button(root, pady=9, padx=8, bg=clr[1], text=clr[1], font=('', 8), command=lambda:savecolor(2)).grid(row=3, column=2, pady=20, ipadx=30)
     elif num == 3:          
          btnSave3 = Button(root, pady=9, padx=8, bg=clr[1], text=clr[1], font=('', 8), command=lambda:savecolor(3)).grid(row=3, column=3, pady=20, ipadx=30)

label = Label(root, text='SaveColor', justify='center', fg='white', bg='#4a4947', font=('Courier', 15), pady=20).grid(row=2, column=0, columnspan=5, ipadx=170, pady=(200, 0))
btnSave1 = Button(root, pady=8, padx=12, command=lambda:savecolor(1)).grid(row=3, column=1, pady=20, ipadx=30)
btnSave2 = Button(root, pady=8, padx=12, command=lambda:savecolor(2)).grid(row=3, column=2, pady=20, ipadx=30)
btnSave3 = Button(root, pady=8, padx=12, command=lambda:savecolor(3)).grid(row=3, column=3, pady=20, ipadx=30)



root.mainloop()
