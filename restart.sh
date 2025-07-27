#!/bin/bash

# Script para reiniciar los contenedores después de realizar cambios

# Crear directorios necesarios
echo "Creando directorios necesarios..."
mkdir -p pdfs result cache uploads

echo "Deteniendo y eliminando contenedores antiguos..."
docker compose down
docker rm -f ocr-pymupdf 2>/dev/null || true

echo "Limpieza de sistema..."
docker system prune --all --volumes --force

echo "Reconstruyendo imágenes..."
docker compose build

echo "Iniciando contenedores..."
docker compose up --detach

echo "Esperando a que los contenedores estén listos..."
sleep 5

echo "Estado de los contenedores:"
docker ps -a | grep ocr-pymupdf

echo "Iniciando modo interactivo..."
docker compose exec -T ocr-pymupdf python -m src.main --mode cli

