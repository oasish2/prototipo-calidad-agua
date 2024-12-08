import os
import json
import random

# Nombre del archivo para guardar los datos
archivo_datos = "cuerpos_de_agua.json"


# Función para cargar datos desde el archivo
def cargar_datos():
    if os.path.exists(archivo_datos):
        with open(archivo_datos, "r") as archivo:
            return json.load(archivo)
    return []


# Función para guardar datos en el archivo
def guardar_datos(datos):
    with open(archivo_datos, "w") as archivo:
        json.dump(datos, archivo, indent=4)


# Función para clasificar el IRCA
def clasificar_irca(irca):
    if irca <= 5:
        return "Sin riesgo"
    elif irca <= 14:
        return "Riesgo bajo"
    elif irca <= 35:
        return "Riesgo medio"
    elif irca <= 80:
        return "Riesgo alto"
    else:
        return "Riesgo inviable sanitariamente"


def opciones_tipos(opc):
    if opc == 1:
        tpa = "Lagos"
    elif opc == 2:
        tpa = "Rios"
    elif opc == 3:
        tpa = "Estanques"
    elif opc == 4:
        tpa = "Corrientes"
    elif opc == 5:
        tpa = "Aguas Subterraneas"
    elif opc == 6:
        tpa = "Llanuras inundables"
    elif opc == 7:
        tpa = "Cienagas"
    elif opc == 8:
        tpa = "Pantanos"
    elif opc == 9:
        tpa = "Tierras anegadas"
    elif opc == 10:
        tpa = "canales embalces"
    else:
        return "El dato ingresado supera la lista establecida o no es un dato valido"
    return tpa


# Inicializar la lista cargando los datos del archivo
cuerpos_de_agua = cargar_datos()


# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar cuerpo de agua")
    print("2. Mostrar cuerpos de agua")
    print("3. Contar cuerpos de agua con IRCA ≤ 35% (riesgo medio o inferior)")
    print("4. mostrar las claves primarias")
    print("5. salir")


def Menu_tipos():
    print("""
             Elija el tipo de cuerpo de agua en esta lista:
              1.Lagos
              2.Rios
              3.Estanques
              4.Corrientes
              5.Aguas Subterraneas
              6.Llanuras inundables
              7.Cienagas
              8.Pantanos
              9.Tierras anegadas
              10.canales embalces 
              """)


# Bucle principal
while True:
    # Mostrar el menú
    mostrar_menu()

    # Pedir al usuario una opción
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        # Agregar un nuevo cuerpo de agua
        nombre = input("Ingresa el nombre del cuerpo de agua: ")

        Menu_tipos()

        try:
            opc = int(input("Selecciona una opción (1-10):"))
            tipo_agua = opciones_tipos(opc)

            if "El dato ingresado" in tipo_agua:
                print(tipo_agua)

            else:
                print(f"Tipo de agua seleccionado: {tipo_agua}")

                irca = float(input("Ingresa el valor del IRCA (%): "))
                if 0 <= irca <= 100:

                    clave_primaria = random.randint(1, 999)
                    while any(c["clave primaria"] == clave_primaria for c in cuerpos_de_agua):
                        clave_primaria = random.randint(1, 999)

                    nivel_riesgo = clasificar_irca(irca)
                    cuerpo = {"clave primaria": clave_primaria,
                              "nombre": nombre,
                              "irca": irca,
                              "nivel_riesgo": nivel_riesgo,
                              "tipo de agua": tipo_agua}
                    cuerpos_de_agua.append(cuerpo)

                    # Guardar los datos actualizados en el archivo
                    guardar_datos(cuerpos_de_agua)
                    os.system('cls')
                    print("¡Cuerpo de agua agregado con éxito!")
                else:
                    print("El valor del IRCA debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingresa un valor numérico válido para el IRCA.")

    elif opcion == "2":
        # Mostrar los cuerpos de agua guardados
        if cuerpos_de_agua:
            print("\nCuerpos de agua guardados:")
            for i, cuerpo in enumerate(cuerpos_de_agua, start=1):
                print(f"{i}. {cuerpo['nombre']} - IRCA: {cuerpo['irca']}% (Riesgo: {cuerpo['nivel_riesgo']})")
        else:
            print("No hay cuerpos de agua guardados.")
    elif opcion == "3":
        # Contar cuerpos de agua con IRCA ≤ 35%
        cuerpos_bajos_medios = [
            cuerpo for cuerpo in cuerpos_de_agua if cuerpo["irca"] <= 35
        ]   
        print(f"Hay {len(cuerpos_bajos_medios)} cuerpos de agua con IRCA ≤ 35% (riesgo medio o inferior).")
        
    elif opcion == "4":
            if cuerpos_de_agua:
                print("\nCuerpos guardados e ID:")
            for i, cuerpo in enumerate(cuerpos_de_agua, start=1):
                print(f"{i}. {cuerpo.get('clave primaria', 'not id')} {cuerpo['nombre']} (Riesgo: {cuerpo['nivel_riesgo']})")
            else:
                print("No hay cuerpos de agua guardados.")
            
    elif opcion == "5":
        # Salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")