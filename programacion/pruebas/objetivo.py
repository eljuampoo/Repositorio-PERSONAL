correcto = "Si estas leyendo esto es porque pudiste resolver nuestra operacion basica. \nBien ahi."
fallaste = "No lograste resolver algo tan basico? que tontito."

operacion = int(input("¿Cuanto es 2+2? "))

if operacion == 4:
    print(correcto)
else:
    print(fallaste)