---
sidebar_position: 5
---

# Interface do Usuário

## Introdução
Nesta seção iremos discorrer sobre o workflow da aplicação web, bem como as tecnologias utilizadas e a arquitetura do projeto.

## Diagrama
Através do diagrama podemos compreender como se dá o fluxo de requisições para nossa interface, o usuário realiza uma requisição através do chatbot, verificamos a validade dessa requisição, ou seja, se ela apresenta os elementos necessários, um item contido no inventário do almoxarifado por exemplo. 

Dada a validade dessa requisição, adicionamos um novo item ao banco de dados e atualizamos a página principal que representa as requisições feitas para o chatbot através do Telegram ou Whatsapp.

Após essa atualização, espera-se uma resposta do robô sobre o status de sua tarefa baseado em três condições: Pendente, Aprovado ou Rejeitado. 

Por padrão sempre que uma requisição é realizada, ela recebe os status de pendente, até que o robô atinja o objetivo e faça uma requisição sinalizando o sucesso ou falha em atender o pedido, resultando nos estados aprovado e rejeitado, respectivamente.
Após esta atualização de status, é retornado para o usuário se sua requisição foi bem sucedida ou não.

<iframe width="800" height="450" src="https://whimsical.com/embed/6wP499ooBYKHKdHdMTzSkt"></iframe>

## Arquitetura do WebApp
A seguir, podemos visualizar a arquitetura do webapp de forma simplificada.

Podemos observar que o cadastro das informações fica a cargo do servidor, então sempre que uma requisição é realizada, a api coleta as informações do pedido e realiza seu cadastro no banco e renderiza esse novo item no frontend.

<iframe width="800" height="450" src="https://whimsical.com/embed/BdViTfHfviiAjqvM9uQFwR"></iframe>

## Demo
Abaixo podemos ver a demonstração dessa aplicação funcionando. Cabe ressaltar que a integração será realizada na sprint 5 e o chatbot será responsável por fazer as requisições para a API, de modo que possamos cadastrar novos itens. Por enquanto estaremos utilizando o insomnia para fins de demonstrar a integração da API em si. 

<iframe
    width="560"
    height="315"
    src="https://youtube.com/embed/wTsbxawsgzU"
    frameborder="0"
    allow="autoplay; encrypted-media"
    allowfullscreen>
</iframe>

## Tecnologias Utilizadas
Abaixo estão listadas as tecnologias utilizadas para concepção da ferramenta de modo tabular.

| Tecnologia     | Descrição                           |                                            |                                      |
| --------------- | ------------------------------------- | ----------------------------------------------- | 
| Django          | Framework web em python             | ![Django Icon](https://skillicons.dev/icons?i=django)          | 
| PostgreSQL      | Banco de dados estruturado (SQL)     | ![PostgreSQL Icon](https://skillicons.dev/icons?i=postgres)  | 
| Tailwind CSS    | Framework de CSS           | ![Tailwind CSS Icon](https://skillicons.dev/icons?i=tailwind)| 
| Flowbite        | Framework de CSS leve| ![Flowbite Icon](https://flowbite.com/images/logo.svg)      | 

### Como Rodar
Para fins de reprodução da interface, podemos seguir o seguinte passo a passo, tendo em vista que o usuário tem docker instalado em seu computador.

```bash
git clone https://github.com/2023M8T2-Inteli/grupo1.git
cd grupo1/src/plataform
docker compose up --build
```