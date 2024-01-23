---
sidebar_position: 1
---

# Construção do modelo de LLM

Este documento tem como objetivo explicar como criar o modelo de processamento de linguagem natural (llm) utilizado pelo sistema para entender os outputs do usuário.

## Setup

Você precisará instalar o pacote ollama:

``` bash
curl https://ollama.ai/install.sh | sh
```

Você também precisará dar permissão ao script para executar:

``` bash
chmod -R o+rx .
```

Depois disso, você pode executar o seguinte comando para criar o modelo:

``` bash
ollama create joseentregas -f Modelfile
```

## Utilização

Você pode usar o modelo executando o seguinte comando:

``` bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "joseentregas",
  "prompt":"ensira sua pergunta aqui",
  "stream": false
}'
```

Só é necessário alterar o prompt para a pergunta que você deseja fazer ao sistema. Porém em geral o modelo sera utilizado pelo resto do sistema sem necessidade de interação direta do usuário.