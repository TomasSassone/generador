import random
from tkinter import *

raiz = Tk()

raiz.title('Cuál es tu nombre de ElChat?')

raiz.resizable(1, 1)

#raiz.geometry('750x600')


miFrame = Frame()

miFrame.pack(fill='both', expand='true')

miFrame.config(width='650', height='500')

miLabel = Label(miFrame, text='¿Cuál es tu nombre de ElChat?', font=15)
miLabel.grid(row=1, column=1, padx=10, pady=10)

pantalla=Entry(miFrame)
pantalla.grid(row=2, column=1, padx=30, pady=15)
pantalla.config(justify='center', width=35)


#-----------------------generador de nombres------------------------------

profesiones = ['PLOMERO', 'ELECTRICISTA', 'ALBAÑIL', 'CONTADOR', 'PINTOR', 'TÉCNICO', 'AYUDANTE DE CÁTEDRA', 'ABOGADO', 'CARNICERO', 'CONSERJE', 'FOTÓGRAFO', 
'DISEÑADOR', 'PEDIATRA', 'NEUROCIRUJANO', 'ODONTÓLOGO', 'ESTILISTA']

random_prof = random.choice(profesiones)

adjetivos = ['HONESTO'. 'TRABAJADOR', 'RESPONSABLE', 'DETERMINADO', 'SOCIAL']

random_adj = random.choice(adjetivos)

edad = random.randint(27, 88)

#------------------------------botón---------------------------------------


def codigoBoton():

  pantalla.delete(0, 'end')
  text = random_prof + ' ' + random_adj + ' ' + str(edad)
  pantalla.delete(0, END)
  pantalla.insert(0, text)
	


botonInicio = Button(raiz, text='Iniciar', command=codigoBoton)

botonInicio.pack()



raiz.mainloop()

