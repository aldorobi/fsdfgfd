# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:09:14 2023

@author: Aldo
"""

from tkinter import *
from  tkinter import ttk
from PIL import ImageTk,Image

spidercat = Tk()
spidercat.title("Spydercat!")
spidercat.geometry("1200x1200")
spidercat.configure(background = "sienna")


cat = ImageTk.PhotoImage(Image.open("cat.jpg"))

etiqueta_animalCatFOTO = Label(spidercat,bg = "sienna",highlightthickness = 5,borderwidth = 3, relief = SOLID )
etiqueta_animalCatFOTO['image'] = cat
etiqueta_animalCatFOTO.place(relx = 0.7, rely = 0.5, anchor = CENTER)


Tienda_la_Morena = Label(spidercat,text = "Tienda la morena!",font = ("comic sans ms",40,"bold"), bg = "Sienna1")
Tienda_la_Morena.place(relx = 0.7, rely = 0.25, anchor = CENTER)


Selecciona_la_Raza = Label(spidercat,text = "SELECIONA LA RAZAA!!",font = ("comic sans ms",10,"bold"), bg = "Sienna1")
Selecciona_la_Raza.place(relx = 0.20, rely = 0.30, anchor = CENTER)


Lista_Gato = ["ragdoll","maine coon","snowshoe","british shorthair"]
Starbucksato = ttk.Combobox(spidercat,state = "readonly", values = Lista_Gato)
Starbucksato.place(relx = 0.20, rely = 0.32, anchor = CENTER)



Selecciona_el_pedigree = Label(spidercat,text = "SELECIONA el PEDIGREE!!!!!!",font = ("comic sans ms",10,"bold"), bg = "Sienna1")
Selecciona_el_pedigree.place(relx = 0.20, rely = 0.40, anchor = CENTER)


Lista_Pedigree = ["si", "no"]
Starbuckschiato = ttk.Combobox(spidercat,state = "readonly", values = Lista_Pedigree)
Starbuckschiato.place(relx = 0.20, rely = 0.42, anchor = CENTER)


Selecciona_la_Dieta = Label(spidercat,text = "SELECIONA la Dieta!!!!!!",font = ("comic sans ms",10,"bold"), bg = "Sienna1")
Selecciona_la_Dieta.place(relx = 0.20, rely = 0.50, anchor = CENTER)


Lista_dieta = ["con dieta", "sin dieta"]
Starbuckschai = ttk.Combobox(spidercat,state = "readonly", values = Lista_dieta)
Starbuckschai.place(relx = 0.20, rely = 0.52, anchor = CENTER)


CantidadPagar = Label(spidercat,font = ("comic sans ms",10,"bold"), bg = "Sienna1")
CantidadPagar.place(relx = 0.20, rely = 0.70, anchor = CENTER)



class Tienda ():
    def __init__(self):
        TIENDA = "Tienda la morena"
        print(TIENDA)
        
    def Tipos (raza):
        if raza == "ragdoll":
            Lista_Pedigree = "si","no"
            print ("Felicidades! has comprado/adoptado un ragdoll"+"\n")
            print ("Porfavor selccione la dieta y el pedigree.")
            print ("Pedigree?"+"\n")
            print ("dieta?"+"\n")
            
            
        elif raza == "maine coon":
            print ("Felicidades! has comprado/adoptado un maine coon")
            print ("Porfavor selccione la dieta y el pedigree.")
            print ("Pedigree?"+"\n")
            print ("dieta?"+"\n")
            
        elif raza == "snowshoe":
            print ("Felicidades! has comprado/adoptado un snowshoe")
            print ("Porfavor selccione la dieta y el pedigree.")
            print ("Pedigree?"+"\n")
            print ("dieta?"+"\n")
            
        elif raza == "british shorthair":
            print ("Felicidades! has comprado/adoptado un british shorthair")
            print ("Porfavor selccione la dieta y el pedigree.")
            print ("Pedigree?"+"\n")
            print ("dieta?"+"\n")
        
    def Raza_Pedigree (raza,pedigree,comida):
        if raza == "ragdoll" and pedigree == "si" and comida == "sin dieta":
            print ("el precio con pedigree es: " + "750$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 750$"
            
        elif raza == "ragdoll" and pedigree == "si" and comida == "con dieta":
            print ("el precio con pedigree y con dieta es: " + "2500$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 25000$"
        
        elif raza == "ragdoll" and pedigree == "no" and comida == "sin dieta":
            print ("el precio sin nada: " + "500$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 500$"
            
        elif raza == "ragdoll" and pedigree == "no" and comida == "con dieta":
            print ("el precio con dieta es: " + "1200$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 1200$"
            
            
        elif raza == "maine coon" and pedigree == "si" and comida == "sin dieta":
            print ("el precio con pedigree es: " + "3750$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 3750$"
            
        elif raza == "maine coon" and pedigree == "si" and comida == "con dieta":
            print ("el precio con pedigree y con dieta es: " + "5000$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 5000$"
        
        elif raza == "maine coon" and pedigree == "no" and comida == "sin dieta":
            print ("el precio sin nada: " + "2000.01$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 2000.01$"
            
        elif raza == "maine coon" and pedigree == "no" and comida == "con dieta":
            print ("el precio con dieta es: " + "3500$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 3500$"
            
        
        elif raza == "snowshoe" and pedigree == "si" and comida == "sin dieta":
            print ("el precio con pedigree es: " + "2000$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 2000$"
            
        elif raza == "snowshoe" and pedigree == "si" and comida == "con dieta":
            print ("el precio con pedigree y con dieta es: " + "4000$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 4000$"
        
        elif raza == "snowshoe" and pedigree == "no" and comida == "sin dieta":
            print ("el precio sin nada: " + "1250$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 1250$"
            
        elif raza == "snowshoe" and pedigree == "no" and comida == "con dieta":
            print ("el precio con dieta es: " + "3500$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 3500$"
            
            
        elif raza == "british shorthair" and pedigree == "si" and comida == "sin dieta":
            print ("el precio con pedigree es: " + "1000$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 1000$"
            
        elif raza == "british shorthair" and pedigree == "si" and comida == "con dieta":
            print ("el precio con pedigree y con dieta es: " + "2500$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 2500$"
        
        elif raza == "british shorthair" and pedigree == "no" and comida == "sin dieta":
            print ("el precio sin nada: " + "0$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 0$"
            
        elif raza == "british shorthair" and pedigree == "no" and comida == "con dieta":
            print ("el precio con dieta es: " + "1250$ " + "\n")
            CantidadPagar["text"]  = "el precio con pedigree es: 1250$"
            
            
            
class Cliente (Tienda):
    def __init__(self,raza):
        self.raza = raza
    def obtener_raza (self):
        raza = Starbucksato.get()
        Tienda.Tipos(raza)
        



class Pedigree_dieta (Tienda):
    def __init__(self,raza,pedigree,comida):
        self.raza = raza
        self.pedigree = pedigree
        self.comida = comida
    
    def CuantoCobranLosGatitos (self):
        raza = Starbucksato.get()
        pedigree = Starbuckschiato.get()
        dieta = Starbuckschai.get()
        Tienda.Raza_Pedigree(raza, pedigree, dieta)
        
Cliente1Orden1 = Cliente(Starbucksato.get())
Cliente1Orden1.obtener_raza()

Cliente1Orden2 = Pedigree_dieta(Starbucksato.get(),Starbuckschiato.get(), Starbuckschai.get())
Cliente1Orden2.CuantoCobranLosGatitos()


Cliente2Orden1 = Cliente("maine coon")
Cliente2Orden1.obtener_raza()

Cliente2Orden2 = Pedigree_dieta("maine coon","si","con dieta")
Cliente2Orden2.CuantoCobranLosGatitos()


Cliente3Orden1 = Cliente("british shorthair")
Cliente3Orden1.obtener_raza()

Cliente3Orden2 = Pedigree_dieta("british shorthair","no","sin dieta")
Cliente3Orden2.CuantoCobranLosGatitos()


boton = Button(spidercat, text = "aja",Command = Cliente1Orden2.CuantoCobranLosGatitos)
boton.pack()


spidercat.mainloop()

            

        
    
        