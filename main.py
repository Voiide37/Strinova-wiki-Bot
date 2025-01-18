import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('*hello'):
            await message.channel.send('Hello!')

        commands = {
            '!michele': 'https://strinova.org/wiki/Michele',
            '!nobunaga': 'https://strinova.org/wiki/Nobunaga',
            '!kokona': 'https://strinova.org/wiki/Kokona',
            '!yvette': 'https://strinova.org/wiki/Yvette',
            '!flavia': 'https://strinova.org/wiki/Flavia',
            '!yugiri': 'https://strinova.org/wiki/Yugiri',
            '!ming': 'https://strinova.org/wiki/Ming',
            '!lawine': 'https://strinova.org/wiki/Lawine',
            '!meredith': 'https://strinova.org/wiki/Meredith',
            '!reiichi': 'https://strinova.org/wiki/Reiichi',
            '!kanami': 'https://strinova.org/wiki/Kanami',
            '!eika': 'https://strinova.org/wiki/Eika',
            '!fragrans': 'https://strinova.org/wiki/Fragrans',
            '!celestia': 'https://strinova.org/wiki/Celestia',
            '!audrey': 'https://strinova.org/wiki/Audrey',
            '!maddelena': 'https://strinova.org/wiki/Maddelena',
            '!fuchsia': 'https://strinova.org/wiki/Fuchsia',
            '!baimo': 'https://strinova.org/wiki/Bai_Mo',
            '!galatea': 'https://strinova.org/wiki/Galatea',
            '!leona': 'https://strinova.org/wiki/Leona'
        }

        for command, link in commands.items():
            if message.content.startswith(command):
                query = command[len('*search'):]
                await message.channel.send(f"Here's The Info Gamer: {link}")
                break

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))
