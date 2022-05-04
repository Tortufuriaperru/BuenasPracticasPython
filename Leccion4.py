# APARTADO 1

#definimos la lista del ejemplo

lista = [[2,4,1], [1,2,3,4,5,6,7,8],[100,250,43]] 

# Comprension de listas

import pdb

#pdb.set_trace()

def lista_de_maximos(lista):
    maxsublist = [max(p) for p in lista]
    return maxsublist 


lista = [[2,4,1], [1,2,3,4,5,6,7,8],[100,250,43]] 
if __name__ == '__main__':
        lista_de_maximos(lista)


# Se podria haber hecho usando map, o sin usar comprension de listas

maxsublist2 = list(map(max, lista)) 
  
print(maxsublist2) 



def lista_maximos(lis):
    maximos=[]
    
    for sublista in lis:
        contador=max(sublista)
        maximos.append(contador)
    return maximos

print(lista_maximos(lista))


# APARTADO 2

# Se define una función que nos devolverá verdadero o falso 
# dependiendo de si el número es primo o no lo es.

def es_primo(x):
	
	for i in range(2,x):
		if x % i == 0:
			return False
	return True


# Esto nos devolverá verdadero
print(es_primo(11))
# Esto nos devolverá falso
print(es_primo(8))


# Se hará uso de la orden filter para que nos devuelva una lista
# con los elementos que si sean primos.


lista2 = [3, 4, 8, 5, 5, 22, 13]

print(list(filter(es_primo,lista2)))        
