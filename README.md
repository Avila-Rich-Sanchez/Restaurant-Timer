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

### Pasos de instalación

1. Clona el repositorio
```bash
git clone https://github.com/Avila-Rich-Sanchez/Restaurant-Timer.git
cd Restaurant-Timer
