import discord
import time
from discord.ext import commands

class purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    def is_it_me(ctx):
        return ctx.author.id == 194439943689469952

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=(amount+1))
        await ctx.send(f"{amount} messages purged")
        time.sleep(.5)
        await ctx.channel.purge(limit=1)

    @commands.command()
    @commands.check(is_it_me)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=(amount + 1))
        await ctx.send(f"{amount} messages purged")
        time.sleep(.5)
        await ctx.channel.purge(limit=1)


def setup(client):
    client.add_cog(purge(client))