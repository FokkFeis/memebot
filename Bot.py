import discord
from discord.ext import commands
import asyncio
import os
import random

description = "Simple meme bot."

bot = commands.Bot(command_prefix="please ", description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context = True)
async def meme(context):
    meme_list = os.listdir("./memes")
    rand_numb = random.randint(0, len(meme_list)-1)
    meme = meme_list[rand_numb]
    await bot.send_file(context.message.channel,fp="./memes/"+meme ,filename=meme, content="aah, fresh meme!")

@bot.command(pass_context = True)
async def delaware(context):
    if context.message.author.id == ("160822173446045697"):
        await bot.say(context.message.author.mention + " is from delaware and therefore sucks balls")
    else:
        await bot.say(context.message.author.mention + " is not from delaware and is therefore cool B)")

bot.run("MjgxNzgyNDg0ODA1NDg0NTQ0.C9JXrA.VisWCc4R2_6EyrBxnk-Alogc1mU")