import discord
from discord.ext import commands
import random

#Permissions
owner = '187239212544688128' #Use: if message.author.id == owner:
admin = '439729155693740032' #Use: if admin in [role.id for role in message.author.roles]:

Token = '' #Bot Token
client = commands.Bot(command_prefix = 'z')
client.remove_command('help')

#This will send the Message in the Console
@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='https://GameLegendz.net'))
	print('Ready for Duty')
	print(client.user.name)

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command()
async def help():
	embed = discord.Embed(
		colour = discord.Colour.orange()
	)

	embed.set_author(name='Help')
	embed.add_field(name='ping', value='Returns Pong!')
	embed.add_field(name='echo (Insert Fart Joke here)', value='Returns what the User said')


	await client.say(embed=embed)

client.run(Token)