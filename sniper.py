import requests, json
from random import choice, randint
from time import sleep

def sendDiscord(content: str):
    with open('./config.json', 'r') as file:
        URL = json.loads(file.read())['DISCORD_WEBHOOK_URL']
    
    headers = {
        'Content-Type': "application/json"
    }
    
    data = {
        "content": content
    }
    
    req = requests.post(URL, headers=headers, data=json.dumps(data))

    if req.status_code == 204:
        print("Sucessfully sent to discord")
    else:
        print(f"Failed to send to discord (Error code: {req.status_code})")


UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"

headers= {
    "user-agent": UA
}

alph = "abcdefghijklmnopqrstuvwxyz"
alph += alph.upper()
nbs = "0123456789"

# i put alph 3 times to decrease the chances to have less numbers
idk = [alph, nbs, alph, alph]

url = "https://outplayed.tv/media/"

attempts = 1
with open('./config.json', 'r') as file:
    DELAY = json.loads(file.read())['DELAY']

while True:
    
    endpoint = ""
    
    for _ in range(6):
        endpoint += choice(idk[randint(0, 3)])
    
    req = requests.get(url + endpoint, headers=headers)
    print(attempts, req, url + endpoint)
    
    if req.status_code != 404:
        print(url + endpoint)
        print(f"Found after {attempts} attempts")

        sendDiscord(url + endpoint)
        attempts = 0
    
    attempts += 1
    sleep(DELAY)
