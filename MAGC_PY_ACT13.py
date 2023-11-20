import tkinter as tk

def suma():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja2.get())
    result = num1 + num2
    cadena.set(result)
    cad_signo.set("+")

def resta():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja2.get())
    result = num1 - num2
    cadena.set(result)
    cad_signo.set("-")

def multiplica():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja2.get())
    result = num1 * num2
    cadena.set(result)
    cad_signo.set("*")

def divide():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja2.get())
    result = num1 / num2
    cadena.set(result)
    cad_signo.set("/")


root=tk.Tk()
cadena=tk.StringVar()
cadena.set("")
cad_signo=tk.StringVar()
cad_signo.set("")
root.geometry("470x250")
root.title("CALCULADORA BÁSICA")

lbl_num1=tk.Label(root, text="NUMERO 1")
lbl_num1.place(x=75, y=50)

lbl_num2=tk.Label(root, text="NUMERO 2")
lbl_num2.place(x=225, y=50)

lbl_rest=tk.Label(root, text="RESULTADO")
lbl_rest.place(x=350, y=50)


ent_caja=tk.Entry(root, text="")
ent_caja.place(x=50, y=100)

ent_caja2=tk.Entry(root, text="")
ent_caja2.place(x=200, y=100)

igual=tk.Label(root, text="=")
igual.place(x=330, y=100)

signo=tk.Label(root, textvariable=cad_signo)
signo.place(x=180, y=100)

lbl_msge=tk.Label(root, textvariable=cadena)
lbl_msge.place(x=350, y=100)


btn_suma=tk.Button(root, text="  +  ", command=suma)
btn_suma.place(x=80, y=150)

btn_mult=tk.Button(root, text="  *  ", command=multiplica)
btn_mult.place(x=274, y=150)

btn_resta=tk.Button(root, text="  -  ", command=resta)
btn_resta.place(x=177, y=150)

btn_div=tk.Button(root, text="  /  ", command=divide)
btn_div.place(x=371, y=150)


firma=tk.Label(root, text="©AlexGamboa 2023")
firma.place(x=350, y=220)

root.mainloop()