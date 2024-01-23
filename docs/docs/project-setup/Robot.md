---
sidebar_position: 2
---
# Inicialização dos pacotes do ros2

## Introdução

Este documento tem como objetivo explicar como inicializar o pacote do robô Jose Entregas. O robô possui 1 nó e dois launchers, sendo eles:

- **llmrc_robot**: Nó responsável por controlar o robô e receber os dados do chatbot.

- **mapper.launch.py**: Launcher que permite o usuário mapear um espaço com o robô.
  
- **chatbot.launch.py**: Launcher que permite o robô receber comandos do chatbot para ir até items específicos.

O usuário deve primeiramente seguir os passos em [Project Setup](./) para instalar o ROS2 e configurar o ambiente. Após isso, o usuário deve se direcionar para a pasta do workspace do ROS2:

```bash
cd  src/ros2_ws
```

Para construir o nó, execute o comando abaixo:

```bash
colcon build
```

Agora o usuário deve dar source no setup.bash do workspace e do ros:

```bash
source install/setup.bash
source ~/opt/ros/humble/setup.bash
```

## Execução do sistema

para executar o sistema, o usuário deve se direcionar a pasta dos launchers atualmente:

```bash
cd src/ros2_ws/src/jose_entregas/launch
```

### Mapper

Para executar o mapper, o usuário deve executar o comando abaixo:

```bash
ros2 launch mapper.launch.py
```

Ao rodar esse comando o sistema pedirá ao usuário para inputar o nome do mapa, após isso dois  processos serão executados:

- **RViz**: Ferramenta de visualização do ROS2.
- **xterm**: Terminal que permite o usuário controlar o robô com as teclas WASD.

Quando o usuário terminar de mapear o espaço, ele deve fechar o xterm com o comando `controlC`  após isso o mapa sera salvo automaticamente na pasta do pacote do robô.

### Chatbot

O launcher do chatbot tem como dependência o modelo de llm ([setup llm](./Llm))e nó do chatbot que se os passos descritos acima foram seguidos já deve estar buildado.Para executar o chatbot, o usuário deve executar o comando abaixo:

```bash
ros2 launch chatbot.launch.py
```

Ao rodar esse comando o sistema pedirá ao usuário para inputar o nome do mapa, após isso dois  processos serão executados:

- **RViz**: Ferramenta de visualização do ROS2.
- **xterm**: Terminal que permite o usuário escrever perguntas que serão interpretadas pelo llm e se necessário o robô irá se mover para o item desejado.
