from tkinter import *

# ****************************************** FUNCIONES ******************************************

i=0
band=0

def agregar (tecla):
    global i
    global band
    if band==1 :
        borrartodo()
        band=0
    i+=1
    resultado.insert(i, tecla)

def operacion ():
    global i
    global band
    texto = resultado.get()
    if i!=0 :
        try:
            result = str(eval(texto))
            resultado.delete(0,END)
            resultado.insert(0, result)
            length = len(result)
            i= length
        except:
            resultado.delete(0,END)
            resultado.insert(0, "ERROR")
            band=1
    else :
        pass

def borrar () :
    global i
    if i!=0 :
        i-=1
        resultado.delete(i,END)
    else :
        pass

def borrartodo():
    resultado.delete(0,END)
    i=0

# *********************************** DECLARAR OBJETOS ****************************************

root=Tk()
root.geometry("300x360")
root.title("CALCULADORA")

marco = Frame (root, bg= 'black')
marco.grid(column = 0,row = 0,padx = 3, pady = 3)

resultado = Entry(marco,bg = '#c4c4c4',width = 23,relief = 'groove',font = 'montserrat 16', justif = 'right')
resultado.grid(columnspan = 4, row = 0, pady = 3, padx = 3, ipadx = 1, ipady = 1)

boton1 = Button(marco,text="1",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(1))
boton2 = Button(marco,text="2",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(2))
boton3 = Button(marco,text="3",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(3))
boton4 = Button(marco,text="4",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(4))
boton5 = Button(marco,text="5",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(5))
boton6 = Button(marco,text="6",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(6))
boton7 = Button(marco,text="7",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(7))
boton8 = Button(marco,text="8",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(8))
boton9 = Button(marco,text="9",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(9))
boton0 = Button(marco,text="0",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar(0))

boton_suma = Button(marco,text="+",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#9a9a9a', anchor= "center",command = lambda:  agregar('+'))
boton_rest = Button(marco,text="-",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#9a9a9a', anchor= "center",command = lambda:  agregar("-"))
boton_mult = Button(marco,text="X",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#9a9a9a', anchor= "center",command = lambda:  agregar('*'))
boton_div = Button(marco,text="/",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#9a9a9a', anchor= "center",command = lambda:  agregar('/'))
boton_mod = Button(marco,text="%",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#9a9a9a', anchor= "center",command = lambda:  agregar('%'))
boton_igual = Button(marco,text="=",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#343434', anchor= "center",command = lambda:  operacion())

boton_punto = Button(marco,text=".",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#dddddd', anchor= "center",command = lambda:  agregar("."))

boton_borra = Button(marco,text="←",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#9a9a9a', anchor= "center",command = lambda:  borrar())
boton_blanco = Button(marco,text="AC",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "orange red", bg = '#9a9a9a', anchor= "center",command = lambda:  borrartodo())


# ******************************* POSICIONAR TECLAS ***************************************

boton_borra.grid(row= 1, column = 0,padx = 5, pady = 5,sticky=W+E)
boton_blanco.grid(row= 1, column = 1,padx = 5, pady = 5,sticky=W+E)
boton_mod.grid(row= 1, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_div.grid(row= 1, column = 3,padx = 5, pady = 5,sticky=W+E)

boton7.grid(row= 2, column = 0,padx = 5, pady = 5,sticky=W+E)
boton8.grid(row= 2, column = 1,padx = 5, pady = 5,sticky=W+E)
boton9.grid(row= 2, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_mult.grid(row= 2, column = 3,padx = 5, pady = 5,sticky=W+E)

boton4.grid(row= 3, column = 0,padx = 5, pady = 5,sticky=W+E)
boton5.grid(row= 3, column = 1,padx = 5, pady = 5,sticky=W+E)
boton6.grid(row= 3, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_rest.grid(row= 3, column = 3,padx = 5, pady = 5,sticky=W+E)

boton1.grid(row= 4, column = 0,padx = 5, pady = 5,sticky=W+E)
boton2.grid(row= 4, column = 1,padx = 5, pady = 5,sticky=W+E)
boton3.grid(row= 4, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_suma.grid(row= 4, column = 3,padx = 5, pady = 5,sticky=W+E)

boton0.grid(row= 5, column = 0, columnspan = 2, padx = 5, pady = 5,sticky=W+E)
boton_punto.grid(row= 5, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_igual.grid(row= 5, column = 3,padx = 5, pady = 5,sticky=W+E)

root.mainloop()