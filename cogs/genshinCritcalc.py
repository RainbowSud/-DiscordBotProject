import discord
from discord.ext import commands
from datetime import datetime

class critcalc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def critcalc(self, ctx, cr, cd, cr2, cd2):
        if int(cr) > 100:
            cr = 100
        if int(cr2) > 100:
            cr2 = 100
        crits = int(cr)
        noncrits = 100 - int(cr)
        dmg = 100 + int(cd)
        crits2 = int(cr2)
        noncrits2 = 100 - int(cr2)
        dmg2 = 100 + int(cd2)
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
        embed.add_field(name="CritCalc", value=f"Assuming 100 hits, with 100 base dmg:\nFirst is: {(dmg * crits) + (100 * noncrits)}\nSecond is: {(dmg2 * crits2) + (100 * noncrits2)}\n",
                        inline=False)
        embed.set_footer(
            text="Ganyu go brr",
            icon_url=f"{self.client.user.avatar_url}")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(critcalc(client))