'''determinar si un estudianten aprueba el trimestre, sabiendo lo siguiente:
a) asistencia= 30%
b) notas= 50%
c) participacion=20%
el estudiante aprueba con el 80%'''

try:
	parti = int (input("ingrese la nota de participacion: "))
    notas = int (input ("ingrese la nota de actividades"))
    asisten = int (input("ingrese la nota de asistencia: "))

    if ((notas >= 0 and notas <= 100) and (asisten >= 0 and asisten <= 100 ) or (parti >= 50 and <= 100))

        prom_trimestre = ((parti + asisten + notas) / 3)
         if prom_trimestre >= 80:
             print("usted aprobo el trimestre ")
         else:
	         print("usted no aprobo el trimestre ")
	else:
	     print("rango incorrecto ")
except valueError:
    print("valor diferente")