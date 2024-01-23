from telegram import Update,File
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,MessageHandler,filters
from decouple import config
from ros_communication import Talker,Listener
from speech_to_text import STT
from tts import TTS
from items_request import handle_authentication,callback_logic, answer_text_support
import requests

KEY = config('TOKEN')
auth = []
chatbot_topic= Talker('chatbot_topic')
listener = Listener('feedback_topic',callback=callback_logic)

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://2023-m8-t2-grupo1.vercel.app/")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global auth
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ola eu sou se ajudante o Jose Entregas! Pergunte para mim em texto ou aúdio sobre a posição de qualquer item no almoxarifado, se quiser que eu responda em audio mande a mensagem: /audio_mode , se quisser que eu mande o robô buscar os items mande a mensagem: /run")
    if not await  handle_authentication(update, context, update.message.chat.first_name,auth ):
        return
    if update.message.chat.first_name not in auth:
        auth.append(update.message.chat.first_name)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global auth
    if not await  handle_authentication(update, context, update.message.chat.first_name,auth ):
        return
    if update.message.chat.first_name not in auth:
        auth.append(update.message.chat.first_name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global auth
    if not await  handle_authentication(update, context, update.message.chat.first_name,auth ):
        return
    if update.message.chat.first_name not in auth:
        auth.append(update.message.chat.first_name)
    chatbot_topic.send("run")
  
    await context.bot.send_message(chat_id=update.effective_chat.id, text="run")


audio_mode = False
async def audio_mode_f(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global audio_mode 
    audio_mode = not audio_mode

    await context.bot.send_message(chat_id=update.effective_chat.id, text="audio mode: "+str(audio_mode))

async def answer_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global auth
    if not await  handle_authentication(update, context, update.message.chat.first_name,auth ):
        return
    if update.message.chat.first_name not in auth:
        auth.append(update.message.chat.first_name)
    answer=  await answer_text_support(update, context)
    if answer is None:
        return
    if audio_mode:
        tts = TTS(filename=None, text=answer)
        tts.generate_audio()
        await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('./audio/audio.mp3', 'rb'))
        return 
    await context.bot.send_message(chat_id=update.effective_chat.id, text= answer)

async def answer_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global auth
    if not await  handle_authentication(update, context, update.message.chat.first_name,auth ):
        return
    if update.message.chat.first_name not in auth:
        auth.append(update.message.chat.first_name)
    new_file = await context.bot.get_file(update.message.voice.file_id)
    with open("./audio/audio.ogg", "wb") as f:
        
        # download the voice note as a file
        await File.download_to_memory(new_file,out=f)
    stt = STT(filename='./audio/audio.ogg')
    speech_text = stt.transcribe()
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text= "entendi o seguinte do audio: "
                                   +speech_text+ 
                                   " vou processar seu pedido.")
    answer =  await answer_text_support(update, context,speech_text)
    if answer is None:
        return 

    if audio_mode:
        tts = TTS(filename=None, text=answer)
        tts.generate_audio()
        await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('./audio/audio.mp3', 'rb'))
        return
    await context.bot.send_message(chat_id=update.effective_chat.id, text= answer)
    
 




if __name__ == '__main__':
    
    application = ApplicationBuilder().token(KEY).build()
    
    start_handler = CommandHandler('start', start)
    run_handler = CommandHandler('run', run)
    message_handler = MessageHandler(filters.TEXT &(~filters.COMMAND), answer_text)
    audio_handler = MessageHandler(filters.VOICE, answer_audio)
    audio_mode_handler = CommandHandler('audio_mode', audio_mode_f)
    website_handler = CommandHandler('website', website)

    application.add_handler(start_handler)
    application.add_handler(message_handler)
    application.add_handler(run_handler)
    application.add_handler(audio_handler)
    application.add_handler(audio_mode_handler)
    application.add_handler(website_handler)
    application.run_polling()