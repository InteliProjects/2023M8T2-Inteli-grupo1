// Necessary imports
const { Client, LocalAuth  } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const dotenv = require('dotenv');
const rclnodejs = require('rclnodejs');
const { QoS } = rclnodejs;
const user = require("../api/src/controllers/user.controller")


// Session variables
const client = new Client({
    authStrategy: new LocalAuth(
        {
            clientId:"pedro"
        }
    )
});
var chat_instance ={
    number:null
}

// Initial settings
dotenv.config();
rclnodejs.init()
client.initialize();


client.on('qr', (qr) => {
    qrcode.generate(qr,{small:true})
});

client.on('ready', () => {
    console.log('Client is ready!');
});


//message_create
client.on('message_create', async msg => {
    //console.log(msg.from, msg.body)
    if (msg.to == process.env.BOT_NUMBER){
        chat_instance.number = msg.from
        user.manager(msg, client, publisher)
        //console.log("aaaa")
    }
    // chat_instance.number = msg.from
    // user.manager(msg, client, publisher)


});




const node2 = rclnodejs.createNode('subscription_message_example_node');
node2.createSubscription(
    'std_msgs/msg/String',
    'whatsApp_topic',
    { qos: QoS.profileSystemDefault },
    (msg) => {
        //client.sendMessage(BOT_ID,`${msg.data}`)
        console.log(`Vinda do robo: para o ${chat_instance.number} a msg: `, msg.data,)

    }
    );
console.log("Subscribe inicializado")
rclnodejs.spin(node2);

const node = rclnodejs.createNode('client');
const publisher = node.createPublisher('std_msgs/msg/String', 'llm_topic');
