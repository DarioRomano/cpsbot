# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:38:15 2020

@author: Dario
"""

import discord

client = discord.Client()
waterlevels={}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('$help'):
        dm=yield message.author.create_dm()
        await dm.send('testerino')
    if message.content.startswith('$remindme'):
        args=message.content.split(' ')
        if args[1] == 's':
            return
        elif args[1] == 'p':
            
            return
        elif args[1] =='water':
            waterlevels[message.user]=args[2]
        
@client.event
async def on_reaction_add(reaction,user):
    if reaction.message.author==client.user:
        return

f=open('token.txt','r')
token=f.read();
f.close();
client.run(token)
