# Practica 2 - Gabriel
# Condiciones, ciclos y funciones

def clasificar_edad(edad):
    if edad < 0:
        return "Edad inválida"
    elif edad < 12:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

edades = [3, 15, 18, 25, 67]

for e in edades:
    categoria = clasificar_edad(e)
    print(f"Edad: {e} → {categoria}")
