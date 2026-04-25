import json
import os
from tkinter import filedialog, Tk
import time

RELATIVE_PATH = os.path.dirname(os.path.abspath(__file__))
path_json = os.path.join(RELATIVE_PATH, "Inventario", "recetas.json")

with open(path_json, "r", encoding="utf-8") as file:
    data = json.load(file)

# Esto oculta la ventana principal de Tkinter
root = Tk()
root.withdraw()

print("--- SISTEMA DE GESTIÓN (BACKEND) ---")
print("Por favor, selecciona el archivo de base de datos en la ventana emergente...")

# Abre el explorador de archivos y guarda la ruta
ruta_txt = filedialog.askopenfilename(
    title="Seleccionar Base de Datos",
    filetypes=[("Archivos de Base de Datos", "*.txt"), ("Todos los archivos", "*.*")]
)

stock = {}

if ruta_txt:
    with open(ruta_txt, "r", encoding="utf-8") as file:
        for line in file:
            if "|" in line:
                # 1. Separamos por la barra
                parts = line.split("|")
                
                # 2. Extraemos el valor después de los dos puntos ":" y limpiamos espacios
                product = parts[0].split(":")[1].strip()
                category = parts[1].split(":")[1].strip()
                stock_product = int(parts[2].split(":")[1].strip())

                data_new = {product: stock_product}
                stock.update(data_new)

        print("Leidos los datos exitosamente!")
else:
    print("No has seleccionado ningun archivo.")

def product_count(recipe):
    for key_r, value_r in data[recipe].items():
        for key_s, value_s in stock.items():
            if key_r.lower() == key_s.lower():
                if value_s < value_r:
                    return f"{key_s} insuficiente. Necesitas {value_r} y tienes {value_s}"
    return True

def plate_production(recipe):
    list_ingredients = {}
    for key_r, value_r in data[recipe].items():
        for key_s, value_s in stock.items():
            if key_r.lower() == key_s.lower():
                value_s -= value_r
                if value_s < 5:
                    msg = f"Te quedan {value_s} de {key_s}. Mejor compra antes de que se acaben."
                elif value_s == 0:
                    msg = f"No te queda mas {key_s}"
                stock[key_s] = value_s
                ingredient = {key_r: value_r}
                list_ingredients.update(ingredient)
    
    return f"Ingredientes descontados: {list_ingredients}. \n{msg}"

def list_buy():
    list_ingredients_buy = {}
    for k, v in stock.items():
        if v < 5:
            new_ingredient_buy = {k: v}
            list_ingredients_buy.update(new_ingredient_buy)
    return list_ingredients_buy


flag = True

while flag:
    print("Menu:")
    print("1. Hacer pedido.")
    print("2. Ver inventario.")
    print("3. Salir.")

    try:
        select_option = int(input("Ingresa el numero de la opcion: "))
    except ValueError:
        print("Debes seleccionar el numero de la opcion.")
        continue

    if select_option == 1:
        print("Menu:")
        number_of_recipes = 1
        recipes = {}
        try:
                for i, product in enumerate(data.keys()):
                    print(f"{i+1}. Hamburguesa {product}.")
                    new_recipe = {i+1: product}
                    recipes.update(new_recipe)
                    number_of_recipes += 1
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {path_json}")
            continue
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            continue

        select_recipe = int(input("Ingresa el numero de la hamburguesa: "))

        if not select_recipe in range(1, number_of_recipes):
            print("Opción inválida.")
            time.sleep(3)
            os.system("cls")
            continue

        for key, value in recipes.items():
            if key == select_recipe:
                value = value
                result = product_count(value)
                break
        
        if result is True:
            print("Ingredientes suficientes.")
            result_production = plate_production(value)
            print(result_production)
        elif "insuficiente" in result:
            print(result)

    elif select_option == 2:
        print("Inventario:")
        for key, value in stock.items():
            print(f"- {key} -> {value}")
        list_buy_ingredients = list_buy()
        print("Lista de ingredientes para comprar:")
        for k,v in list_buy_ingredients.items():
            print(f"- {k} Cantidad en stock {v}")
    elif select_option == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion Invalida.")