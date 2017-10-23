import discord
import logging
import asyncio


with open('token.txt', 'r') as token:
    token = token.readline()
#loogimise moodul
logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event #kirjutab yle client evendis

async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')


@client.event

async def on_message(message):
    if message.content.startswith('/who is the best'):
        await client.send_message(message.channel, 'Martin Ilbi')
    elif message.content.startswith('/help'):
        await client.send_message(message.channel, 
        """
        Showing all available commands:
        1) /help
        2) /who is the best
        """)


client.run(token)