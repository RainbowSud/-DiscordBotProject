import discord
import json
from datetime import datetime
from discord.ext import commands

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Help'])
    async def help(self, ctx, com = " "):
        user = ctx.message.guild
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        if com == " ":
            embed = discord.Embed(title="Help Menu", color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name=f"{prefixes[str(user.id)]}help",
                            value="Brings up this menu",
                            inline=False)
            embed.add_field(name=f"{prefixes[str(user.id)]}wish",
                            value="Simulates a 10x wish of the requested genshin impact banner",
                            inline=False)
            embed.add_field(name=f"{prefixes[str(user.id)]}purge",
                            value="Purges that number of messages",
                            inline=False)
            embed.add_field(name=f"{prefixes[str(user.id)]}critcalc",
                            value="Compares 2 different sets of crit rate and dmg to see which is better",
                            inline=False)
            embed.add_field(name=f"{prefixes[str(user.id)]}changeprefix",
                            value="Changes the bots prefix for your server",
                            inline=False)
            embed.add_field(name=f"{prefixes[str(user.id)]}reminder",
                            value="Allows you to set a reminder for X amount of time.",
                            inline=False)
            embed.set_footer(
                text=f"{prefixes[str(user.id)]}help (command name) to get more info on a command",
                icon_url = f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)
        elif com == 'help':
            embed = discord.Embed(title="Help Menu", color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name=f"{prefixes[str(user.id)]}help",
                            value="Usage: help",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)
        elif com == 'wish':
            embed = discord.Embed(title="Help Menu", color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name=f"{prefixes[str(user.id)]}wish",
                            value="Usage: wish venti for venti, klee for klee, tartaglia for tartaglia, leave empty for standard."
                                  " Make sure the char name is lowercase",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)
        elif com == 'purge':
            embed = discord.Embed(title="Help Menu", color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name=f"{prefixes[str(user.id)]}purge",
                            value="Usage: purge",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)
        elif com == 'critcalc':
            embed = discord.Embed(title="Help Menu", color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name=f"{prefixes[str(user.id)]}critcalc",
                            value="Usage: critcalc <CR1> <CD1> <CR2> <CD2>\nDon't put <> when adding your numbers",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)
        elif com == 'changeprefix':
            embed = discord.Embed(title="Help Menu", color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name=f"{prefixes[str(user.id)]}changeprefix",
                            value="Usage: changeprefix <new prefix>",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)
        elif com == 'reminder':
            embed = discord.Embed(title="Help Menu", color=0x55a7f7, timestamp=datetime.utcnow())
            embed.add_field(name=f"{prefixes[str(user.id)]}reminder",
                            value="Usage: reminder #$ 'message', where # is a number, and $ is either"
                                  " d,h,m,s for days, hours, minutes, or seconds. "
                                  "Time can't be less then 1 second or exceed 90 days",
                            inline=False)
            embed.set_footer(
                text="Ganyu go brr",
                icon_url=f"{self.client.user.avatar_url}")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))