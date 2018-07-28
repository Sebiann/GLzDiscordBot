import subprocess
import discord
from discord.ext import commands

owner = '187239212544688128'
atlantic = '465504814155956225'

class Mc:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self, ctx):
        author = ctx.message.author
        if (any(role.name == 'name' for role in author.roles)):
            subprocess.call("start.sh", shell=True)
            await self.client.say('Server started')
        else:
            await self.client.say('Sorry no permissions')

def setup(client):
    client.add_cog(Mc(client))
