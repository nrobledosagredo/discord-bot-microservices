# Bot de Discord con microservicios y arquitectura distribuida

![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)

Este proyecto es un bot de Discord diseñado para demostrar el uso de una arquitectura distribuida basada en **microservicios**. Incluye funcionalidades como gestión de cumpleaños, búsqueda de videos en YouTube y comunicación entre servicios mediante RabbitMQ.

## Funcionalidades

- **Gestión de cumpleaños**:
  - Consulta y registro de fechas de cumpleaños.
  - Comandos interactivos en Discord.
  
- **Búsqueda en YouTube**:
  - Encuentra videos y envía enlaces directamente en Discord.

- **Arquitectura distribuida**:
  - Servicios desacoplados que se comunican mediante RabbitMQ.
  - Contenerización con Docker para facilitar el despliegue.

## Componentes

1. **Discord Listener**: Gestiona comandos y mensajes en Discord.
2. **Birthday Manager**: Administra la base de datos de cumpleaños.
3. **YouTube Service**: Procesa búsquedas de videos.
4. **RabbitMQ**: Provee la comunicación entre servicios.
5. **Base de datos MariaDB**: Almacena información de los cumpleaños.

## Requisitos

- **Docker** y **Docker Compose**.
- Variables de entorno configuradas en un archivo `.env`:
   ```env
   DISCORD_TOKEN=<tu-token-de-discord>
   DISCORD_GUILD=<nombre-de-tu-servidor>
   RABBITMQ_HOST=rabbitmq
   DATABASE_IP=birthday_database
   ```

## Ejecución

Para desplegar el proyecto, usa el siguiente comando:

```bash
docker-compose up --build
```

Esto levantará los contenedores necesarios, incluyendo el bot, los servicios y RabbitMQ.

## Comandos principales

| Comando                | Descripción                                           |
|------------------------|-------------------------------------------------------|
| `!birthday <nombre>`   | Consulta la fecha de cumpleaños de un miembro.        |
| `!add-birthday <datos>`| Registra el cumpleaños de un miembro.                 |
| `!search <palabras>`   | Busca un video en YouTube y envía el enlace.          |