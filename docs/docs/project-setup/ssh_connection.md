---
sidebar_position: 3
---

# Conexão via SSH 

## Introdução

Nesta seção você compreenderá como é possível utilizar o ROS2 no robô, localmente, através de uma conexão SSH.

1. Para tal, abriremos um terminal no computador e nos conectaremos ao robô via SSH. Neste terminal, executaremos os comandos abaixo para tal.

```bash
ssh grupo1@grupo1.local
# A senha que deverá ser digitada quando solicitada é: grupo1
```

Em caso de erro, sugerimos ao usuário testar o comando sem a terminação ".local" e, caso o erro persista, reiniciar o robô.

2. Após o login, o usuário deverá executar os comandos abaixo para iniciar o ROS2 no robô.

```bash
ros2 launch turtlebot3_bringup turtlebot3_robot.launch.py use_sim_time:=false
```
Este comando permitira que o controle do robô seja feito localmente, através do computador, fazendo a comunicação entre tópicos do ROS2 no robô e no computador. 

<iframe
    width="560"
    height="315"
    src="https://youtube.com/embed/zIDk3Rm953k"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen>
</iframe>

3. Em um novo terminal, o usuário deverá executar os comandos abaixo para iniciar o ROS2 no computador.

```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

<iframe
    width="560"
    height="315"
    src="https://youtube.com/embed/RmAy1_IhhBI"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen>
</iframe>