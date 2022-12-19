import os
import telebot
import time
import requests


print(os.getenv("API_TOKEN"))

url = 'http://host.docker.internal:8000/upload'


bot = telebot.TeleBot(os.getenv("API_TOKEN"))


@bot.message_handler(commands=["start"])
def handle_start(message):
    chat_id = message.from_user.id
    print(message.text)
    print(chat_id)
    #print(message)
    bot.send_message(message.from_user.id, f"ok")


@bot.message_handler(content_types=["text", "photo"])
def handle_photo(message):
    chat_id = message.from_user.id
    #print('in', chat_id, message.text)
    #print(message)
    #global msg
    #msg = message
    if not message.photo is None:
        #print(len(message.photo))
        fileID = message.photo[-1].file_id   
        file_info = bot.get_file(fileID)
        

        #print(file_info.file_path)
        
        downloaded_file = bot.download_file(file_info.file_path)
        resp = requests.post(url=url, files={'file': downloaded_file})
        bot.send_message(message.from_user.id, resp.json()['message'])
    else:
        bot.send_message(message.from_user.id, "Отправьте, пожалуйста картинку")        

    #print('out', chat_id, message.text)
    
    
bot.infinity_polling()
