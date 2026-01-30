# Programa para calcular la nota definitiva de un estudiante


print("------------------------------------")
print("-------Nota Definitiva Curso--------")
print("------------------------------------")


# input
# Se solicitan las notas siguiendo el diagrama de flujo
nc = input("Ingrese la nota de Nc (30%): ")
np = input("Ingrese la nota de Np (30%): ")
na = input("Ingrese la nota de Na (10%): ")
au = input("Ingrese la nota de Au (10%): ")
bi = input("Ingrese la nota de Bi (20%): ")


# Conversión a flotante para permitir decimales
nc = float(nc)
np = float(np)
na = float(na)
au = float(au)
bi = float(bi)


# processing
# Fórmula: nd = 0.3*nc + 0.3*np + 0.1*na + 0.1*au + 0.2*bi
nd = 0.3*nc + 0.3*np + 0.1*na + 0.1*au + 0.2*bi


# output
print("------------------------------------")
print("-------------Resultados-------------")
print("------------------------------------")
print("La nota definitiva (nd) es: " + str(nd))
print("------------------------------------")
