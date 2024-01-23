---
sidebar_position: 1
---

# Requisitos Funcionais & Não Funcionais

A inclusão de requisitos funcionais e não funcionais é fundamental para uma compreensão abrangente e eficaz das funcionalidades do sistema que está sendo desenvolvido. Os requisitos funcionais delineiam as ações específicas que o sistema deve executar, proporcionando uma visão clara e detalhada do comportamento esperado em resposta a diferentes entradas ou eventos. Ao compreender essas funcionalidades específicas, os desenvolvedores e stakeholders podem alinhar suas expectativas e garantir que o sistema atenda às necessidades operacionais e de negócios.

Por outro lado, os requisitos não funcionais focam nos atributos de qualidade do sistema, tais como desempenho, segurança e usabilidade. Esses requisitos são cruciais para validar a eficiência global do sistema, indo além das funcionalidades básicas. Ao estabelecer critérios mensuráveis para aspectos como escalabilidade, confiabilidade e experiência do usuário, a documentação de requisitos não funcionais fornece um guia essencial para avaliar a viabilidade e o sucesso do sistema em termos mais amplos. Em conjunto, os requisitos funcionais e não funcionais não apenas definem o que o sistema deve fazer, mas também asseguram que ele o faça de maneira eficiente, confiável e em conformidade com as expectativas e exigências do usuário e do negócio.

## Requisitos

A seguir, estão algumas delas listadas:

<div style={{display: "flex"}}>

<div style={{width:"50%"}}>

| N°  | Requisito | Descrição                                                                              |
| --- | --------- | -------------------------------------------------------------------------------------- |
| 1   | Funcional | Capacidade do sistema entender a peça que deve ser pega por fala ou texto              |
| 2   | Funcional | Capacidade de mapear espaços que o robô percorreu                                      |
| 3   | Funcional | Robô deve ser capaz de percorrer o caminho até um item específico em um espaço mapeado |
| 4   | Funcional | Deve haver controle automático do inventário das peças retiradas pelo robô             |
| 5   | Funcional | Deve haver uma aplicação que permita ver o inventário                                  |
| 6   | Funcional | Deve haver uma aplicação que permita ativar o robô para pegar um item                  |
| 7   | Funcional | A aplicação deve ter um método de parar o robô                                         |

</div>

<div style={{width:"50%", paddingLeft:"50px"}}>

| Nº  | Tipo          | Descrição |
| --- | ------------- | --------- |
| 1   | Não-funcional | O sistema deve ser capaz de processar comandos de fala ou texto em menos de 2 segundos |
| 2   | Não-funcional | O sistema deve ser capaz de mapear um espaço de 1000 metros quadrados em não mais que 15 minutos |
| 3   | Não-funcional | O sistema de controle de inventário deve ser capaz de atualizar o status de um item em menos de 1 segundo após o robô pegá-lo |
| 4   | Não-funcional | A aplicação deve ser capaz de exibir os itens disponíveis em menos de 3 segundos após a solicitação |
| 5   | Não-funcional | A aplicação deve ser capaz de ativar o robô para pegar um item em menos de 5 segundos após a solicitação |
| 6   | Não-funcional | A aplicação deve ser capaz de exibir o inventário atualizado em menos de 10 segundos após a solicitação |
| 7   | Não-funcional | A aplicação deve ser capaz de parar o robô em menos de 10 segundo após a solicitação |
| 8   | Não-funcional | O sistema deve ser capaz de operar por pelo menos 8 horas contínuas sem falhas  |
| 9   | Não-funcional | O sistema deve garantir a segurança dos dados do inventário, permitindo apenas acesso autorizado |
| 10  | Não-funcional | O Robô deve ser capaz de servir as páginas, em menos de 2 segundos, relacionadas ao controle do robô.|

</div>
</div>

## Testes

Para testar os requisitos não-funcionais, foram preparados testes unitários (neste caso, _scripts_ em *_Python_*) que auxiliassem na validação das funcionalidades. Todos os testes podem ser encontrados na pasta _test_ do [repositório no Github](https://github.com/2023M8T2-Inteli/grupo1/tree/dev/test).

| N° | Teste | Status | Procedimento | Resultados | Observação |
|:--:|:-----:|:------:|:------------:|:----------:|:----------:|
| 1  | O sistema deve ser capaz de processar comandos de fala ou texto em menos de 2 segundos | ✅ Sucesso | Utilizando um cronômetro, mediu-se o tempo que leva para registrar o comando e transformá-lo em coordenada efetiva para o robô | <ul> <li>✅ A conversão de texto para comando leva menos de 1ms</li> <li>🚧 A conversão de fala para comando leva em torno de 1s a 1.5s para ser processada</li> </ul> | O tempo de conversão pode variar dependendo da conexão com a Internet, visto que depende de uma API externa |
| 2  | O sistema deve ser capaz de mapear um espaço de 1000 metros quadrados em não mais que 15 minutos | ✅ Sucesso | Utilizando um cronômetro, mediu-se o tempo que leva para mapear um espaço sem obstáculos de 100 m² | O tempo registrado para esse teste de mapeamento foi inferior a um minuto e meio  | 🚧 Caso o ambiente apresente muitos obstáculos, o tempo de mapeamento pode ser bem superior a esse |
| 3  | O sistema de controle de inventário deve ser capaz de atualizar o status de um item em menos de 1 segundo após o robô pegá-lo | ❔ Ainda não testado | - | - | Ainda não há um inventário para fazer o teste |
| 4  | A aplicação deve ser capaz de exibir os itens disponíveis em menos de 3 segundos após a solicitação | ✅ Sucesso  | Utilizando um cronômetro, mediu-se o tempo que leva até a página com os itens do inventário ser carregada totalmente | ✅ O carregamento da página com boa conexão leva menos de 1 segundo | O tempo de carregamento pode variar dependendo da conexão com a Internet |
| 5  | A aplicação deve ser capaz de ativar o robô para pegar um item em menos de 5 segundos após a solicitação | ✅ Sucesso | Utilizando um cronômetro, mediu-se o tempo que leva para enviar a coordenada ao robô e seu efetivo movimento | ✅ A ativação do robô até o ponto demora entre 1~3ms para iniciar a rotina de navegação até o ponto indicado| - |
| 6  | A aplicação deve ser capaz de exibir o inventário atualizado em menos de 10 segundos após a solicitação | ✅ Sucesso  | Utilizando um cronômetro, mediu-se o tempo que leva até a página com os itens do inventário ser carregada totalmente | ✅ O carregamento da página com boa conexão leva menos de 1 segundo | O tempo de carregamento pode variar dependendo da conexão com a Internet |
| 7  | A aplicação deve ser capaz de parar o robô em menos de 10 segundo após a solicitação | ❔ Ainda não testado | - | - | - |
| 8  | O sistema deve ser capaz de operar por pelo menos 8 horas contínuas sem falhas | ❌ Falhou | Utilizando um relógio, mede-se o tempo no qual o robô mantêm-se operando sem irregularidades | O robô precisa ser recarregado após algumas horas de uso | Deve-se pensar em uma maneira mais eficiente de gerenciar a bateria do robô. Devido às restrições de projeto, ainda não há solução disponível |
| 9  | O sistema deve garantir a segurança dos dados do inventário, permitindo apenas acesso autorizado | ❌ Falhou | - |  Autenticação não implementada  | - |
| 10  | O Robô deve ser capaz de servir as páginas, em menos de 2 segundos, relacionadas ao controle do robô. | ✅ Sucesso  | Utilizando um cronômetro, mediu-se o tempo que leva até a página ser carregada totalmente | ✅ O carregamento da página com boa conexão leva menos de 1 segundo | O tempo de carregamento pode variar dependendo da conexão com a Internet |