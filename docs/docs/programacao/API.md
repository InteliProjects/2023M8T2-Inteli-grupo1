---
sidebar_position: 6
---

# API

## Visão Geral

A API do Projeto é uma interface abrangente projetada para gerenciar logs, números autorizados e itens em uma aplicação baseada em Django. Esta API inclui endpoints para criar, recuperar, atualizar e deletar diversos recursos, além de uma camada de visualização sofisticada para apresentar dados de forma eficaz.

## Configuração de URL

### URL Base

A URL base para acessar o sistema é `http://<endereço-do-servidor>/`

### Endpoints

#### Visualizações

-   `/` (Home View) - Página principal da aplicação.
-   `logs/` (Logs View) - Página de logs do banco de dados.
-   `numbers/` (Numbers View) - Página de números autorizados do sistema.
-   `items/` (Items View) - Página de lista dos itens do banco de dados.

### Endpoints da API

### Logs

-   **POST** `api/logs/create/` - Criar uma nova entrada de log.
    Estrutura do JSON:

```json
{
	"requester_name": "Nome do Solicitante",
	"requester_number": "11999999999",
	"item": "nome do item",
	"quantity": 1,
	"category": "categoria do item",
	"status": 0
}
```

O status pode ser 0 (pendente), 1 (aprovado) ou 2 (rejeitado).
É retornado o código 201 (Created) em caso de sucesso junto com o JSON da entrada criada, caso contrário, é retornado o código 400 (Bad Request) com o JSON do erro.

---

-   **POST** `api/logs/status/` - Atualizar o status de uma entrada de log.

```json
{
	"id": 1,
	"status": 1
}
```

O status pode ser 0 (pendente), 1 (aprovado) ou 2 (rejeitado).
É retornado o código 200 (OK), caso contrário, caso o id não exista, é retornado o código 404 (Not Found), caso o status não seja válido, é retornado o código 400 (Bad Request).

---

-   **GET**`api/logs/csv/` - Obter logs em formato CSV.

Retorna o código 200 (OK) junto com o arquivo CSV com os logs em caso de sucesso, caso contrário, é retornado o código 400 (Bad Request).

### Números Autorizados

-   **POST** `api/number/create/` - Criar um novo número autorizado.

```json
{
	"number": "11999999999",
	"name": "Nome do Solicitante"
}
```

Retorna o código 201 (Created) em caso de sucesso junto com o JSON do número criado, caso contrário, é retornado o código 400 (Bad Request) com o JSON do erro.

---

-   **GET** `api/number/get/` - Recuperar todos os números autorizados

Retorna o código 200 (OK) em caso de sucesso junto com o JSON dos números autorizados em formato de lista, caso contrário, é retornado o código 400 (Bad Request) com o JSON do erro.

---

-   **DELETE** `api/number/delete/` - Deletar um número autorizado.

```json
{
	"id": 1
}
```

Retorna o código 200 (OK) em caso de sucesso na exclusão do número, caso o número não exista, é retornado o código 404 (Not Found), caso contrário, é retornado o código 400 (Bad Request) com o JSON do erro.

### Itens

-   **POST** `api/item/create/` - Criar um novo item.

```json
{
	"item": "Nome do Item",
	"x": 0.0,
	"y": 0.0,
	"z": 0.0,
	"image_url": "www.url.com/image.png"
}
```

Retorna o código 201 (Created) em caso de sucesso junto com o JSON do item criado, caso contrário, é retornado o código 400 (Bad Request) com o JSON do erro.

-   **GET** `api/item/get/` - Recuperar todos os itens.

Retorna o código 200 (OK) em caso de sucesso junto com o JSON dos itens em formato de lista, caso contrário, é retornado o código 400 (Bad Request) com o JSON do erro.

-   **DELETE** `api/item/delete/` - Deletar um item.

```json
{
	"id": 1
}
```

Retorna o código 200 (OK) em caso de sucesso na exclusão do item, caso o item não exista, é retornado o código 404 (Not Found), caso contrário, é retornado o código 400 (Bad Request) com o JSON do erro.
