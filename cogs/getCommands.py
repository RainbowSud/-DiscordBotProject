import discord
import json
from discord.ext import commands
from datetime import datetime

class getCommands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def allTimeWishes(self, ctx):
        user = ctx.message.author
        with open('wishPity.json', 'r') as f:
            pity = json.load(f)
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
        embed.add_field(name="Your Wish",
                        value=f"\nAll Time Wishes = {pity[str(user.id)]['allTimeWishes']}"
                              f"\nApprox Money Spent = ${pity[str(user.id)]['allTimeWishes'] * 1.98}",
                        inline=False)
        embed.set_footer(
            text="Ganyu go brr",
            icon_url=f"{self.client.user.avatar_url}")
        with open('wishPity.json', 'w') as f:
            json.dump(pity, f, indent=4)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(getCommands(client))




