import subprocess
import discord
from discord.ext import commands

owner = '187239212544688128'
atlantic = '465504814155956225'

class Mc:
    def __init__(self, client):
        self.client = client

    @commands.event
    async def on_message(message):
        if message.content.startswith('zstart') and any(role.name == name for role in message.author.roles):
            subprocess.call("start.sh", shell=True)
            await self.client.say('Server started')
        else:
            await self.client.say('Sorry No permissions')
def setup(client):
    client.add_cog(Mc(client))
