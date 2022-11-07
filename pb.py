import requests
#import json
from Yobit import get_btc
from time import sleep

tok = 'Токен'
URL = "https://api.telegram.org/bot" + tok + "/"
global last_update_id
last_update_id = 0


def get_updates():
    url = URL + "getupdates"
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data["result"][-1]
    update_id = last_object['update_id']
    global last_update_id
    if last_update_id != update_id:
        last_update_id = update_id
        chat_id = last_object["message"]["chat"]["id"]
        message_text = last_object["message"]["text"]
        message = {"chat_id": chat_id,
                       "text": message_text}
        return message
    return None


def send_message(chat_id, text="Подождите..."):
    url = URL + "sendmessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)


def main():
 #d = get_updates()
 #with open("updates.json", "w") as file:
    #json.dump(d, file, indent=2, ensure_ascii=False)
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text == '/btc':
                send_message(chat_id, get_btc())
            sleep(2)
        else:
            continue

if __name__ == "__main__":
    main()
