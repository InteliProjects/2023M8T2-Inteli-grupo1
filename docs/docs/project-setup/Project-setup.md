---
sidebar_position: 0
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Instalação de dependências

Para utilizar o sistema, é necessário que o usuário instale as dependências do projeto nos dispositivos que serão utilizados e execute os comandos necessários para a execução do sistema. Sendo necessário acesso ao repositório do projeto, que pode ser encontrado no [GitHub](https://github.com/2023M8T2-Inteli/grupo1/), o computador que será utilizado como servidor, e ao robô [TurtleBot3](https://www.turtlebot.com/turtlebot3/).

## Pré-requisitos

Será necessário que o usuário tenha instalado em seu computador e ao robô alguns softwares para execução do sistema. É recomendado que o usuário tenha já instalado como sistema operacional o [Ubuntu 22.04 LTS Desktop](https://ubuntu.com/download/desktop) no servidor, e [Ubuntu 22.04 LTS Server](https://ubuntu.com/download/server) no [TurtleBot3](https://www.turtlebot.com/turtlebot3/), pois o sistema foi desenvolvido e testado nessa versão do sistema operacional Linux.

_:warning: **Atenção**: Os comandos a seguir são dependências do servidor e do robô, portanto, devem ser executados em ambos os dispositivos._

### Docker

O Docker é uma ferramenta que permite a execução de aplicações em ambientes isolados, chamados de containers. Para instalar o Docker, siga os passos abaixo:

#### Remoção de versões antigas e adição do repositório

<Tabs defaultValue="remove-docker" values={[
{label: 'Remover docker antigo', value: 'remove-docker'},
{label: 'Limpar configurações', value: 'clean-settings'},
{label: 'Adicionar repositório', value: 'adding-repository'}
]}>

<TabItem value="remove-docker">

```bash
sudo apt remove docker-desktop
```

</TabItem>

<TabItem value="clean-settings">

```bash
# Remove configurações do docker
rm -r $HOME/.docker/desktop

# Remove o binário do docker
sudo rm /usr/local/bin/com.docker.cli

# Remove todos os pacotes do docker
sudo apt purge docker-desktop
```

</TabItem>

<TabItem value="adding-repository">

```bash
# Adiciona a chave GPG oficial do Docker
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Adiciona o repositório do docker
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

</TabItem>
</Tabs>

#### Instalação do docker e configuração

<Tabs defaultValue="install-docker" values={[
{label: 'Instalar docker', value: 'install-docker'},
{label: 'Configurar permissão docker', value: 'config-docker'},
]}>

<TabItem value="install-docker">

```bash
# Instala o docker e suas dependências
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

</TabItem>

<TabItem value="config-docker">

```bash
# Cria o grupo docker
sudo groupadd docker

# Adiciona o usuário atual ao grupo docker
sudo usermod -aG docker $USER

# Ativa as mudanças no grupo docker para o usuário atual
newgrp docker
```

</TabItem>

</Tabs>

### Git

O Git é uma ferramenta de controle de versão de código fonte. Para instalar o Git, siga os passos abaixo:

<Tabs defaultValue="install-git" values={[
{label: 'Instalar git', value: 'install-git'},
{label: 'Clonar repositório', value: 'clone-repository'},
]}>

<TabItem value="install-git">

```bash
# Instala o git
sudo apt install git
```

</TabItem>

<TabItem value="clone-repository">

```bash
# Clona o repositório
git clone git@github.com:2023M8T2-Inteli/grupo1.git
```

</TabItem>

</Tabs>

## Execução do sistema

As instruções a seguir são para execução do sistema no servidor e no robô.

### Entrar na pasta do código fonte

O código fonte do projeto contém duas principais pastas, uma para o servidor e outra para o robô. Para executar o sistema, é necessário entrar na pasta do código fonte do dispositivo que será utilizado.

<Tabs defaultValue="server" values={[
{label: 'Servidor', value: 'server'},
{label: 'TurtleBot', value: 'turtlebot'},
]}>

<TabItem value="server">

```bash
# Entra na pasta para execução do servidor
cd src/server
```

</TabItem>

<TabItem value="turtlebot">

```bash
# Entra na pasta para execução do robô
cd src/turtlebot
```

</TabItem>

</Tabs>

### Executar o container

Para executar o container, execute o comando abaixo em cada dispositivo:

```bash
# Executa o container
docker compose up
```

_:four_leaf_clover: **Dica**: Para executar o container em segundo plano, execute o comando `docker compose up -d`. Caso queira parar a execução do container, execute o comando `docker compose down`._
