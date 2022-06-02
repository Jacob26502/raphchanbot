import asyncio
import os
import io
import random as random
import re
import sched
import time
import typing
from datetime import datetime
import discord
from discord.ext import tasks, commands
from discord.ext.commands import cooldown
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix='/')
script_dir = os.path.dirname(__file__)
print(time.time())
class DiscordBot():

    @bot.event
    async def on_ready():
        await bot.change_presence(status=discord.Status.idle)  ##TODO: REMOVE this when going back online ##################
        print(time.time())
        print(bot.user)

    @bot.command(name='raphsay')
    async def raphsay(ctx):
       await ctx.send("Rafu!")




bot.run(os.environ.get("DISCORD_BOT_SECRET"), reconnect=True)
