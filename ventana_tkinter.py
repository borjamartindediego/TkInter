# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:16:34 2019

@author: Borja
"""

import tkinter as tk

def mifuncion():
    print("Soy la funcion")

ventana = tk.Tk()
ventana.title=('mi_ventana')

#etiqueta1=tk.Label(ventana,text='operator')
#etiqueta2=tk.Label(ventana,text='operator2')
#etiqueta3=tk.Label(ventana,text='operator3')
boton=tk.Button(ventana,bg="blue", text='mi_boton',command=mifuncion)
boton1=tk.Button(ventana,bg="blue", text='mi_boton',command=mifuncion)
boton2=tk.Button(ventana,bg="blue", text='mi_boton',command=mifuncion)
#Ahora mismo no se imprimiría necesitamos colocal un layout 
#etiqueta1.pack()
#etiqueta2.pack()
#etiqueta3.pack()
#fill expande el elemento (Y no debe tener elementos en el mismo eje)
#expand fuerza a extender en los ejes que no se rellenar
#boton.pack(fill=tk.BOTH,expand=1)
boton.pack(side=tk.LEFT)
boton1.pack(side=tk.LEFT)
boton2.pack(side=tk.RIGHT)

#Retener la ventana -->  SIEMPRE AL FINAL 
ventana.mainloop()
