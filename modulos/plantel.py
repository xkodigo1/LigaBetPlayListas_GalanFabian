import os
def rgstr_plantel(equipos):
    if len(equipos) == 0: return input('No puede registrar un plantel si no hay equipos existentes')
    print('Estos son los equipos disponibles')

    for index, contenido in enumerate(equipos):
        print(f"{index + 1}. {contenido[0]}")
    
    try:
        equipo = int(input('Ingrese el indice del equipo al que quiere registrar plantel'))
        if equipo -1 > len(equipos)-1 or equipo == 0 : return input('No existe un equipo en ese indice.')

        entrenador = input("Ingrese el nombre del entrenador: ")
        if len(entrenador) == 0 or entrenador.isspace(): return input('No puede registrar nombres vacios')
        asistente = input("Ingrese el nombre del asistente: ")
        if len(asistente) == 0 or asistente.isspace(): return input('No puede registrar nombres vacios')
        preparador_fisico = input("Ingrese el nombre del preparador: ")
        if len(preparador_fisico) == 0 or preparador_fisico.isspace(): return input('No puede registrar nombres vacios')
        
        equipos[equipo - 1][1].append(entrenador)
        equipos[equipo - 1][1].append(asistente)
        equipos[equipo - 1][1].append(preparador_fisico)
        input('Plantel registrado satisfactoriamente\nAcontinuacion deberá registrar a los jugadores')

        while True:
            nombre = input('Ingrese el nombre del jugador -> ')
            posicion = input('Ingrese la posicion del jugador -> ')
            dorsal = int(input('Ingrese el dorsal del jugador -> '))

            equipos[equipo - 1][6].append([nombre, posicion, dorsal])

            continuarJugador = input('Desea agregar otro jugador (Y/N): ').lower()
            if continuarJugador == 'n': break

        

    except:
        input('Tipos de datos invalido')