from tkinter import*
import cv2
import numpy as np
from PIL import Image

raiz=Tk()

raiz.title("Editor")

#raiz.iconbitmap("")

miFrame = Frame()
miFrame.pack(fill="both")
miFrame.config(width="1250",height="750")
miFrame.config(bg="gray")

def agregar_imagen():
    img = cv2.imread('foto.jpg')
    img=cv2.resize(img,(300,250))
    cv2.imshow('Imagen original',img)
    cv2.waitKey(0)

botonAgregarImagen=Button(miFrame,text="Agregar Imagen", command=agregar_imagen)
botonAgregarImagen.pack()
botonAgregarImagen.grid(row=0, column=3)




#botonRecortarImagen=Button(miFrame,text="Recortar Imagen", command=recortarImagen)
#botonRecortarImagen.pack()
#botonRecortarImagen.grid(row=5, column=0)

#def recortarImagen():

#botonRotarImagen=Button(miFrame,text="Rotar Imagen", command=rotarImagen)
#botonRotarImagen.pack()
#botonRotarImagen.grid(row=5, column=1)

#def rotarImagen():

def filtro1():
    imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagen Gray', imgGray)

botonFiltro1=Button(miFrame,text="Filtro 1", command=filtro1)
botonFiltro1.pack()
botonFiltro1.grid(row=5, column=2)


def filtro2():
    imgBlur = cv2.GaussianBlur(img, (5, 5), 1)
    cv2.imshow('Imagen Suavizada', imgBlur)


botonFiltro2=Button(miFrame,text="Filtro 2", command=filtro2)
botonFiltro2.pack()
botonFiltro2.grid(row=5, column=3)

def filtro3():
    imgCanny=cv2.Canny(img,200,200)
    cv2.imshow('Imagen Canny',imgCanny)

botonFiltro3=Button(miFrame,text="Filtro 3", command=filtro3)
botonFiltro3.pack()
botonFiltro3.grid(row=5, column=4)






raiz.mainloop()