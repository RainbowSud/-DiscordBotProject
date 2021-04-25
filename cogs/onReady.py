import discord
from discord.ext import commands

class OnReady(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("%help"))
        print("Bot is ready.")


def setup(client):
    client.add_cog(OnReady(client))
