# Discord bot with microservices and distributed architecture

![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)

A Discord bot designed as a learning project to demonstrate the use of a distributed **microservices** architecture. It includes functionalities like birthday management, YouTube video search, and communication between services via RabbitMQ.

## Features

- **Birthday management**:
  - Query and register birthday dates.
  - Interactive commands in Discord.
  
- **YouTube search**:
  - Find videos and send links directly in Discord.

- **Distributed architecture**:
  - Decoupled services communicating through RabbitMQ.
  - Containerization with Docker for easy deployment.

## Requirements

- **Docker** and **Docker Compose**.
- Environment variables configured in a `.env` file:
   ```env
   DISCORD_TOKEN=<your-discord-token>
   DISCORD_GUILD=<your-guild-name>
   RABBITMQ_HOST=rabbitmq
   DATABASE_IP=birthday_database
   ```

## How to run

To deploy the project, use the following command:

```bash
docker-compose up --build
```

This will start the necessary containers, including the bot, services, and RabbitMQ.

## Main commands

| Command               | Description                                          |
|-----------------------|------------------------------------------------------|
| `!birthday <name>`    | Query the birthday of a member.                     |
| `!add-birthday <data>`| Register a member's birthday.                       |
| `!search <keywords>`  | Search for a YouTube video and send the link.       |
