import os
import telebot
import time
import requests
import datetime
from PIL import Image
import pickle


print(os.getenv("API_TOKEN"))


url_ocr = 'http://host.docker.internal:8000/upload'
url_predict = 'http://host.docker.internal:8001/upload' 


bot = telebot.TeleBot(os.getenv("API_TOKEN"))


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.from_user.id, "Отправьте, пожалуйста картинку")


@bot.message_handler(content_types=["text", "photo"])
def handle_photo(message):
    if message.photo is None:
        bot.send_message(message.from_user.id, "Отправьте, пожалуйста картинку")   
    else:
        try:
            fileID = message.photo[-1].file_id   
            file_info = bot.get_file(fileID)
            
            downloaded_file = bot.download_file(file_info.file_path)
            filename = datetime.datetime.now().strftime("%d.%m.%Y_%H.%M.%S.%f")
            with open(f'{filename}.png', 'wb') as f:
                f.write(downloaded_file)
            with open(f'{filename}.png', 'rb') as f:
                resp = requests.post(url=url_ocr, files={'file': f})
            
            text = resp.json()['message']
            img = Image.open(f'{filename}.png')
            
            with open(f'{filename}.pkl', 'wb') as f:
                pickle.dump((img, text), f)

            with open(f'{filename}.pkl', 'rb') as f:
                resp = requests.post(url=url_predict, files={'file': f})
            result = f'{text}\n{resp.json()["message"]}'
            
            bot.send_message(message.from_user.id, result)
        except Exception as ex:
            bot.send_message(message.from_user.id, "Internal error")
    
    
bot.infinity_polling()
