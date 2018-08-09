import os
from os.path import join, dirname
from dotenv import load_dotenv
import discord
from discord.ext import commands

#Load the .env File
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

owner = os.getenv('owner')
cmds = '424617816025464832'

class Main:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        author = ctx.message.author
        channel = ctx.message.channel
        if channel.id == cmds or author.id == owner:
            await self.client.say('Pong!')
        else:
            pass

    @commands.command(pass_context=True)
    async def echo(self, ctx, *args):
        author = ctx.message.author
        channel = ctx.message.channel
        if channel.id == cmds or author.id == owner:
            output = ''
            for word in args:
                output += word
                output += ' '
                await self.client.say(output)
        else:
            pass

def setup(client):
    client.add_cog(Main(client))
