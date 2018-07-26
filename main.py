import discord
from discord.ext import commands

class Main:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self):
        await self.client.say('Pong!')

    @commands.command()
    async def echo(self, *args):
        output = ''
        for word in args:
            output += word
            output += ' '
        await self.client.say(output)

def setup(client):
    client.add_cog(Main(client))
