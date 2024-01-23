const require_iten = (msg,number,client, action, publisher) => {

    if (action[number] == "Em cadastro" || action[number] == "Pedido finalizado"){
        //client.sendMessage(number,`Olá ${action[number]}, em que posso ajudar?`);
        //console.log(`Olá ${action[number]}, em que posso ajudar?`)
        action[number] = "Em uso"
    }else{
        //client.sendMessage(number,'Pedido em processo');
        console.log('Pedido registrado')
        //console.log(robo.send(msg)) // Criar um loop logico aqui
        publisher.publish(`${msg}`);
        //action[number] = "Pedido finalizado"

    }
}


// // exportando funções criadas acima
module.exports = {
    require_iten,

};
