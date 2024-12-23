# -*- coding: utf-8 -*-
"""
Spyder Editor

@ygoats

This is a temporary script file.
"""

from pycoingecko import CoinGeckoAPI
import telegram_send
from datetime import datetime
from time import sleep

def grabTopSeven():
    cg = CoinGeckoAPI()
    
    data = cg.get_search_trending()
    
    coin1 = data['coins'][0]['item']['symbol']
    coin2 = data['coins'][1]['item']['symbol']
    coin3 = data['coins'][2]['item']['symbol']
    coin4 = data['coins'][3]['item']['symbol']
    coin5 = data['coins'][4]['item']['symbol']
    coin6 = data['coins'][5]['item']['symbol']
    coin7 = data['coins'][6]['item']['symbol']
    
    telegram_send.send(conf='user1.conf',messages=["TOP 7 TRENDING COINGECKO COINS" + "\n" + \
                                                   "#1: " + str(coin1) + "\n" + \
                                                   "#2: " + str(coin2) + "\n" + \
                                                   "#3: " + str(coin3) + "\n" + \
                                                   "#4: " + str(coin4) + "\n" + \
                                                   "#5: " + str(coin5) + "\n" + \
                                                   "#6: " + str(coin6) + "\n" + \
                                                   "#7: " + str(coin7)])                                         

def Main():
    
    initialProcessing = True
    
    now = datetime.now()
    tt = now.strftime("%H:%M:%S")
    
    startProg = True
    
    while startProg == True:
        now = datetime.now()
        tt = now.strftime("%H:%M:%S")
        if tt == "00:00:00" or tt == "04:00:00" or tt == "08:00:00" or tt == "12:00:00" or tt == "16:00:00" or tt == "20:00:00":
            
            grabTopSeven()
            sleep(100)
if __name__ == '__main__':
    Main()

