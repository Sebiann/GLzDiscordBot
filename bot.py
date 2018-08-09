import os
from os.path import join, dirname
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
import sys

#Load the .env File
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

Token = os.getenv('Token')
owner = os.getenv('owner')
admin = '439729155693740032'

client = commands.Bot(command_prefix = os.getenv('prefix'))
client.remove_command('help')

extensions = ['main', 'mc']

#This will send the Message in the Console
@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name=os.getenv('presence'), type=0))
	print('Ready for Duty')
	print(client.user.name)

@client.command
async def load(extension):
	try:
		client.load_extension(extension)
		print('Loaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be loaded [{}]'.format(extension, error))

@client.command
async def unload(extension):
	try:
		client.unload_extension(extension)
		print('Unloaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be unloaded [{}]'.format(extension, error))

if __name__ == '__main__':
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as error:
			print('{} cannot be loaded [{}]'.format(extension, error))

@client.command()
async def help():
	em = discord.Embed(title="Help", color=0x992d22).add_field(name='ping', value='Returns Pong!').add_field(name='echo (Insert Fart Joke here)', value='Returns what the User said').set_footer(text="These only Work in #commands")
	await client.say(embed=em)

@client.command(pass_context=True)
async def stop(ctx):
	if ctx.message.author.id == owner:
		sys.exit()
	else:
		await client.say('U are not the Owner')

client.run(Token)
