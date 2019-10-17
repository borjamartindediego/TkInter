import tkinter as tk
#config es una manera de poder pasar atributos al boton
#aunque declaremos una variable aqui no sera totalmente global porque todas las funciones en tk inter funcionan como un callback

def col():
    #la declaramos aqui r aunque no tenga sentido
    #global es una instruccion que hace la variable global aunque este en una funcion
    global pulsado

                
            
    if pulsado==False:
         boton.config(bg="blue")
         pulsado=True
    else:
        boton.config(bg="red")
        pulsado=False
    
#Con config le estamos diciendo que al pulsar en el boton haga .....
#    ventana.iconify()
#    time.sleep(3)
#    ventana.deiconify()

print("hola")
ventana=tk.Tk()
#ventana.geometry('200x200')
ventana.title('título')

#etiqueta=tk.Label(ventana,text="hola tkinter")
etiqueta=tk.Label(ventana,text="HOLA")
#El pack es un layout automatico para colocar el elemento en pantalla
#Si comentamos etiqueta.pack, no se imprime hola tkinter
#Tambien tenemos grid (por filas y columnas) y place por coordenadas
etiqueta.pack(side=tk.LEFT)
#command ES PARECIDO A UN EVENTO JS ONCLICK
#boton=tk.Button(ventana, text="pulsa", command=ventana.iconify)
boton=tk.Button(ventana, text="pulsa", command=col)
boton.pack(side="left")
# Con esta linea se queda en azul permanente boton.config(bg="blue")

ventana.mainloop() #mantiene la ventana en ejecucion
