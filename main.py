import discord
from discord.ext import commands

class Main:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self):
        await self.client.say('Pong!')

    @client.command()
    async def echo(*args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await client.say(output)

def setup(client):
    client.add_cog(Main(client))
