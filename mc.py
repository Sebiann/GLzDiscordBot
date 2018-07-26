import subprocess
import discord
from discord.ext import commands

class Mc:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self):
        subprocess.call("start.sh", shell=True)
        await self.client.say('Server Started')

def setup(client):
    client.add_cog(Mc(client))
