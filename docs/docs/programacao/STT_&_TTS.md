---
sidebar_position: 5
---

# STT & TTS

A incorporação das tecnologias de Reconhecimento de Fala (STT - Speech-To-Text) e Síntese de Fala (TTS - Text-To-Speech) foi estrategicamente implementada para ampliar a versatilidade das respostas oferecidas por nossa solução. No contexto da acessibilidade, é crucial que a solução seja capaz de atender ao maior número possível de usuários. A inclusão da capacidade de interação por meio de comandos e respostas por voz enriquece significativamente a experiência do usuário, garantindo uma ampla gama de possibilidades de uso.

## STT

O STT foi utilizado para permitir que usuários pudessem mandar comandos por áudio e receber a resposta do modelo da mesma forma.

A classe abaixo refere-se à classe contruída para a utilização do STT no projeto:

```python
class STT:
    def __init__(self, filename=None):
        self.filename = filename
        self.audio_file = open(self.filename, "rb")

    def transcribe(self):
        if self.filename is not None:
            transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=self.audio_file, 
            response_format="text"
            )
            return transcript
```

### Métodos

- ____init____: O contrutor recebe _filename_, o qual é o arquivo que será aberto para obtenção do conteúdo de áudio.
- __transcribe__: Utiliza a API da OpenAI para fazer a transcrição do áudio em texto.

## TTS

O TTS foi empregado para devolver respostas de voz ao cliente a partir daquelas geradas pelo LLM.

A classe abaixo refere-se a classe construída para a utilização do TTS no projeto.

### Métodos

- ____init____: O construtor possui dois argumentos iniciais: _filename_ e _text_, que podem ser usados para passar o nome de um arquivo ou o texto diretamente à classe
- __transcript__: A partir do arquivo ou do texto passados, extrai a informação que deve ser convertida em áudio.
- __generate_audio__: A partir do texto extraído, utiliza a API da OpenAI para fazer a conversão para áudio e transferir o conteúdo para um arquivo .mp3.
- __play__: Utiliza a biblioteca playsound para executar o arquivo de áudio gerado.

```python
class TTS:
    def __init__(self, filename=None, text=None):
        self.filename = filename
        self.text = text
    
    def transcript(self):
        """Gets the textual content of the provided element (e.g. filename's info or raw text)"""
        if self.filename is not None:
            with open(self.filename, "r") as f:
                self.text = f.read()
        
        return self.text
    
    def generate_audio(self):
        """Using the OpenAI API, transforms the current text into audio file"""
        self.transcript()
        response = client.audio.speech.create(
            model='tts-1',
            voice='alloy',
            input=self.text,
        )

        response.stream_to_file("./audio/audio.mp3")
        return

    def play(self):
        """Plays the generated audio"""
        playsound("audio.mp3")
        return
```

