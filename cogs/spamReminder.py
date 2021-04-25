import discord
import asyncio
from datetime import datetime
from discord.ext import commands

class GenshinReminder(commands.Cog):

    def __init__(self, client):
        self.client = client

    def is_it_me(ctx):
        return ctx.author.id == 194439943689469952

    @commands.command()
    @commands.check(is_it_me)
    async def StartReminder(self, ctx, reminder):
        time = .7
        i = 0
        while i < 10:
            await asyncio.sleep(time)
            i += 1
            await ctx.send(f'{reminder}')


def setup(client):
    client.add_cog(GenshinReminder(client))