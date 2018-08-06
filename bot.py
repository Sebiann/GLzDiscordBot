import discord
from discord.ext import commands
import random

#Permissions
owner = '187239212544688128' #Use: if message.author.id == owner:
admin = '439729155693740032' #Use: if admin in [role.id for role in message.author.roles]:

Token = '' #Bot Token
client = commands.Bot(command_prefix = 'z')
client.remove_command('help')

extensions = ['main', 'mc']

#This will send the Message in the Console
@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='GLz Bot', type=0))
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
	em = discord.Embed(title="Help", description="Still Testing", color=0x992d22).set_author(name="Help2", icon_url=ctx.message.author.avatar_url).add_field(name='ping', value='Returns Pong!').add_field(name='echo (Insert Fart Joke here)', value='Returns what the User said').set_footer(text="These only Work in ")
	await client.say(embed=em)

client.run(Token)
