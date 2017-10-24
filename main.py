import discord
import logging
import asyncio
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
from websearch import ytsearch


#t6mbab tokeni failist et github ei n2eks
with open('token.txt', 'r') as token:
    token = token.readline()
#loogimise moodul
logging.basicConfig(level=logging.INFO)
description = 'nibbabot'
client = discord.Client()
bot = commands.Bot(command_prefix='?', description=description)
version_inf = '0.1 pre-Alpha'

@client.event #kirjutab yle client evendis

async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')

#####käsklused
@client.event

async def on_message(message):
    if message.content.startswith('/bestperson'):
        await client.send_message(message.channel, 'Martin Ilbi')
    elif message.content.startswith('/help'):
        await client.send_message(message.channel, 
        """
        Showing all available commands:
        1) /help - all commands
        2) /bestperson - the best person on the planet
        4) /yt + search term - useless youtube search
        5) /version - version info
        """)
    elif message.content.startswith('/yt'):
        term = message.content.replace('/yt ', '')
        await client.send_message(message.channel, ytsearch(term))
    elif message.content.startswith('/version'):
        await client.send_message(message.channel, version_inf)



@client.event
async def on_message_delete(message):
    sonum = '{0.author.name} kustutas ära sõnumi:\n{0.content}'
    await client.send_message(message.channel, sonum.format(message))

@bot.command()
async def joined(member : discord.Member):
    #ss kui keegi liitub discordi
    await client.say('{0.name} liitus {0.joined_at}'.format(member))


client.run(token)