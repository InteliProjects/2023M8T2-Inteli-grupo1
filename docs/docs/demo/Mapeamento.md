---
sidebar_position: 1
---

# Pacote de Mapeamento
Abaixo, podemos ver o pacote de mapeamento, desenvolvido durante a sprint 2. Para que esse pacote seja lançado e o usuário possa realizar a cartografia do espaço desejado, é necessário que o usuário tenha um desktop contendo Ubunto 18.0 ou superior, e que tenha instalado o ROS2 Humble.

Para fins de instalação, consulte a seção de [instalação](/docs/project-setup/Project-setup.md).

## Nós do pacote de mapeamento
O pacote de mapeamento é composto por 3 nós, sendo eles:
- Nó de mapeamento
- Nó de visualização

## Funcionamento do pacote de mapeamento
O pacote de mapeamento é responsável por realizar a cartografia do espaço desejado pelo usuário. Para isso, o usuário deve lançar o pacote de mapeamento, e em seguida, lançar o pacote de controle. O pacote de controle é responsável por controlar o robô, e o pacote de mapeamento é responsável por realizar a cartografia do espaço.

## Como rodar o pacote de mapeamento
Para rodar o pacote de mapeamento basta utilizar os comandos abaixo, enquanto estiver conectado ao robô via ssh:

```bash
cd src/ros2_ws
colcon build 
source install/setup.bash
ros2 launch mapper.launch.py
```

Após isso, iremos utilizar o teleop para controlar o robô. Para isso, basta utilizar o comando abaixo em um novo terminal:

```bash 
ros2 run turtlebot3_teleop teleop_keyboard
``` 

Abaixo podemos ver o pacote de mapeamento sendo lançado e o pacote de controle sendo lançado em seguida:

<iframe
  width="750"
  height="450"
  src="https://youtube.com/embed/0PME6sJjU3U"
  frameborder="0"
  allow="autoplay; encrypted-media"
  allowfullscreen>
</iframe>
