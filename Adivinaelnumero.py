import random

def main():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        intento_usuario = int(input("Ingresa tu intento: "))
        intentos += 1

        if intento_usuario < numero_secreto:
            print("El número que estoy pensando es mayor que tu intento.")
        elif intento_usuario > numero_secreto:
            print("El número que estoy pensando es menor que tu intento.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    main()
