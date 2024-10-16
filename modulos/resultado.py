import os 
def rslt_prt(fechas, cajaResultados, equipos):
    if len(fechas) == 0 : return input('No existe ninguna fecha a registrar')
    print("Estas son las fechas disponibles: ")
    for index, contenido in enumerate(fechas):
        print(f"{index + 1}. {contenido[0]}: {contenido[1]} vs {contenido[2]} ")
    try:
        fecha_partido = int(input("Ingrese el indice de la fecha que desea registrar: "))
        if fecha_partido -1 > len(fechas)-1 or fecha_partido == 0 : return input('No existe un registro de esa fecha.')

        local = ""
        visitante = ''
        for index, contenido in enumerate(equipos):
            if contenido[0] == fechas[fecha_partido - 1][1]: local = index
            if contenido[0] == fechas[fecha_partido - 1][2]: visitante = index
        
        rslt = int(input("Resultado Local: "))
        rslt_2 = int(input("Resultado Visitante: "))
        if rslt > rslt_2:
            print(f"Ganador: {fechas[fecha_partido - 1][1]}\nPerdedor: {fechas[fecha_partido - 1][2]}")
            equipos[local][2] += 3
            equipos[visitante][2] += 0
            equipos[local][3] += 1
            equipos[visitante][4] += 1
        elif rslt < rslt_2:
            print(f"Ganador: {fechas[fecha_partido - 1][2]}\nPerdedor: {fechas[fecha_partido - 1][1]}")
            equipos[local][2] += 0
            equipos[visitante][2] += 3
            equipos[local][4] += 1
            equipos[visitante][3] += 1
        else:
            print("Empate") 
            equipos[local][5] += 1
            equipos[visitante][5] += 1
            equipos[local][2] += 1
            equipos[visitante][2] += 1
# indice 2 putnos de liga
# indice 3 partidos ganadops
# indice 4 partidos perdidos
# indice 5 partidos empatados
    except: input('Ingreso un tipo dato invalido --')
    
    