const userService = require("../services/user.service")
const fs = require('fs');
const path = require('path');

const fetch = require('../database/fetch')


const action ={}

const validacao = {

}


const get_Users = async () =>{ usersNum = await fetch.getFetch()
for (const num in usersNum) {
    validacao[`55${usersNum[num]}@c.us`] = true;
    console.log(`55${usersNum[num]}@c.us`)
}}




const manager = async (msg, client,publish) =>{
    await get_Users()
    if (validacao[msg.from]  !=  true){
        console.log(validacao)
        console.log(validacao[msg.from])
        //console.log("Esse BOT é de uso exclusivo, sendo necessário cadastro de um Gestor para ser usado.")
        //client.sendMessage(msg.from,"Esse BOT é de uso exclusivo, sendo necessário cadastro de um Gestor para ser usado.");
        return
    }
    try {

        var menssage = ''
        if (msg.hasMedia) {
            //client.sendMessage(msg.from,'Processando seu audio');
            var dataBase64 = (await msg.downloadMedia()).data;
            var binaryAudio = Buffer.from(dataBase64, 'base64');
            // Caminho onde você deseja salvar o arquivo no servidor
            const filePath = __dirname+'/temp/audio.mp3';

            // Escreva os dados binários no arquivo
            fs.writeFile(filePath, binaryAudio, 'binary', (err) => {
                if (err) {
                    console.error('Erro ao salvar o arquivo:', err);
                } else {
                    console.log('Arquivo salvo com sucesso em:', filePath);
                }
            });

            var stt = './src/robot_api/stt.py'
            //console.log(path.join(__dirname,'../','robot_api/stt.py'))
            var spawn = require("child_process").spawn;
            var process = spawn('python3',[stt,
            ""] );

            process.stdout.on('data', function(data) {
            console.log(data.toString());
            menssage = data.toString()
            userService.require_iten(menssage,msg.from,client,action, publish);

            } )
        }
            else{
                menssage = msg.body;
                userService.require_iten(menssage,msg.from,client, action,publish);
            }
        action[msg.from] = "Em uso"


      } catch (error) {
        //client.sendMessage(msg.from,'Houve um erro ao processar sua requisição');

        return console.log(error)
      }

}

module.exports = {
    manager

};
