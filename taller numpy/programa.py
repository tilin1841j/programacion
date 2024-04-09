#importan la biblioteca
import numpy as np

# una forma de crear arreglos ndarray es usando una lista 

miLista=[3.79,5.89,7,9,"hola"]
miArreglo= np.array(miLista)
#Dimensiones 
print(miArreglo.ndim)

print(miArreglo.shape)

print(miArreglo.size)

print(miArreglo.dtype)

miArreglo= np.array([3,6,7,90])

#crear arreglos de 2 dimensisones a partir de listas

miLista=[(1,3,5,7), (3,8,2,4)]
miArreglo= np.array(miLista, dtype=int)

print(miArreglo.ndim)
print(miLista)


# Usando funoiones de "relleno" de arreglos

miArreglo= np.zeros((3,4))
print(miArreglo)

miArreglo= np.arange(-10,10)
print(miArreglo.ndim)

miArreglo.reshape((2,10))

print(miArreglo)
 # utilizamnos linspace 
 
miArreglo= np.linspace(20,10,10)
miArreglo=miArreglo.reshape(10,10)
print(miArreglo.ndim)



