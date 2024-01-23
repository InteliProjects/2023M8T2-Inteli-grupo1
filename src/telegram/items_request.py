import requests
import re
from model import ChatBotModel
from ros_communication import Talker
llm = ChatBotModel()
talker = Talker('chatbot_topic')
requested_items = []
def get_items():
    url = 'https://2023-m8-t2-grupo1.vercel.app/api/item/get'
    response = requests.get(url)
    item_dict = {}
    if response.status_code == 200:
        data = response.json()
        with open('itens.txt', 'w') as file:
            for item in data:
                item_name = item['item']
                x_value = item['x']
                y_value = item['y']
                file.write(f'O {item_name} se encontra em x: {x_value} e y: {y_value}\n')
                item_dict[(x_value, y_value)] = item_name
    else:
        print("Ocorreu um erro:", response.status_code)
    response = requests.get('https://2023-m8-t2-grupo1.vercel.app/api/number/get')
    if response.status_code == 200:
        numbers = response.json()
    return item_dict,numbers
    

def find_person(lista:list,name: str) -> dict:
    for item in lista:
        if item['name'] == name:
            return item
    return None

            
def get_input_position(msg):
    """
    This function purpose is to get the position from the chatbot
    using a regex, then returning it as a list of integers
    """
    input_text = msg
    match = re.findall(r'[-+]?\d*\.\d+|[-+]?\d+', input_text)
    if not match:
        return None
    print(match)
    position = [float(i) for i in match]
    print(f"position: {position}")
    return position

def callback_logic(message):
    print(message)
    if message == "i am done":
        for item in requested_items:
            print(item['id'])
            requests.post('https://2023-m8-t2-grupo1.vercel.app/api/logs/status/',json={"id":item['id'],"status":2})
        print("done")
        requested_items.clear()
       
        return
    
itens,numbers = get_items()
async def answer_text_support(update, context,speech_to_text=None):
    global itens,numbers
    if speech_to_text is None:
        answer= llm.chat(update.message.text)
    else:
        answer= llm.chat(speech_to_text)
    position = get_input_position(answer)

    if position is None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "não entendi o que você quis dizer, tente novamente")
        return
    item =itens[(position[0],position[1])]
    talker.send(f"{position[0]},{position[1]}")
    name = update.message.chat.first_name
   
    person = find_person(numbers,name)
    if person is None:
     
        itens,numbers = get_items()
        person = find_person(numbers,name)

    json = {
    "requester_name":name,
    "requester_number": person['number'],
    "item": item,
    "quantity": 1,
    "category": "manutenção",
    "status": 1
}
    print(json)

    response = requests.post('https://2023-m8-t2-grupo1.vercel.app/api/logs/create/', json=json)
    print(response)
    requested_items.append(response.json())
    return answer

async def handle_authentication(update, context,name,auth):
    if name in auth:
        return True
    numbers = requests.get('https://2023-m8-t2-grupo1.vercel.app/api/number/get').json()
    if find_person(numbers,name) is None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "você não está autorizado a usar este bot. se cadastre no site: https://2023-m8-t2-grupo1.vercel.app/")
        return False 
    return True
   

