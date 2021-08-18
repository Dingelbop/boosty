import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    print('{} said: {}'.format(message.author, message.content))
    command = message.content
    splitcommand = command.split()
    splitcommandlength = len(splitcommand)
    print(splitcommand)
    print(splitcommandlength)
    messageout = 'Hello!'
    if splitcommandlength == 1:
      await message.channel.send(messageout)
    else:
      splitcommand.pop(0)
      for s in splitcommand:
        messageout += ' ,{}'.format(s)
      await message.channel.send(messageout)


    

@client.event
async def on_message(message):
  if message.content.startswith('!ticket'):
    print('{} Opened a ticket'.format(message.author))
    messageout = 'You wanted to open a ticket. Write your message here:'
    embed = discord.Embed(title=messageout)
    await message.author.send(embed=embed)
  
@client.event
async def on_message(message):
  user = message.author
  role = discord.utils.find(lambda r: r.name == 'Advertiser',message.author.roles)
  if role in user.roles:
    if message.content.startswith('!ad'):
      ads = message.content.split(';')
      ad = ads[0].split()
      comment = ads[1]
      ad.pop(0)
      print(ad)
      faction = ad[0]
      roles = ad[1]
      if ad[2].find('<')!=-1:
        roles +=ad[2]
        if ad[3].find('<')!=-1:
          roles +=ad[3]
          pot=ad[4]
          realm=ad[5]
          runs = ad[6]
          key = ad[7]
        else:
          roles +=ad[2]
          pot=ad[3]
          realm=ad[4]
          runs = ad[5]
          key = ad[6]
      else:
        roles +=ad[2]
        pot=ad[3]
        realm=ad[4]
        runs = ad[5]
        key = ad[6]

      embed = discord.Embed(title='M+ run {}'.format(ad[0]),description='Roles: {}'.format(roles))
      embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
      embed.add_field(name='Boosters', value='-', inline=False)
      embed.add_field(name='Pot', value=pot, inline=True)
      embed.add_field(name='Booster cut', value='55000', inline=True)
      embed.add_field(name='Ad cut', value='60000', inline=True)
      embed.add_field(name='Dungeon', value=key, inline=False)
      embed.add_field(name='Runs', value=runs, inline=True)
      embed.add_field(name='Payment Realm', value=realm, inline=True)
      embed.add_field(name='Contact', value=message.author.name, inline=True)
      embed.add_field(name='Comment from advertiser:', value=comment, inline=False)
      await message.channel.send(embed=embed)
  
    





@client.event
async def on_reaction_add(reaction, user):
  print('{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))
  await reaction.message.channel.send('{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
  print('{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))
  await reaction.message.channel.send('{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))




client.run(os.environ['TOKEN'])

