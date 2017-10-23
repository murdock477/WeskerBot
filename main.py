import discord
import logging
import asyncio
import requests
from discord.ext import commands


#t6mbab tokeni failist et github ei n2eks
with open('token.txt', 'r') as token:
    token = token.readline()
#loogimise moodul
logging.basicConfig(level=logging.INFO)
description = 'nibbabot'
client = discord.Client()
bot = commands.Bot(command_prefix='?', description=description)

@client.event #kirjutab yle client evendis

async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')


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
        """)
    elif message.content.startswith('/yt'):
        term = message.content.replace('/yt ', '')
        url = 'https://www.youtube.com/results?search_query=' + term
        await client.send_message(message.channel, url)


@client.event
async def on_message_delete(message):
    sonum = '{0.author.name} kustutas ära sõnumi:\n{0.content}'
    await client.send_message(message.channel, sonum.format(message))

@bot.command()
async def joined(member : discord.Member):
    #ss kui keegi liitub discordi
    await client.say('{0.name} liitus {0.joined_at}'.format(member))


client.run(token)