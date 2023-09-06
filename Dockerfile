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
    krb5-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copia el archivo requirements.txt (si tienes uno) y tu código al contenedor
COPY requirements.txt .
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymssql

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta tu aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
