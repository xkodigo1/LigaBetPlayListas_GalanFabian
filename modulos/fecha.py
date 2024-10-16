import os
def fecha_prt(fecha_prt, cajaEquipos):
    if len(cajaEquipos) <= 1: return input('No existen equipos o debe existir al menos dos')
    print("Estos son los equipos disponibles:")
    for index, contenido in enumerate(cajaEquipos):
        print(f"{index + 1}. {contenido[0]} ")
    
    try:
        fecha = input("Ingrese la fecha en que se jugarà el partido '(dd/mm/aa)': ")
        lcl = int(input("Ingrese el numero del equipo que jugará de local: "))
        if lcl - 1 > len(cajaEquipos) - 1 or lcl == 0 : return input('El equipo que eligio de local no existe')
        vst = int(input("Ingrese el numero del equipo que jugará de visitante: "))
        if vst - 1 > len(cajaEquipos) - 1 or vst == 0: return input('El equipo que eligio de vistante no existe')
        fecha_prt.append([fecha, cajaEquipos[lcl-1][0], cajaEquipos[vst - 1][0], "Pendiente"])


        print(f"Partido programado para {fecha}. Enfrentamiento {lcl} vs {vst}.")
    except: 
        input('Alguno de los datos ingresados es erroneo')