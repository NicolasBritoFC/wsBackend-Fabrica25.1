# Usa a imagem oficial do Python
FROM python:3.11

# Define o diretório de trabalho
WORKDIR /tradutor

# Instala dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia APENAS o arquivo de dependências primeiro (para melhor cacheamento)
COPY requirements.txt .
# Atualiza pip e instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instala as dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto para dentro do container
COPY . /tradutor/

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000","--workers","4","meu_projeto.wsgi:application"]