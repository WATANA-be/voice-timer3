import discord
from discord.ext import commands
import os
import traceback
client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_voice_state_update(before, after):
    print("ボイスチャンネルで変化がありました")


if(before.voice_channel is None):#入室時
    pretime_dict[after.name] = datetime.datetime.now()
else(after.voice_channel is None):#退出時
    duration_time = pretime_dict[before.name] - datetime.datetime.now()
    duration_time_adjust = int(duration_time.total_seconds()) * -1
    
reply_channel_name = "雑談"
reply_channel = [channel for channel in before.server.channels if channel.name == reply_channel_name][0]

reply_text = after.name + "　が　"+ before.voice_channel.name + "　から抜けました。　通話時間：" + str(duration_time_adjust) +"秒"

await client.send_message(reply_channel ,reply_text)

    
bot.run(token)
client.run("token")
