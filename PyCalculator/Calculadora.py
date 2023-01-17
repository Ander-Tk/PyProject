from tkinter import *

root = Tk()
root.title("Calculadora [By: AndersPotato]")
root.configure(bg="#4a4947") #[Define a cor de fundo]
#Tamanho min/max da janela
root.minsize(width=338, height=259)
root.maxsize(width=338, height=259)
#Define o Incone da Janela
root.iconbitmap('pypixel.ico')

visor = Entry(root, width=54, borderwidth=6)
visor.grid(row=0, column=0, columnspan=4, ipady=8)
#Expressa os números no visor
def btn_click(number):
     atual = visor.get()
     visor.delete(0, END)
     visor.insert(0, str(atual) + str(number))

#Limpa o visor
def btn_clear():
     visor.delete(0, END)
#Aciona o gatilho para a função especificada
def btn_plus():
     n1 = visor.get()
     global pN1
     global math
     math = "adição"
     pN1 = float(n1)
     visor.delete(0, END)

def btn_minus():
     n1 = visor.get()
     global pN1
     global math
     math = "subtração"
     pN1 = float(n1)
     visor.delete(0, END)

def btn_multiply():
     n1 = visor.get()
     global pN1
     global math
     math = "multiplicação"
     pN1 = float(n1)
     visor.delete(0, END)
     
def btn_divide():
     n1 = visor.get()
     global pN1
     global math
     math = "divisão"
     pN1 = float(n1)
     visor.delete(0, END)
#Executa as operações com o gatilho especificado e apresenta o resultado     
def btn_equal():
     n2 = float(visor.get())
     visor.delete(0, END)

     if math == "adição":
          visor.insert(0, pN1 + n2)
     elif math == "subtração":
          visor.insert(0, pN1 - n2)
     elif math == "multiplicação":
          visor.insert(0, pN1 * n2)
     elif math == "divisão":
          if n2 == 0:
               visor.insert(0, "Não é possível dividir por zero")
          else:
               visor.insert(0, pN1 / n2)

#Define os botões
btn_1 = Button(root, text="1", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(1))
btn_2 = Button(root, text="2", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(2))
btn_3 = Button(root, text="3", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(3))
btn_4 = Button(root, text="4", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(4))
btn_5 = Button(root, text="5", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(5))
btn_6 = Button(root, text="6", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(6))
btn_7 = Button(root, text="7", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(7))
btn_8 = Button(root, text="8", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(8))
btn_9 = Button(root, text="9", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(9))
btn_0 = Button(root, text="0", padx=35, pady=15, bg="#363232", fg="white", command=lambda: btn_click(0))
#Define os Operadores
btn_plus = Button(root, text="+", padx=31, pady=15, bg="#363232", fg="white", command=btn_plus)
btn_minus = Button(root, text="-", padx=32, pady=15, bg="#363232", fg="white", command=btn_minus)
btn_multiply = Button(root, text="*", padx=32, pady=15, bg="#363232", fg="white", command=btn_multiply)
btn_divide = Button(root, text="/", padx=32, pady=15, bg="#363232", fg="white", command=btn_divide)

btn_equal = Button(root, text="=", padx=34, pady=15, bg="#363232", fg="green", command=btn_equal)
btn_clear = Button(root, text="C", padx=34, pady=15, bg="#363232", fg="red", command=btn_clear)

#Organiza os botões
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=1)

btn_plus.grid(row=1, column=3)
btn_minus.grid(row=2, column=3)
btn_multiply.grid(row=3,column=3)
btn_divide.grid(row=4, column=3)
btn_clear.grid(row=4, column=0)
btn_equal.grid(row=4, column=2)

root.mainloop()
