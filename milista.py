# ejemplo de uso de lista
misnovias=["Agripina","Anastacia","Maria"]
misnumeros=[666,77,10]
# Mostrando mis novias
print(misnovias)
# Mostrando mis numeros raros
print(misnumeros)
print("---accediendo a los elementos de la lista---")
print(misnovias[-2])
if "Ana" in misnovias:
  print("si, 'Ana' esta en la lista de mis novias")
else:
  print("chale no es mi novia")
print("Numero de novias")
Nnovias=len(misnovias)
print(f"Numero de novias = {Nnovias}")
print("ciclo for en listas")
posicion=0
for medianaranja in misnovias:
    print(posicion," ",medianaranja)
    posicion=posicion+1