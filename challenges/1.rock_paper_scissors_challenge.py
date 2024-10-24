# Piedra, papel y tiejeras: Ejercicio práctica de estructuras condicionales

## Primero haremos una variable para player1 y player2 y recibir un input de ambos. 
"""
Las opciones validas son solo 'piedra', 'papel' y 'tijeras'. En caso de que sea un opción diferente,
pediremos al jugador que ingrese otra vez la opción hasta que sea la opción correcta.
De esta manera, evitamos que pongan palabras diferentes y aleatorias. Se agregará un condicional para esta función.
"""

## Estas son las palabras permitidas
opciones_validas = ['piedra', 'papel', 'tijeras'];

# Opciones para juador1
while True:
    ## En este bucle, asignamos la variable con el input. Hay dos métodos. 
    ### .lower() recibe el input y vuelve el string en minúsculas. Así, no recibiremos palabras como PieDRa, TIJERas. De esta manera normalizamos la entrada
    ### .strip() normaliza la entra también pero quitando los espacio que puedan haber al inicio o al final.
    jugador1 = input("Jugador 1, elige entre 'piedra, papel y tijeras: ").lower().strip();
    ## Si las opciones ingresadas en jugador1 están en la variable de opciones_Validas, entonces procederá con el primer bucle.
    if jugador1 in opciones_validas:
        print(f'Jugador1 has elegido {jugador1}');
        break
    ## Si no se cumplen las funciones de arriba, entonces entrará en este bucle.
    else:
        print(f'Jugador1 no has elegido correctamente. Por favor elige entre piedra, papel o tijeras');

 # Opciones para jugador2. Son las mismas opcioones que jugador 1
while True:
    jugador2 = input("Jugador 2, elige entre 'piedra, papel y tijeras: ").lower().strip();
    if jugador2 in opciones_validas:
        print(f'Jugador2 has elegido {jugador1}');
        break
    else:
        print(f'Jugador2 no has elegido correctamente. Por favor elige entre piedra, papel o tijeras');

## Estructura piedra

if jugador1 == 'piedra' and jugador2 == 'tijeras':
    print("Jugador1 gana esta partida");
elif jugador1 == jugador2:
    print("Esta partida es un empate");
elif jugador1 == 'piedra' and jugador2 == 'papel':
    print("Jugador2 gana esta partida");
#else:
    #print("Esta partida es invalida");

# Estructura papel

if jugador1 == 'papel' and jugador2 == 'tijeras':
    print("Jugador2 gana esta partida");
elif jugador1 == 'papel' and jugador2 == 'piedra':
    print("Jugador1 gana esta partida");
elif jugador1 == jugador2:
    print("Esta partida es un empate");
#else:
    #print("Esta partida es invalida");


# Estructura tijeras

if jugador1 == jugador2:
    print("Esta partida es un empate");
elif jugador1 == 'tijeras' and jugador2 == 'piedra':
    print("Jugador2 gana esta partida");
elif jugador1 == 'tijeras' and jugador2 == 'papel':
    print("Jugador1 gana esta partida")

