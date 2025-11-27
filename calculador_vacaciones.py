# calculador_vacaciones.py
print("======================================")
print("Calculador de derecho de vacaciones")
print("======================================\n")

def obtener_dias_vacaciones(key, años):
    # tabla: key -> (dias_0_1, dias_2_5, dias_6_mas)
    tabla = {
        1: (6, 14, 20),   # Atención al cliente
        2: (7, 15, 22),   # Logística
        3: (10, 20, 30),  # Gerencia
    }
    if key not in tabla:
        return None
    if años < 0:
        return "años inválidos"
    d0_1, d2_5, d6 = tabla[key]
    if años in (0, 1):
        return d0_1
    elif 2 <= años < 6:
        return d2_5
    else:
        return d6

def pedir_entero(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("Introduce un número entero válido.")

name = input("Introduce tu nombre: ").strip()
print(f"\nHola {name}\n")

key = pedir_entero("Introduce tu numero de clave (1-Atencion, 2-Logistica, 3-Gerencia): ")

dias = obtener_dias_vacaciones(key, pedir_entero(f"{name}, introduce los años que llevas en el puesto: "))

if dias is None:
    print("\nLa clave introducida no existe, vuelve a intentar.")
elif dias == "años inválidos":
    print("\nHas introducido años inválidos. Revisa el dato.")
else:
    print(f"\nTus vacaciones permitidas son {dias} dias al año, disfrútalas {name}.\n")
    print("Úsalas cuando quieras, gracias por formar parte de la empresa :D")
