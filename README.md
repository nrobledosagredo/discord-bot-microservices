# Discord bot with microservices and distributed architecture

![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

## Overview

A Discord bot developed as a demonstration of a distributed microservices architecture. It features birthday management, YouTube video search, and service communication via RabbitMQ.

## Features

- **Birthday management**: Query and register birthday dates via interactive Discord commands.
- **YouTube search**: Find and share YouTube video links directly within Discord.
- **Distributed architecture**: Decoupled services containerized with Docker, communicating via RabbitMQ.

## Prerequisites

* Docker
* Docker Compose
* Environment variables configured in a `.env` file:
    ```env
    DISCORD_TOKEN=<your-discord-token>
    DISCORD_GUILD=<your-guild-name>
    RABBITMQ_HOST=rabbitmq
    DATABASE_IP=birthday_database
    ```

## Setup

1. Create a `.env` file in the project's root directory with the required environment variables as shown above.

2. Run the following command to build and start the containers:

    ```bash
    docker-compose up --build
    ```

## Main commands

| Command               | Description                                       |
|-----------------------|---------------------------------------------------|
| `!birthday <name>`    | Query the birthday of a member.                   |
| `!add-birthday <data>`| Register a member's birthday.                     |
| `!search <keywords>`  | Search for a YouTube video and send the link.     |
