# Dashboard

## Setup development environment docker

### Clone the repository

```bash
git clone git@github.com:2023M8T2-Inteli/grupo1.git
```

and go to the project folder

```bash
cd grupo1/src/dashboard
```

### Get the environment variables (.env )

You can find the environment variables in the [env.example](./env.example) file, copy the file and rename it to `.env`

```bash
cp env.example .env
```

And fill the variables with the correct values

#### Install docker

You can find the installation instructions for your operating system here:

-   docker: https://docs.docker.com/get-docker/

Last tested version:

-   Docker version 24.0.7

#### Verify installations

```bash
docker --version
```

_🍀 Tip: Is recommended use the docker-desktop app to manage and monitor the containers_

#### Running the container

```bash
docker compose up
```

_🍀 Tip: If you want to run the container in the background, use the `-d` flag_

#### Using the docker-desktop

You can use the docker-desktop app to manage and monitor the containers.

#### For modifications in the code

the [dockerfile](./Dockerfile) is configured to run the container in development mode, so you can make changes in the code and the container will be updated automatically in the next start, and has the [docker-compose.yml](./docker-compose.yml) configured for start and connect to the container.
