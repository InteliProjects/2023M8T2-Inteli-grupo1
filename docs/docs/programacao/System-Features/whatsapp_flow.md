# Whatsapp

## Fluxo Atual

Abaixo, o fluxo do usuário pelo WhatsApp em um diagrama de blocos:

<iframe width="800" height="450" src="https://whimsical.com/embed/Ay2sLu2xp9JkxeNW7okHEx"></iframe>

## Aquivos e Funções Utilizadas

Abaixo os principais arquivos e funções utilizadas na interface whatsapp robô.

### API - server.js
<p><b>Caminho do diretório:</b> grupo1/src/api/server.js</p>

```javascript
// Imports
const { Client, LocalAuth  } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const dotenv = require('dotenv');

const user = require("../api/src/controllers/user.controller")
const dev = require("../api/src/controllers/user.dev")


//  Environment settings
dotenv.config();
const BOT_ID = process.env.BOT_ID;
const client = new Client({
    authStrategy: new LocalAuth(
        {
            clientId:"pedro"
        }
    )
});
```

Importações:
- <b>whatsapp-web.js:</b> Biblioteca para interagir com o WhatsApp Web.
- <b>qrcode-terminal:</b> Biblioteca que possibilita a exibição de qr codes no terminal.
- <b>dotenv:</b> Biblioteca que permite trabalhar com variáveis de ambiente.


<p>As configurações do ambiente incluem o número do WhatsApp armazenado na constante 'BOT_ID' e uma configuração para que o <b>client</b> saiba que deve manter a sessão do WhatsApp.</p>

```javascript
// Usage of the WhatsApp client
client.on('qr', (qr) => {
    qrcode.generate(qr,{small:true})
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.initialize();

client.on('message_create', async msg => {
    if (msg.fromMe){dev.manager(msg, client);}
    if (msg.to == `${BOT_ID}`){user.manager(msg, client);}
});
```

<p>Como a biblioteca do WhatsApp se trata de um socket, ela é orientada a eventos, dos quais estou utilizando:</p>

- <b>'qr':</b> Usado para estabelecer uma sessão do WhatsApp Web.
- <b>'ready':</b> Acionado quando a sessão termina de parear com whatsapp.
- <b>'message_create':</b> Acionado quando o número cadastrado (BOT_ID) recebe uma mensagem.

Nesse trecho do código, eu só verifico se a mensagem recebida foi enviada pelo próprio número cadastrado. Se sim, envio o fluxo de desenvolvimento; se não, envio o fluxo de usuário normal.

### API - user.controller.js
<p><b>Caminho do diretório:</b> grupo1/src/api/controllers/user.controller.js</p>

```javascript
// Session management
var users = {

}


var cadastrado = {

}
```

```javascript
//  Validations
const namefind = (numero) => {
    if (users[numero]){
        console.log("User cadastrado ----> ", users[numero])
        return true
    }
    return  false

}

const validacao = (numero) => {
    if (cadastrado[numero]){
        console.log("User cadastrado")
        return false
    }
    else{
        cadastrado[numero] = "Em cadastro"
        return true
    }

}
```

Na camada de controle, faço o gerenciamento da sessão do cliente e o cadastro em tempo de execução. A variável 'cadastro' serve para controlar o fluxo das mensagens, sendo possível incorporar os valores:

- <b>"Em uso":</b> As mensagens são encaminhadas diretamente para o robô.
- <b>"Em cadastro":</b> Registra o nome do cliente.
- <b>"Pedido finalizado":</b> Indica o termino da conversa.

### API - user.service.js
<p><b>Caminho do diretório:</b> grupo1/src/api/services/user.service.js</p>

```javascript
//  Item request
const require_iten = (msg,client, users, cadastrado) => {
    console.log(cadastrado)
    if (cadastrado[msg.from] == "Em cadastro" || cadastrado[msg.from] == "Pedido finalizado"){
        client.sendMessage(msg.from,`Olá ${users[msg.from]}, em que posso ajudar?`);
        //console.log(`Olá ${users[msg.from]}, em que posso ajudar?`)
        cadastrado[msg.from] = "Em uso"
    }else{
        client.sendMessage(msg.from,'Pedido em processo');
        robo.send(msg.body,cadastrado[msg.from])

    }
}
```

```javascript
//  User registration
const create =(msg,users) =>{
    if (users[msg.from] ){
        return
    }else {users[msg.from] = msg.body}
}
```

Na camada de serviço que o sistema execulta as ações necessárias, tendo no momento duas:

- <b>"require_iten":</b> Manda a menssagem para o robô.
- <b>"create":</b> Finaliza o cadastro adicionando o número ao array de usuários.

### API - robot.js
<p><b>Caminho do diretório:</b> grupo1\src\api\src\robot_api\robot.js</p>

```javascript
const rclnodejs = require('rclnodejs');
const path = require("path")

// Create ros object to communicate over your ros connections
rclnodejs.init()
const node = rclnodejs.createNode('client');
const publisher = node.createPublisher('std_msgs/msg/String', 'llm_topic');

// Message publisher
function send(msg) {
    try {
        publisher.publish(`${msg}`);
        const spawn = require("child_process").spawn;
        const pythonProcess = spawn('python3',[path.resolve(__dirname, 'tts.py'), msg]);
        return "Mensagem após cliente send";

    } catch (error) {
        console.log(error)
    }
}
```
Importações:
- <b>rclnodejs:</b> Biblioteca para interagir com o WhatsApp Web.
- <b>path:</b> Biblioteca que permite trabalhar com variáveis de ambiente.

Na camada robô que o sistema cria uma comunicação com os tópicos do ros, publicando no tópico 'llm_topic' as menssagens passadas pelo argumento 'msg':

### Robot Service - llm_robot.py
<p><b>Caminho do diretório:</b> grupo1\src\ros2_ws\src\robot_service\robot_service\llm_robot.py</p>


```python
class ChatBotModel(Node):
    def __init__(self):
        super().__init__('llm_node')
        self._publisher = self.create_publisher(String, 'chatbot_topic', 10)
        self._subscriber = self.create_subscription(
            String,
            'llm_topic',
            self.listener_callback,
            10)
        self._logger = self.get_logger()
        self._msg = String()
        self._model = LLM_model()
```

Através do método construtor, realizo a criação de instância do meu modelo de LLM, crio um publisher e um subscribe.

```python
    def listener_callback(self, msg):
        """
        This function purpose is to processes data from the llm_topic
        """
        self._logger.info(f'Robot received: {msg.data}')
        self._logger.warning('Passing data to navigation controller')
        self.chat(msg.data)
```

Com o callback do meu tópico 'llm_topic', passo a mensagem vinda do WhatsApp para o meu modelo de LLM.

```python
    def chat(self, text):
        output_text = self._model.chat(text)
        self.get_logger().info('Model output: ' + output_text)
        self._msg.data = self.get_input_position(output_text)
        self._publisher.publish(self._msg)
```

Essa função tem a responsabilidade de publicar a saída que o modelo deu para a entrada da mensagem.

```python
    def get_input_position(self,text):
        """
        This function purpose is to get the position from the chatbot
        using a regex, then returning it as a list of float
        """
        input_text = text
        self._logger.info(f'Robot received: {text}')
        match = re.findall(r'[-+]?(\d*\.\d+|\d+)([eE][-+]?\d+)?', input_text)
        position = [float(i[0]) for i in match]
        self._logger.info(f'position: {position}')
        if len(position) > 1:
            return f"{position[0]},{position[1]}"
        self._logger.info(f'Erro ao detectar as peças: { len(position) }')
```

Com essa função, filtro a saída do modelo para que sejam postadas somente as coordenadas indicadas por ele.

### Robot Service - llm.py
<p><b>Caminho do diretório:</b> grupo1\src\ros2_ws\src\robot_service\robot_service\llm.py</p>


```python
class LLM_model():
    def __init__(self) -> None:
        self._model = ollama.Ollama(model="dolphin2.2-mistral")
        self._retriever = self.archive_loader_and_vectorizer()
        template = """Answer the question based only on the following context:
        {context}
        Question: {question}
        """
        self._prompt = ChatPromptTemplate.from_template(template)
```

No método construtor, indico qual modelo irei utilizar e crio um template de resposta para ele.

```python
    def archive_loader_and_vectorizer(self):
        """
        This function loads txt documents from current directory
        and vectorizes them
        """
        loader = DirectoryLoader('./',
                                glob='**/items.txt',
                                loader_cls=TextLoader,
                                show_progress=True
                            )
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = chroma.Chroma.from_documents(docs, embedding_function)
        retriever = vectorstore.as_retriever()
        return retriever
```

Nessa função indico que tipo de codificação será utilizada para o meu arquivo de contexto, onde ele se encontra e configuro meu retriever.

```python
    def chat(self, text):

        chain = (
            {"context": self._retriever, "question": RunnablePassthrough()}
            | self._prompt
            | self._model
        )
        return str(chain.invoke(text))
```

Invoca a chamada do modelo passando o texto vindo do meu subscribe.

### Robot Service - robot.py
<p><b>Caminho do diretório:</b> grupo1\src\ros2_ws\src\robot_service\robot_service\llm.py</p>


```python
class Robot(Node):
    def __init__(self):
        super().__init__('robot_node')
        self._publisher = self.create_publisher(String, 'whatsApp_topic', 10)
        self._subscriber = self.create_subscription(
            String,
            'chatbot_topic',
            self.listener_callback,
            10)
        self._logger = self.get_logger()
        self._msg = String()
        self._nav = Navigation()

```

Através do método construtor, realizo a criação de instância do Navigation, crio um publisher e um subscribe.

```python
    def listener_callback(self, msg):
        """
        This function purpose is to receive the data from the chatbot topic
        """
        self._logger.info(f'Robot received: {msg.data}')
        self._logger.warning('Passing data to navigation controller')
        self._msg = msg.data
        return self._msg

```

No meu callback, adiciono as coordenadas públicas à minha variável _msg.

```python
    def get_input_position(self):
        """
        This function purpose is to get the position from the chatbot
        using a regex, then returning it as a list of integers
        """
        input_text = self.listener_callback()
        match = re.findall(r'\b\d+\b', input_text)
        position = [float(match) for i in match[-2:]]
        return position

```

Essa função ira pegar as coordenadas vindas no formato (x,y) e passa-las para uma lista.

```python
    def move_towards_required_position(self):
        """
        This function purpose is to create a pose and move the robot
        """
        position = self.get_input_position()
        self._nav.create_pose(position[0], position[1], 0.0)

```

Com a lista acima, essa função adiciona as coordenadas para o navigation.

```python
    def cheking_status(self):
        """
        Checks the status of a task after moving towards the required position.
        Returns:
        bool: True if the task is completed successfully, False otherwise.
        """
        self.move_towards_required_position()
        task_status = self._nav.robot_navigation_status()

        return task_status if task_status == TaskResult.SUCCEEDED else False

```

Por fim, esta é uma função de controle que verifica o status de toda essa operação.
