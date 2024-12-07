#Código creado por Leonardo Mellado, Nicolas Reyes, Hector Valenzuela

#Función para procesar el archivo
def leerArchivo(archivo):
    with open(archivo, 'r') as f:
        # Leer la primera línea: número de estados y símbolos
        estados, simbolos = map(int, f.readline().split())

        # Obtener los símbolos del alfabeto
        alfabeto = f.readline().split()
        # Crear el diccionario de transiciones
        transiciones = {estado: {simbolo: '-' for simbolo in alfabeto} for estado in range(estados)}

        # Leer y procesar las reglas de transición
        for _ in range(estados * simbolos):
            estado, simbolo, nuevo_simbolo, direccion, nuevo_estado = f.readline().split()
            transiciones[int(estado)][simbolo] = f"{nuevo_simbolo} {direccion} {nuevo_estado}"

        # Leer el número de cintas
        num_cintas = int(f.readline())

        # Leer las cintas
        cintas = [list(f.readline().strip()) for _ in range(num_cintas)]
    return estados,simbolos,alfabeto,transiciones,num_cintas,cintas

# Función para imprimir los datos de la máquina de Turing y la aceptación o rechazo de los casos
def prints_maquina_turing(estados, simbolos, alfabeto, transiciones,num_cintas,cintas):
    print("\n---- Máquina de Turing ----\n")
    print("Estados:", estados)
    print(f"Símbolos ({simbolos}): {' '.join(alfabeto)}")
    print("Función de transición:")  
    encabezado = " " * 4  
    for simbolo in alfabeto:
        encabezado += simbolo.center(10)
    print(encabezado)
    print("-" * 36)
    for estado in range(estados):
        row = f"{estado}".rjust(3) + " |"
        for simbolo in alfabeto:
            transicion = transiciones[estado][simbolo]
            if transicion == '-':
                row += " " * 10
            else:
                nuevo_simbolo, direccion, nuevo_estado = transicion.split()
                if nuevo_estado == '-1':
                    row += f" {nuevo_simbolo} {direccion} {nuevo_estado}".ljust(9) + " "
                else:
                    row += f" {nuevo_simbolo} {direccion}  {nuevo_estado}".ljust(10)
        print(row)
    if num_cintas > 1:
        print(f"\n{num_cintas} casos disponibles\n")
    else:
        print(f"\n{num_cintas} caso disponible\n")

    # Procesamiento de las cadenas
    for i in range(len(cintas)):
       print(f">> Caso {i+1}")
       print(f"Cadena de entrada: {cintas[i]}")
       print("[La cadena es aceptada]\n" if transicionar(cintas[i], transiciones) else "[La cadena es rechazada]\n")
 
# Función para realizar los movimientos de cabezal, lectura y escritura de la cinta 
def transicionar(cadena,transiciones):
    cabezal = 0
    cinta = cadena + ["-"]
    estado = 0 
    # Mientras no se llegue a un estado final la maquina sigue funcionando
    while estado != -1:
        
        simbolo = cinta[cabezal]

        #print("SIMBOLO : ", simbolo)
        #print("ESTADO: ", estado)
        #print("CABEZAL: ",cabezal)
        #print("\n")

        agregarCinta,mover,estado = movimiento(tuple(transiciones[estado][simbolo].replace(" ","")))

        #print(f"Agregar Cinta: {agregarCinta}, Mover: {mover}, Estado: {estado}")

        cinta[cabezal] = agregarCinta
        if mover == "i":
            cabezal += -1
        elif mover == "d":
            cabezal += 1
        #print(cinta)
        
    # Si llega al estado final y en la cinta de la posición del cabezal solo se encuentra una "a" 
    # y solo existe una "a" en la cinta y no es la cadena vacía se dirá que es una cadena aceptada
    if estado == -1 and cinta[cabezal] == "a" and cinta.count("a") == 1 and cadena != []:
        print("Cinta resultante: ",cinta)
        print("Posición del cabezal: ",cabezal)
        return True
    # Si no cumple lo de arriba y llega al estado final es un estado rechazado
    if estado == -1:
        print("Cinta resultante: ",cinta)
        print("Posición del cabezal: ",cabezal)
        return False
    # Si llega a cualquier otro estado se rechaza
    else:
        print("Cinta resultante: ",cinta)
        print("Posición del cabezal: ",cabezal)
        return False


def movimiento(tupla):
    # Procesamiento de las transiciones para no tener que hacer 100 if
    if len(tupla) == 4:
        nuevaTupla = (tupla[0],tupla[1],"-1")
        agregarCinta=nuevaTupla[0]
        mover=nuevaTupla[1]
        nuevoEstado=int(nuevaTupla[2])
    else:
        agregarCinta=tupla[0]
        mover=tupla[1]
        nuevoEstado=int(tupla[2])
    return agregarCinta,mover,nuevoEstado


# Función main
def main():
    estados, simbolos, alfabeto, transiciones,num_cintas,cintas = leerArchivo("entrada.txt")
    prints_maquina_turing(estados, simbolos, alfabeto, transiciones,num_cintas,cintas)
 
if __name__ == "__main__":
    main()
