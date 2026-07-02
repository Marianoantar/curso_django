#!/bin/bash

VENV_DIR="env"
CARPETA_PROYECTO="tienda_videojuegos"

echo "🚀 Iniciando el entorno de desarrollo..."

# 1. Verificar si el entorno virtual existe
if [ -d "$VENV_DIR" ]; then
    echo "📦 Activando el entorno virtual ($VENV_DIR)..."
    source "$VENV_DIR/bin/activate"
else
    echo "❌ Error: No se encontró la carpeta del entorno virtual '$VENV_DIR'."
    echo "Asegurate de estar en la raíz del proyecto o edita el script con el nombre correcto."
    exit 1
fi

# 2. Verificar si existe manage.py antes de lanzar Django
cd $CARPETA_PROYECTO || { echo "❌ Error: No se pudo cambiar al directorio '$CARPETA_PROYECTO'."; deactivate; exit 1; } 

if [ -f "manage.py" ]; then
    echo "🖥️  Lanzando el servidor de desarrollo de Django..."
    echo "------------------------------------------------"
    python manage.py runserver
else
    echo "❌ Error: No se encontró el archivo 'manage.py' en este directorio."
    deactivate
    exit 1
fi