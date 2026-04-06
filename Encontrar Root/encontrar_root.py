from Merkle_Tree import Merkle_Tree
from itertools import permutations

def encontrar_orden(transacciones, user_root):
    p_orden = list(permutations(transacciones))
    for tras in p_orden:
        k = Merkle_Tree(tras)
        k.calcular_merkle_root() 
        
        if (k.root[0] == user_root):
            return tras


num_transacciones = int(input("Ingrese el número de transacciones: "))
i = 0
input("A continuación ingrese las transacciones en el orden que desee.(presione enter para continuar.)")
transacciones = []
while i != num_transacciones:
    trans = input("Ingrese una transacción: ")
    transacciones.append(trans)
    i += 1
user_root= input("Ingrese su root: ")
orden = encontrar_orden(transacciones, user_root)
if orden == None : 
    print("Con las transacciones ingresadas es imposible generar esa root.")
else:
    print("El orden en el que deben ir las transacciones para generar esa root es: ", orden, "(presione enter para continuar.)")
