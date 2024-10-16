import os
import modulos as pck
from tabulate import tabulate
def menu ():
    os.system('clear')
    rgstr_equipos = []
    fecha_prt = []
    rslt_prt = []

    while True:
        ttl = """
            ***************
            * LigaBetPlay *    
            ***************
        """
        print(ttl)
        try:
            opc = int(input("1. Registrar Equipo\n2. Registrar Plantel Equipo\n3. Programar Fecha Partido\n4. Registrar Resultado Partido\n5. Ver Equipos\n6. Tabla de clasificación\nIngresar opciòn: "))
            os.system('clear')
            if (opc == 1):
                pck.rgstr_equipos(rgstr_equipos)
            elif (opc == 2):
                pck.rgstr_plantel(rgstr_equipos)
            elif (opc == 3):
                pck.fecha_prt(fecha_prt, rgstr_equipos)
            elif (opc == 4):
                pck.rslt_prt(fecha_prt, rslt_prt, rgstr_equipos)
            elif (opc == 5):
                pck.ver_equipos(rgstr_equipos)
            elif (opc == 6):
                pck.showStats(rgstr_equipos)
            else:
                print("Opciòn no vàlida")
        except:
            print('Ingreso un tipo de dato invalido')



