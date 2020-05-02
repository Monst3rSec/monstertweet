import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = str('1106991658:AAGaBVzdt6EYlc43Cfk5CTEKYIbnXScDhi0')
    bot_chatID = str('692290737')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    print send_text
    response = requests.get(send_text)

    return response.json()
    

#test = telegram_bot_sendtext('\#Testing Telegram bot')
#print(test)
