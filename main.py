import discord
import logging
import asyncio
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
from websearch import ytsearch, fourchantop


#t6mbab tokeni failist et github ei n2eks
with open('token.txt', 'r') as token:
    token = token.readline()
#loogimise moodul
logging.basicConfig(level=logging.INFO)
description = 'nibbabot'
client = discord.Client()
bot = commands.Bot(command_prefix='/', description=description)
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
        await client.send_message(message.channel, 'Martin Ilbi <o/')
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
        await client.send_message(message.channel, ':youtube: Searching :mag_right: ' + ytsearch(term))
    elif message.content.startswith('/version'):
        await client.send_message(message.channel, version_inf)
    elif message.content.startswith('/xd'):
        await client.send_message(message.channel, """
        :joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy:
:joy::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::joy:
:joy::cool::100::cool::cool::cool::100::cool::100::100::100::cool::cool::cool::joy:
:joy::cool::100::100::cool::100::100::cool::100::cool::100::100::cool::cool::joy:
:joy::cool::cool::100::cool::100::cool::cool::100::cool::cool::100::100::cool::joy:
:joy::cool::cool::100::100::100::cool::cool::100::cool::cool::cool::100::cool::joy:
:joy::cool::cool::cool::100::cool::cool::cool::100::cool::cool::cool::100::cool::joy:
:joy::cool::cool::100::100::100::cool::cool::100::cool::cool::cool::100::cool::joy:
:joy::cool::cool::100::cool::100::cool::cool::100::cool::cool::100::100::cool::joy:
:joy::cool::100::100::cool::100::100::cool::100::cool::100::100::cool::cool::joy:
:joy::cool::100::cool::cool::cool::100::cool::100::100::100::cool::cool::cool::joy:
:joy::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::cool::joy:
:joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy:
        """
        )
    elif message.content == '/testvastamine':
        await client.send_message(message.channel, 'test1: läbitud \nnyyd vasta commandiga /testvastamine2')
        msg = await client.wait_for_message(author=message.author, content='/testvastamine2')
        await client.send_message(message.channel, 'läbitud')
    elif message.content == '/4c':
        await client.send_message(message.channel, 'Which Board?')
        msg = await client.wait_for_message(author=message.author)
        await client.send_message(message.channel, fourchantop(msg.content))
    elif message.content == '/dab':
        await client.send_file(message.channel, 'dab.png' , filename='dab.png')
    elif message.content.startswith('/setbestph'):
        with open('bestph.txt', 'w') as ph:
            link = message.content.replace('/setbestph ', '')
            try:
                testing = requests.get(link)
                status_code = testing.status_code
            except:
                    status_code = 404
            if 'http://www.pornhub.com/' not in link:
                await client.send_message(message.channel, 'Please Submit correct link!')
            elif status_code != 200:
                await client.send_message(message.channel, 'Invalid link!')
            else:
                ph.write(link)
                ph.close()
                await client.send_message(message.channel, 'Success!')
    elif message.content.startswith('/bestph'):
        with open('bestph.txt', 'r') as ph:
            link = ph.readline()
            await client.send_message(message.channel, link)

@client.event
async def on_message_delete(message):
    sonum = '{0.author.name} kustutas ära sõnumi:\n{0.content}'
    await client.send_message(message.channel, sonum.format(message))

@bot.command()
async def joined(member : discord.Member):
    #ss kui keegi liitub discordi
    await client.say('{0.name} liitus {0.joined_at}'.format(member))

client.run(token)