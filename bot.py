import os
import random
import discord
import time
from dotenv import load_dotenv
from discord.ext import commands

chamber = random.randint(1, 6)
bullet = 1
load_dotenv()

client = commands.Bot(command_prefix = '.')
TOKEN = ''
GUILD = os.getenv('')
print("Bot is now Online")

#just to kick
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} have been kicked sucessfully")
  
  
#just to ban
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} have been bannned sucessfully")

#just to unban

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user} have been unbanned sucessfully")
    return
    
#the gun game
@client.event
async def on_message(message):
    if message.content.startswith('.spin'):
            await message.channel.send("%s spins the cylinder of the revolver with 1 bullet in it..." % message.author)

            global chamber
            global bullet
            chamber = random.randint(1,6)
            bullet = 1
    if message.content.startswith('.pull'):
        if chamber == bullet:
            await message.channel.send("%s placed the muzzle against their head and pulls the trigger..." % message.author)
            time.sleep(2)
            await message.channel.send("%s pulled the trigger and was not lucky. R.I.P." % message.author)
            await message.channel.send("...their brain gets splattered all over the wall.")
            game_active = False
        else:
            await message.channel.send("%s placed the muzzle against their head and pulls the trigger..." % message.author)
            time.sleep(2)
            await message.channel.send("%s pulled the trigger and nothing happened." % message.author)
    












client.run(TOKEN)
