import discord
import logging

#loogimise moodul
logging.basicConfig(level=logging.INFO)


def main():
    client = discord.Client
    kasutajanimi = client.user('WeskerBot')
    email = client.email('9gag@gmail.com')


main()