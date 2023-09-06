#!/bin/bash

# Añadir claves y repositorios de Microsoft para el ODBC Driver
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Actualizar e instalar el ODBC Driver 17 for SQL Server
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Instalar dependencias de Python
pip install --no-cache-dir -r requirements.txt
pip install pymssql