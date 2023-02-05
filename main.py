import discord
import os
import io
import aiohttp
from discord.ext import commands

import fun

#keep alive
from keep_alive import keep_alive

keep_alive()

#client = discord.Client()
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing, name='send /Photo'))


@client.command(name="photo")
async def Photo(ctx):
    imoji = fun.coolImoji()
    print("pic reqested..")
    await ctx.channel.send(
        ctx.author.mention + " මේ කොහෙද කියලා guess  කරන්න " + imoji, )
    async with aiohttp.ClientSession() as session:
        async with session.get("https://picsum.photos/400") as resp:
            if resp.status != 200:
                return await ctx.channel.send(
                    'අයේ පාරක් ට්‍රයි කරන්න යාලුවේ පොඩි කේස් එකක් ගියා')
            data = io.BytesIO(await resp.read())
            await ctx.channel.send(file=discord.File(data, 'cool_image.png'))


client.run(os.getenv('TOKEN'))
