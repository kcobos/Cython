# -*- coding: utf-8 -*-
import fibonacciPython
import fibonacciCython
from ctypes import cdll
libfi = cdll.LoadLibrary('./libfibonacci.so')

from datetime import datetime
import matplotlib.pyplot as plt
import os

nMax = 36

tiemposPy = []
tiemposCy = []
tiemposC = []

for n in range(1,nMax):
	t1 = datetime.now()
	fibonacciPython.fibonacciRec(n)
	t2 = datetime.now()
	delta = t2 - t1
	tiemposPy.append(delta.total_seconds())
	print("n = ", n, "\ttiempo = ", delta.total_seconds())
print("fin fibonacciPython")

for n in range(1,nMax):
	t1 = datetime.now()
	fibonacciCython.fibonacciRec(n)
	t2 = datetime.now()
	delta = t2 - t1
	tiemposCy.append(delta.total_seconds())
	print("n = ", n, "\ttiempo = ", delta.total_seconds())
print("fin fibonacciCython")

for n in range(1,nMax):
	t1 = datetime.now()
	libfi.fibonacciRecC(n)
	t2 = datetime.now()
	delta = t2 - t1
	tiemposC.append(delta.total_seconds())
	print("n = ", n, "\ttiempo = ", delta.total_seconds())
print("fin fibonacciC")


plt.plot(range(1,nMax), tiemposPy, "b.-", label="Python")
plt.plot(range(1,nMax), tiemposCy, "r.-", label="Cython")
plt.plot(range(1,nMax), tiemposC, "k.-", label="C/C++")
plt.legend(loc=3)
plt.xlabel('Número de entrada')
plt.ylabel('Tiempo empleado el calcularlo (s)')
plt.show()


import cythonC

print(cythonC.string_to_int(b"54"))
