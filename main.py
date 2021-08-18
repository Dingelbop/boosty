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
    await message.channel.send('Hello!<br>asdf')

@client.event
async def on_reaction_add(reaction, user):
  print('{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))
  await reaction.message.channel.send('{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
  print('{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))
  await reaction.message.channel.send('{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))




client.run(os.environ['TOKEN'])

