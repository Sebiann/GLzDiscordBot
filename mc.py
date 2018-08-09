import os
from os.path import join, dirname
from dotenv import load_dotenv
import subprocess
import discord
from discord.ext import commands

#Load the .env File
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

owner = os.getenv('owner')
hope = '465504814155956225'
alex = '453613035387486232'

class Mc:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def start(self, ctx):
        author = ctx.message.author
        if author.id == alex or author.id == owner:
            em = discord.Embed(description="Started the Server", color=0xff0000).set_author(name=author.name, icon_url=author.avatar_url).set_footer(text="Imagination")
            subprocess.call("./start.sh", shell=True)
            await self.client.say(embed=em)
        else:
            await self.client.say('Sorry no permissions')

#    @commands.command(pass_context=True)
#    async def start(self, ctx):
#        author = ctx.message.author
#        if (any(role.id == hope for role in author.roles)):
#            subprocess.call("./start.sh", shell=True)
#            await self.client.say('Server started')
#        else:
#            await self.client.say('Sorry no permissions')

def setup(client):
    client.add_cog(Mc(client))
