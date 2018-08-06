import discord
from discord.ext import commands

owner = '187239212544688128'
cmds = '424617816025464832'

class Main:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        author = ctx.message.author
        channel = ctx.message.channel
        if channel.id == cmds or author.id == owner:
            await self.client.say('Pong!')
        else:

    @commands.command()
    async def echo(self, *args, ctx):
        author = ctx.message.author
        channel = ctx.message.channel
            if channel.id == cmds or author.id == owner:
                output = ''
                for word in args:
                    output += word
                    output += ' '
                    await self.client.say(output)
            else:

def setup(client):
    client.add_cog(Main(client))
