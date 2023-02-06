from arsein import Messenger
from time import sleep
bot = Messenger("")

ID = "Nycto__ph_ilia"


guid = bot.getInfoByUsername(ID)['data']['user']['user_guid']


fosh = ['ماهی خوشگله الهی نمیری']

x = 0

while True:
    for i in fosh:
        bot.sendMessage(guid,i)
        x += 1
        print(f'ok {x}')
        sleep(5)