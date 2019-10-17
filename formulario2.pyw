# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:56:45 2019

@author: Borja
"""

import tkinter as tk

def f():
    print('hola '+ent.get())

v=tk.Tk()
ent=tk.Entry(v)
ent.pack(side=tk.LEFT)
btn=tk.Button(v,text="pulsa",command=f)
btn.pack(side=tk.LEFT)


v.mainloop()
