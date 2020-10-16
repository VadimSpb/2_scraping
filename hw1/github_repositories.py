import requests
from getpass import getpass
import json

def auth_user():
    username = input('Enter your username: ')
    password = getpass('Enter your password: ')
    link = f'https://api.github.com/user'
    answ = requests.get(link, auth=(username, password))
    if answ.ok is True:
        print ('Authorization is ok')
    else:
        print ('Something was wrong')
        pass
    return answ

answ = auth_user()
while answ.ok is not True:
    answ = auth_user()

username = input('Enter the username whose repo you want to get: ')
link = f'https://api.github.com/users/{username}/repos'
answ = requests.get(link)

answ = answ.json()

print ('List os repos:')
for i in range(len(answ)):
    print(answ[i]['name'])


link_to_file = f'{username}_repos.json'
with open(link_to_file, "w", encoding="utf-8") as file:
    json.dump(answ, file)

