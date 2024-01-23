---
sidebar_position: 4
---

# Estrutura de Dados & Design Patterns

Para o projeto, utilizaremos Estruturas de Dados e Design Patterns que auxiliaram na construção e manutenção escalável apoiando-se em boas práticas. A princípio, temos hipóteses iniciais sobre quais serão os elementos implementados no projeto.

## Estrutura de Dados

### Filas

Em um primeiro momento, utilizaremos algoritmos de navegação para realizar as rotinas do robô. Nesse sentido, filas seriam de grande utilidade para armazenar pontos de destino, pois garantem que os pontos de destino sejam executados na ordem correta, respeitando a sequência de tarefas planejadas.

### Tabelas

A princípio, será utilizado um banco de dados relacional, PostgreSQL. No banco de dados serão criadas tabelas para armazenar informações do robô, como por exemplo, a posição atual do robô, a posição de destino, a posição de origem, etc, além disso, o sistema de gerenciamento do almoxarifado utilizará uma tabela deste banco para verificar a disponibilidade de peças, baixa das peças solicitadas, etc.

## Design Patterns

### Singleton

O _Singleton_ é um padrão de design que garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a essa instância. No contexto do ROS (Robot Operating System), usar o Singleton para o ROS Master é uma escolha comum, pois o ROS Master é um componente central que gerencia a comunicação entre nós em um sistema ROS.

### Observer

O _Observer_ é um padrão de design que consiste em dois tipos de objetos; _Publishers_ e _Subscribers_. O primeiro possui um _Subject_, que é basicamente alguma informação de interesse dos Subscribers. Sempre que o _Subject_ muda de estado, é papel de _Publisher_ notificar todos os _Subscribers_ inscritos neste _Subject_, da mudança desse estado. 
