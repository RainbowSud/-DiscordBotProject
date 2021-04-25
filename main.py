import discord
import json
import os
from discord.ext import commands

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = get_prefix, intents = intents)
client.remove_command('help')
os.chdir(r'C:\Users\Benjamin Swenson\PycharmProjects\DiscordBotProject')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

def is_it_me(ctx):
    return ctx.author.id == 194439943689469952


@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.check(is_it_me)
async def reload(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.unload_extension(f'cogs.{filename[:-3]}')
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f'cogs.{filename[:-3]}')
    await ctx.send("All cogs reloaded")



client.run("NzkxMDcyMjczMTQxNTk2MTkw.X-J1dw.3PzMmzyYfAhm-_hqRfQbCvD7bYg")
