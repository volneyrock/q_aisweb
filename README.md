# Aplicativo Flask que mostra informações sobre aeródromos

Este é um exemplo de um aplicativo Flask executado em um contêiner Docker.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu sistema:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Executando o Aplicativo

Siga estas etapas para executar o aplicativo em um contêiner Docker:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/volneyrock/q_aisweb.git

2. **Construa a imagem Docker:**

   ```bash
   docker build -t qipu-web:latest .

3. **Execute o aplicativo em um contêiner Docker:**

   ```bash
   docker run -d -p 5000:5000 qipu-web
   ```

- **Se preferir usar o docker compose:**

   ```bash
   docker-compose up -d
   ```

- Agora, seu aplicativo Flask estará em execução e será acessível em http://localhost:5000.
