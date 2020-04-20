# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:38:15 2020

@author: Dario
"""

import discord
import datetime
import threading,time
import holidays
from calendar import week

client = discord.Client()
waterlevels={}
timenow=datetime.datetime.now()
if timenow.isoweekday() <5:
    nextreminder=timenow
    
def timeUntilNextNotification(thetime:datetime)->int:
    if thetime.isoweekday() >5:
        nextreminder=datetime(year=thetime.year(),month=thetime.month(),)
        
def waterreminder():
    while True:
        now=datetime.datetime.now()
        for key in waterlevels.keys():
                if waterlevels[key] == 4:
                    key.create_dm().send('This is a friendly reminder to drink some water.')
        if now in holidays.Austria() or now.isoweekday()>5 or now.hour>17 or now.hour<9:
            time.sleep(60)
            continue
        elif (now.hour-1)%2==0 and now.minute==0:
            for key in waterlevels.keys():
                if waterlevels[key] == 1:
                    key.create_dm().send('This is a friendly reminder to drink some water.')
        elif now.minute==0:
            for key in waterlevels.keys():
                if waterlevels[key] == 2:
                    key.create_dm().send('This is a friendly reminder to drink some water.')
        elif now.minute == 0 or now.minute==30:
            for key in waterlevels.keys():
                if waterlevels[key] == 3:
                    key.create_dm().send('This is a friendly reminder to drink some water.')
        time.sleep(60)
waterthread= threading.Thread(target=waterreminder)
waterthread.start()

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
        helpfile=open('helpmessage.txt','r')
        helpmessage= helpfile.read()
        helpfile.close()
        dm= await message.author.create_dm()
        await dm.send(helpmessage)
    if message.content.startswith('$remindme'):
        print('got remindme msg')
        args=message.content.split(' ')
        print(args)
        if args[1] == 's':
            return
        elif args[1] == 'p':
            
            return
        elif args[1] =='w':
            print(int(args[2]))
            if args[2] == '0':
                del waterlevels[message.author]
            if int(args[2]) >0 and int(args[2])<=4:
                waterlevels[message.author]=int(args[2])
                print(str(message.author) +'subscribed with level '+args[2])
            else:
                print('could not match level')    
        
@client.event
async def on_reaction_add(reaction,user):
    if reaction.message.author==client.user:
        return

f=open('token.txt','r')
token=f.read();
f.close();
client.run(token)
