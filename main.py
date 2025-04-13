import discord
from config import token
from discord.ext import commands
import os
import asyncio


bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("bot is online")
    try:
        synced_commands = await bot.tree.sync()
        print(f"{len(synced_commands)} Commands")
    except Exception as e:
        print("An error with syncing with application commands", e)
    

async def load_cogs():
    for extension in os.listdir("./cogs"):
        if extension.endswith(".py"):
            await bot.load_extension(f"cogs.{extension[:-3]}")
            


async def main():
    async with bot:
        await load_cogs()
        await bot.start(token)
        


asyncio.run(main())


        