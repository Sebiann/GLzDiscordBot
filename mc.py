import subprocess
import discord
from discord.ext import commands

owner = '187239212544688128'
hope = '465504814155956225'
alex = '453613035387486232'

class Mc:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def start(self, ctx):
        author = ctx.message.author
        if author.id == alex:
            subprocess.call("start.sh", shell=True)
            await self.client.say('Server started')
        else:
            await self.client.say('Sorry no permissions')

#    @commands.command(pass_context=True)
#    async def start(self, ctx):
#        author = ctx.message.author
#        if (any(role.id == hope for role in author.roles)):
#            subprocess.call("start.sh", shell=True)
#            await self.client.say('Server started')
#        else:
#            await self.client.say('Sorry no permissions')

def setup(client):
    client.add_cog(Mc(client))
