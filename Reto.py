"""Ejercicio! 
    El objetivo es usar los métodos de las listas en python:
    append(), remove(), insert() y pop() para resolver el problema
    para hacer que la frase "Don't panic!" se vuelva "on tap" e imprimirlo en consola
    Las primeras lineas de código convierten la frase en una lista y la imprimen
    Las últimas tres líneas unen la lista de vuelta en un string y lo imprimen,
    en ese momento debe imprimir "on tap"
    No se pueden modificar las líneas de código ya dadas, solo escribir nuevo 
    código en donde se indica.
    Pista: Se pueden usar if's y for's para tareas repetitivas ;)
 """
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#Your code
index = 0
bucle = True
while bucle:
    if plist[index]=='o':
        index += 1
        break
    else:
        plist.append(plist.pop(index))
while bucle:
    if plist[index]=='n':
        index += 1
        break
    else:
        plist.append(plist.pop(index))
while bucle:
    if plist[index]==' ':
        index += 1
        break
    else:
        plist.append(plist.pop(index))
while bucle:
    if plist[index]=='t':
        index += 1
        break
    else:
        plist.append(plist.pop(index))
while bucle:
    if plist[index]=='a':
        index += 1
        break
    else:
        plist.append(plist.pop(index))
while bucle:
    if plist[index]=='p':
        index += 1
        break
    else:
        plist.pop(index)

#End of your code

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)