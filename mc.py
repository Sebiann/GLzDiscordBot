import subprocess
import discord
from discord.ext import commands

owner = '187239212544688128' #Use: if message.author.id == owner:

class Mc:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self):
        subprocess.call("start.sh", shell=True)
        await self.client.say('Server Started')

    @commands.command()
    async def stop(self):
        if message.author.id == owner:
            subprocess.call("stop.sh", shell=True)
            await self.client.say('Server Stoped')
        else:
            await self.client.say('Sorry No permissions')
def setup(client):
    client.add_cog(Mc(client))
