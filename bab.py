import json
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

class Bab:
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Bab(client))
