# -*- coding: utf-8 -*-
"""Consulta_Python_Miguel_Angulo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZRYB5njYySlhj05gFMQJz4Qkvf0Jikxj
"""

import numpy as np
from collections import OrderedDict, Counter

# Miguel Angel Angulo - 2170812

#1)

#Utilizamos la libreria collections para poder ordenar nuestro array por numero de apariciones
class OrderedCounter(Counter, OrderedDict):
    pass

#Creamos un Ndarray con 5000 posiciones, donde cada posición representa un voto por el número de ese candidato.
#Cabe destacar que el número 0 representará el voto en blanco.
a = np.random.randint(31,size=(5000))

#Ordenamos nuestro Array por mayor cantidad de votos:
c = OrderedCounter(a)
keys = list(c)
a_ord = sorted(c, key=lambda x: (-c[x],keys.index(x)))
print("La votación por los candidatos terminó en el siguiente orden: \n",a_ord)

#2)

#Creamos una clase estudiante que tengan los atributos código, nombre, promedio acumulado
class Estudiante:
  def __init__(self,codigo,nombre,promedio):
    self.codigo = codigo
    self.nombre = nombre
    self.promedio = promedio

  def showEstudiante(self):
    print("\n Nombre:",self.nombre,"\n Código:",self.codigo,"\n Promedio acumulado:",self.promedio)

#Para mostrar la lógica y funcionamiento del algoritmo solo utilizaremos 8 estudiantes, ya que instanciar 6500 estudiantes no resulta viable.
id = [1891815,2170812,1880402,2210311,2200901,1850321,2051034,1862030]
nom = ["Maria","Pedro","Jaime","Brian","Miguel","Carlos","Sebastian","Lucia"]
pa = [3.0,4.2,4.1,3.6,2.9,2.8,3.9,4.7]
b = [] #El array b sera un array donde cada posición guardará a un estudiante.

#Insertamos los 8 estudiantes en el array
for i in range(0,8):
  b.append(Estudiante(id[i],nom[i],pa[i]))

#Algoritmo para resolver el punto 2.1)
cont = 0
for i in b:
  if i.promedio > 4.0:
    i.showEstudiante()
    cont = cont+1
print("\n El número de estudiantes con promedio acumulado mayor a 4.0 es:",cont)

#Algoritmo para resolver el punto 2.2)
#Cabe destacar que las primeras 3 cifras indican el año de ingreso, por lo que cualquier codigo menor a 1900000 indicara que ingreso antes de 1990.
print("\n Estudiantes ingresados antes de 1990 y en estado de condicional:")
for i in b:
  if i.codigo < 1900000 and i.promedio < 3.2:
    i.showEstudiante()