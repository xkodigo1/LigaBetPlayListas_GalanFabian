from tabulate import tabulate

def showStats (equipo):
    
    copiaEquipo = [] # Inicia variable que será la copia de los equipos generales

    

    for index, contenido in enumerate(equipo): # Recorremos el arreglo de equipos original, sacando indice y contenido, cada contenido es un arreglo con los detalles del equipo
        copiaEquipo.append([]) # Inicializamos el arreglo que copiara el equipo de la iteracion actual
        for index2, content in enumerate(contenido): # Recorremos el arreglo del equipo actual, donde content toma por cada iteracion el valor del detalle actual (milloz, pts ...)
            if index2 == 1 or index2 == len(contenido) - 1: continue # si el indice de content es == 1, quiere decir que estamos sobre el cuerpo tecnico, por lo que el continue, se brinca la iteracion, o si el indice es igual a la longitud del contenido querra decir que estamos sobre los jugadores, por lo que tambien deberá saltarlos
            copiaEquipo[index].append(content) # si el indice no es 1, quiere decir que no estamos sobre los tecnicos, por lo que podemos agregar el content


    # Tabulate recibe dos argumentos, el primero es el contenedor (arreglo) que contiene los datos que vamos a querer mostrar
    # el segundo parametro se tiene que llamar 'headers' y se le debe asignar un arreglo (=[]), donde dentro de este arreglo van los encabezados de cada columna
    print(tabulate(copiaEquipo, headers=['Equipo', 'Pts. liga', 'Ptds. ganados', 'Ptds. perdidos', 'Ptds. empatados']))
    input('...')