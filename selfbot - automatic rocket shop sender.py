import discord
from random import *

#Your shop without restriction
Shop = """

"""

#Your shop in a version that follows the rules on the “Rocket League Garage” and “Rocket Planet” servers(15 lines maximum, ...)
MinShop = """

"""

# Liste des channels possibles ainsi que leurs id:
RLGarage = 280753307860074496
RocketPlanet = 249642821047418881
RLTrade = 1043143367640494110
RLInsider = 363460545006796800
GlacialTrades = 326103689469362186
RLTracker = 224147292330917888
KanGolu = 340249014899310593



# CN for "current number"
CN_RLG = 0                                      # RLG for "Rocket League Garage"
CN_RP = 0                                       # RP for "Rocket Planet"
CN_RLT = 0                                      # RLT for "Rocket League Trade"
CN_RLI = 0                                      # RLI for "RL Insider"
CN_GT = 0                                      # GT for "Glacial Trades"
CN_RLTr = 0                                      # RLTr for "RL Tracker"
CN_KG = 0                                      # KG for "KanGolu"

#NTR for "Number To Reach" (randomly generated between 10 and 30 messages)
NTR = 0
def GenNTR():
    global NTR
    NTR = randint(10,30)                                         
    print('Le nouveau nombre à atteindre est ', NTR, ' !')

class MyClient(discord.Client):
    async def on_ready(self):
        global NTR
        print('Logged on as', self.user)
        GenNTR()

    async def on_message(self, message):
        global CN_RLG, CN_RP, CN_RLT, CN_RLI, CN_GT, CN_RLTr, CN_KG, NTR
        if message.author != self.user:

            if message.channel.id == RLGarage:
                CN_RLG = CN_RLG + 1
                print('On est à ', CN_RLG, 'message(s) sur ', NTR, ' dans le channel du serveur ', message.guild)
                if CN_RLG >= NTR :
                    await message.channel.send(MinShop)
                    print('Le shop a été envoyé dans le channel du serveur ', message.guild, '!')

                    CN_RLG = 0
                    print('La variable CN_RLG a été réinitialisée !')

                    GenNTR()
            
            if message.channel.id == RocketPlanet:
                CN_RP = CN_RP + 1
                print('On est à ', CN_RP, 'message(s) sur ', NTR, ' dans le channel du serveur ', message.guild)
                if CN_RP >= NTR :
                    await message.channel.send(MinShop)
                    print('Le shop a été envoyé dans le channel du serveur ', message.guild, '!')

                    CN_RP = 0
                    print('La variable CN_RP a été réinitialisée !')

                    GenNTR()
            
            if message.channel.id == RLTrade:
                CN_RLT = CN_RLT + 1
                print('On est à ', CN_RLT, 'message(s) sur ', NTR, ' dans le channel du serveur ', message.guild)
                if CN_RLT >= NTR :
                    await message.channel.send(Shop)
                    print('Le shop a été envoyé dans le channel du serveur ', message.guild, '!')

                    CN_RLT = 0
                    print('La variable CN_RLT a été réinitialisée !')

                    GenNTR()

            if message.channel.id == RLInsider:
                CN_RLI = CN_RLI + 1
                print('On est à ', CN_RLI, 'message(s) sur ', NTR, ' dans le channel du serveur ', message.guild)
                if CN_RLI >= NTR :
                    await message.channel.send(Shop)
                    print('Le shop a été envoyé dans le channel du serveur ', message.guild, '!')

                    CN_RLI = 0
                    print('La variable CN_RLI a été réinitialisée !')

                    GenNTR()

            if message.channel.id == GlacialTrades:
                CN_GT = CN_GT + 1
                print('On est à ', CN_GT, 'message(s) sur ', NTR, ' dans le channel du serveur ', message.guild)
                if CN_GT >= NTR :
                    await message.channel.send(Shop)
                    print('Le shop a été envoyé dans le channel du serveur ', message.guild, '!')

                    CN_GT = 0
                    print('La variable CN_GT a été réinitialisée !')

                    GenNTR()
            
            if message.channel.id == RLTracker:
                CN_RLTr = CN_RLTr + 1
                print('On est à ', CN_RLTr, 'message(s) sur ', NTR, ' dans le channel du serveur ', message.guild)
                if CN_RLTr >= NTR :
                    await message.channel.send(Shop)
                    print('Le shop a été envoyé dans le channel du serveur ', message.guild, '!')

                    CN_RLTr = 0
                    print('La variable CN_RLTr a été réinitialisée !')

                    GenNTR()
            
            if message.channel.id == KanGolu:
                CN_KG = CN_KG + 1
                print('On est à ', CN_KG, 'message(s) sur ', NTR, ' dans le channel du serveur ', message.guild)
                if CN_KG >= NTR :
                    await message.channel.send(Shop)
                    print('Le shop a été envoyé dans le channel du serveur ', message.guild, '!')

                    CN_KG = 0
                    print('La variable CN_KG a été réinitialisée !')

                    GenNTR()

client = MyClient()
client.run('YOUR TOKEN HERE')