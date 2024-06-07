def opciones():
    print(f"""\n
╔ Menu de Gestion de Empleados ══╗
╠════════════════════════════════╣
║1. Lista de empleados.          ║
║2. Alta un empleado.            ║
║3. Baja un empleado.            ║
║4. Actualizar el domicilio.     ║
║5. Salir del sistema.           ║
╚════════════════════════════════╝
""")
    opcion = input("Ingrese la opcion deseada: ")
    return opcion

def listar_empleados(empleados):
    print("\nLISTA DE EMPLEADOS")
    print(f"{"╔"}{"═"*60}{"╗"}")
    print(f"{"║"}{"Legajo":<8}{"Apellido y nombre":<20}{"DNI":<10}{"Domicilio":<22}{"║"}")
    print(f"{"╠"}{"═"*60}{"╣"}")
    for empleado in empleados:
        print(f"{"║"}{empleado["legajo"]:<7} {empleado["apellido_nombre"]:<21} {empleado["dni"]:<10}{empleado["domicilio"]:<20}{"║"}")
    print(f"{"╚"}{"═"*60}{"╝"}")

def alta_empleados(empleados):
    print("\nALTA DE EMPLEADOS")
    legajo = input("Ingrese el legajo: ")
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    apellido_nombre = f"{apellido}, {nombre}"
    dni = input("Ingrese dni: ")
    domicilio = input("Ingrese el domicilio: ")
    nuevo_empleado = {
        "legajo": legajo, 
        "apellido_nombre": apellido_nombre,
        "dni": dni,
        "domicilio": domicilio
        }
    empleados.append(nuevo_empleado)
    print("Empleado agregado correctamente")

def baja_empleados(empleados):
    print("\nBAJA DE EMPLEADOS")
    legajo = input("Ingrese el legajo del empleado a eliminar: ")
    for empleado in empleados:
        if empleado["legajo"] == legajo:
            empleados.remove(empleado)
            print(f"Empleado {empleado["apellido_nombre"]} eliminado correctamente")
            return
    print("Empleado no encontrado...")

def actualizar_domicilio(empleados):
    legajo = input("Ingrese el legajo del empleado a actualizar: ")
    for empleado in empleados:
        if empleado["legajo"] == legajo:
            calle = input("Ingrese la nueva calle: ")
            numero = input("Ingrese la numeración: ")
            domicilio = f"{calle} {numero}"
            empleado["domicilio"] = domicilio
            return
    print("Empleado no encontrado...")



def main():
    empleados = [
        {
            "legajo": "1",
            "apellido_nombre": "Perez, Juan",
            "dni": "33556699",
            "domicilio": "Calle viva 1234",
            },
        {
            "legajo": "2",
            "apellido_nombre": "Juanita, Antonia",
            "dni": "39684128",
            "domicilio": "Avenida España 113",
            },
        {
            "legajo": "3",
            "apellido_nombre": "Dante, Alvarez",
            "dni": "7554123",
            "domicilio": "Calle Olazabal 3211",
            },
        {
            "legajo": "4",
            "apellido_nombre": "Esperanza, Muypoca",
            "dni": "5533474",
            "domicilio": "Los Receros 3251",
            },
        {
            "legajo": "5",
            "apellido_nombre": "Juan Manuel, Nidea",
            "dni": "21552697",
            "domicilio": "Av. Rivadavia 8899",
            },
        ]
    while True:
        opcion= opciones()
        #menu
        match opcion:
            case "1":
                listar_empleados(empleados)
            case "2":
                alta_empleados(empleados)
            case "3":
                baja_empleados(empleados)
            case "4":
                actualizar_domicilio(empleados)
            case "5":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")


main()
