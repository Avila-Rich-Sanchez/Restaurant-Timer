# 🍔 Restaurant Timer - Sistema de Gestión de Inventario

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow.svg)

**Restaurant Timer** es un sistema backend de gestión de inventario diseñado específicamente para restaurantes de hamburguesas. Permite controlar el stock de ingredientes, procesar pedidos de manera automática, descontar ingredientes del inventario y generar alertas de compra cuando los productos están por agotarse.

El sistema trabaja con dos archivos principales:
- `recetas.json` - Contiene las recetas de cada tipo de hamburguesa
- Base de datos `.txt` - Almacena el inventario actual del restaurante

## Características

- Procesamiento de pedidos - Verifica disponibilidad de ingredientes y descuenta automáticamente del stock
- Control de inventario - Visualización en tiempo real del stock disponible
- Alertas inteligentes - Notifica cuando los ingredientes están bajos (< 5 unidades)
- Lista de compras automática - Genera automáticamente qué ingredientes necesitan reabastecimiento
- Interfaz por consola - Menú intuitivo y fácil de usar
- Persistencia de datos - El inventario se mantiene durante la sesión de trabajo

## Instalación

### Requisitos previos
- Python 3.x instalado en tu sistema
- Git (opcional, para clonar el repositorio)

## Estructura de los archivos

```bash
Restaurant-Timer/
│
├── app.py                    # Archivo principal del sistema
├── Inventario/
│   └── recetas.json         # Base de datos de recetas
|   └── inventario.txt 
└── README.md                # Este archivo
```
## Formato del JSON

### Ejemplo
```bash
{
  "Clásica": {
    "pan": 2,
    "carne": 1,
    "lechuga": 1,
    "tomate": 1
  },
  "Doble Queso": {
    "pan": 2,
    "carne": 2,
    "queso": 2,
    "tocino": 1
  }
}
```
## Formato del TXT

### Ejemplo
```bash
Producto:Pan|Categoría:Panes|Stock:50
Producto:Carne|Categoría:Proteínas|Stock:30
Producto:Lechuga|Categoría:Verduras|Stock:12
```
## Ejemplo de Uso

```bash
--- SISTEMA DE GESTIÓN (BACKEND) ---
Por favor, selecciona el archivo de base de datos en la ventana emergente...

Menu:
1. Hacer pedido
2. Ver inventario
3. Salir
Ingresa el numero de la opcion: 1

1. Hamburguesa Clásica.
2. Hamburguesa Doble Queso.
Ingresa el numero de la hamburguesa: 1

Ingredientes suficientes.
Ingredientes descontados: {'pan': 2, 'carne': 1, 'lechuga': 1, 'tomate': 1}. 
Te quedan 3 de pan. Mejor compra antes de que se acaben.
```
### Pasos de instalación

1. Clona el repositorio
```bash
git clone https://github.com/Avila-Rich-Sanchez/Restaurant-Timer.git
cd Restaurant-Timer
