# Usar Debian 10 (buster) como base
FROM python:3.11-slim-buster

# Establece un directorio de trabajo
WORKDIR /app

# Desactivar diálogos interactivos y definir variables de entorno necesarias
ENV DEBIAN_FRONTEND=noninteractive ACCEPT_EULA=Y

# Actualizar el sistema, instalar dependencias y limpiar todo en un solo RUN para optimizar las capas
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    unixodbc \
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
    gnupg && \ 
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Añadir las claves de Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Añadir el repositorio de Microsoft para Debian 10
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Actualizar y instalar los paquetes
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

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
