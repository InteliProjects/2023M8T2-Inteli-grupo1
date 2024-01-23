---
sidebar_position: 2
---

# Arquitetura da Solução

## Introdução

Para esse projeto, foram propostas duas arquiteturas de solução, portanto, serão apresentadas as duas versões nesse documento, justificando as suas alterações. A mudança da arquitetura tem em vista uma maior adequação que otimize a experiência do usuário, além de trazer uma maior viabilidade de implementação.

## Arquitetura Antiga

Essa arquitetura possui 3 partes principais: Aplicação Electron, Backend e Robô de Serviço.

![img alt](/img/arquitetura_antiga.png)


### Aplicação Electron

A Aplicação Electron é um software de desktop que permite aos usuários interagirem com um robô por meio de uma interface amigável através de requisições. Neste contexto, os usuários podem se comunicar usando comandos de voz, capturados por um microfone (Speech To Text), ou inserindo texto diretamente no computador do almoxarifado. O sistema também possui a capacidade de converter o texto inserido em fala (Text To Speech), facilitando assim a interação. Além disso, a aplicação se conecta a um servidor backend para listar os itens disponíveis e manter um registro das peças retiradas.

### Backend

O Backend compreende um banco de dados (ainda a ser definido) e uma API implementada em FASTAPI, que oferece rotas de acesso aos itens e ao sistema LLM. O LLM, por sua vez, está conectado ao robô e fornece instruções sobre quais peças devem ser retiradas.

### Robô de Serviço

O Robô de Serviço recebe instruções do Backend por meio de tópicos no ROS (Robot Operating System). Com base nessas instruções, o robô executa rotinas de navegação para recuperar as peças necessárias. Ele mantém um registro para análises posteriores e controle de falhas. Além disso, há uma ideia adicional de disponibilizar um servidor HTTP, permitindo aos usuários interagir diretamente com o robô durante suas operações através de uma aplicação Web.

## Arquitetura Nova

Essa arquitetura possui 3 partes principais: Robô de Serviço, Arquitetura Web e LLM(Large Language Model). Todas as partes da arquitetura foram pensadas para serem conteinerizadas, permitindo assim uma maior facilidade de deploy e manutenção. Para isso, foi utilizado o Docker.

### Robô de Serviço

![img alt](/img/arquitetura_turtlebot.png)

O robô utilizado para essa arquitetura é o Turtlebot3, portando o sistema operacional Ubuntu 22.04. A partir disso, foi utilizado o ROS(Robot Operating System) para a comunicação entre o robô e o restante de nossa arquitetura. Para a movimentação, foi utilizado o Navigation2, que é um pacote do ROS que permite a movimentação do robô de forma autônoma. Para os scripts de navegação, foi utilizada a linguagem Python.

### Arquitetura Web

![img alt](/img/arquitetura_web.png)

Para a web, foi utilizado o framework Django, que é um framework web de alto nível escrito em Python. O Django permite a criação de aplicações web de forma rápida e limpa, além de possuir uma grande comunidade e ser bem documentado. Para o banco de dados, foi utilizado o PostgreSQL, que é um sistema gerenciador de banco de dados objeto relacional. O PostgreSQL é um dos bancos de dados mais utilizados no mundo, além de ser open source e possuir uma grande comunidade. Para o frontend, foi utilizado o Tailwind CSS, além de Flowbite, que é um framework de UI para o Tailwind CSS.

### LLM(Large Language Model)

![img alt](/img/arquitetura_llm.png)

O LLM foi construído partindo de duas principais aplicações de mensageria: Utilizando o Whatsapp-web.js, que consiste em um pacote Node.js que permite a utilização do Whatsapp Web através de uma API, e também a partir da Telegram API, que consiste em uma interface para o controle de um bot no Telegram. A partir disso, foi utilizado o Whisper da OpenAI, que é responsável pela transcrição de áudios para textos. Em seguida, foi utilizado a API da OpenAI para a interpretação da mensagem do usuário e geração de resposta, assim como a transformação da resposta para o formato de áudio.