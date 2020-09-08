from discord.ext import commands
import os
import traceback

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
    
    
const mainChannelId = [738726518292742247];

client.on('voiceStateUpdate', (oldGuildMember, newGuildMember) =>{
 if(oldGuildMember.voiceChannelID === undefined && newGuildMember.voiceChannelID !== undefined){
   if(client.channels.get(newGuildMember.voiceChannelID).members.size == 1){
     if (newGuildMember.voiceChannelID == "725595164105768984") {
       newGuildMember.voiceChannel.createInvite({"maxAge":"0"})
         .then(invite => sendMsg(
           mainChannelId, "<@" + newGuildMember.user.id +"> が通話を開始しました！\n" + invite.url
         ));
     }
   }
 }
});


bot.run(token)
