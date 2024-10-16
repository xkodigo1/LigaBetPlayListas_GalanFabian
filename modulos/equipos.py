import os
def rgstr_equipos(equipos):
    
    print("Registrar Equipo")
    equipo = input("Ingrese el nombre del Equipo: ")
    
    if len(equipo) == 0 or equipo.isspace(): return input('Debe ingresar el nombre de un equipo')
    
    equipos.append([equipo, [], 0, 0, 0, 0, []])
    print("Equipo agregado con èxito.")
    
    input()
