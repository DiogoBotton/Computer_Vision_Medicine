## Scripts

Para rodar o docker-compose da API digite:

```bash
    docker-compose up -d --build
```

Para rodar o docker-compose com o RabbitMQ para a atividade "Ir Além" envolvendo ESP32 digite:

```bash
    docker-compose -f docker-compose-rabbitmq.yml up -d --build
```

Para rodar o docker-compose com a API WebSocket para se conectar ao RabbitMQ digite:

```bash
    docker-compose -f docker-compose-websocket.yml up -d --build
```