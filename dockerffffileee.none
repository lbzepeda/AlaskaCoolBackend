# Usar Debian 10 (buster) como base
FROM python:3.11-slim-buster

# Establece un directorio de trabajo
WORKDIR /app

# Actualizar el sistema
RUN apt-get update
RUN apt-get upgrade -y

# Instalar dependencias básicas
RUN apt-get install -y unixodbc \
    unixodbc-dev \
    freetds-dev \
    gcc \
    g++ \
    python3-dev \
    libgssapi-krb5-2 \
    libkrb5-3 \
    libkrb5-dev \
    libssl-dev \
    libcrypto++-dev \
    krb5-user \
    krb5-config \
    curl \
    apt-transport-https \
    gnupg

# Agregar las claves y repositorios de Microsoft para ODBC
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Instalar apt-transport-https y limpiar cache
RUN apt-get install -y apt-transport-https
RUN apt-get clean
RUN apt-get update

# Instalar msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Limpieza final
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiar archivos necesarios y código al contenedor
COPY requirements.txt .
COPY setup.sh .
COPY . .

# Ejecutar script para configurar el entorno
RUN ./setup.sh

# Exponer el puerto 8000
EXPOSE 8000

# Ejecutar tu aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
