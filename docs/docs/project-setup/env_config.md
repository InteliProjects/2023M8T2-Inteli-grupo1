# Criação de um arquivo de variáveis de ambiente

Para que as features de STT e TTS funcionem corretamente, bem como o funcionamento da interface de usuário, deve-se primeiro configurar o arquivo de ambiente. Aqui estarão presentes as chaves secretas que serão utilizadas no projeto.

:::note

É necessário uma chave de utilização da API a fim de rodar a solução.

:::


Crie um arquivo .env. Um template pode ser encontrado no repositório oficial do projeto. 

```bash
cp env.example .env
```

 Em seguida e preencha os as variáveis com os valores corretos. Um exemplo abaixo:

- OPENAI_API_KEY: Chave de API da OPENAI
- DJANGO_SECRET_KEY: Chave secreta para rodar a aplicação Web
- KEY: Chave do bot do telegram
- BOT_ID: Número do bot do WhatsApp

```.env
OPENAI_API_KEY="chave-da-api-aqui"
DJANGO_SECRET_KEY="chave-secreta-aqui"
TELEGRAM_KEY="chave-do-bot-telegram-aqui"
WHATSAPP_BOT_KEY="chave-do-whatsapp-aqui"
```

:::warning

Tome cuidado para não tornar as chaves públicas! Por padrão, o arquivo .env não é rastreado no controle de versão do repositório, mas certifique-se de mante-las protegida.

:::

