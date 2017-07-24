import discord
from discord.ext import commands
import asyncio
import os
import random
import json

description = "Simple meme bot."

bot = commands.Bot(command_prefix="please", description=description)
with open("links.json") as links:
        links = json.load(links)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def meme(message):
    meme_list = os.listdir("./memes")
    rand_numb = random.randint(0, len(meme_list)-1)
    m = meme_list[rand_numb]
    await bot.send_file(message.channel,fp="./memes/"+m ,filename=m, content="aah, fresh meme!")

async def list_attachments(message):
    await bot.send_message(message.channel, content = message.attachments)


@bot.event
async def on_message(message):
    if message.content.startswith("please meme"):
        meme(message)
    elif message.content.startswith("please list"):
        list_attachments(message)

bot.run("MjgxNzgyNDg0ODA1NDg0NTQ0.C9JXrA.VisWCc4R2_6EyrBxnk-Alogc1mU")
