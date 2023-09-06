FROM python:3.11-slim

# Establece un directorio de trabajo
WORKDIR /app

# Actualizar el sistema e instalar dependencias necesarias
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
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
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instala el ODBC Driver 17 para SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Copia el archivo requirements.txt, setup.sh y tu código al contenedor
COPY requirements.txt .
COPY setup.sh .
COPY . .

# Ejecuta el script para configurar el entorno
RUN ./setup.sh

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta tu aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]