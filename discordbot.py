import discord
from discord.ext import commands
import os
import traceback
client = discord.Client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@client.event()
async def on_voice_state_update(before, after):
    channel = client.get_channel('738726518292742247')
    await channel.send('もくもく会が始まったようです！')


bot.run(token)
