import discord
from discord.ext import commands
import random

class whatchamp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def whatchamp(self, ctx):
        champ = [
            'garen',
            'chogath',
            'nasus',
        ]
        await ctx.send(random.choice(champ))

    @commands.command()
    async def ppe(self, ctx):
        char = [
            'wizard',
            'priest',
            'archer',
            'rogue',
            'warrior',
            'necromancer',
            'assassin',
            'huntress',
            'knight',
            'ninja',
            'sorcerer',
            'mystic',
            'trickster',
            'paladin',
            'samurai',
            'bard',
        ]
        await ctx.send(random.choice(char))

def setup(client):
    client.add_cog(whatchamp(client))