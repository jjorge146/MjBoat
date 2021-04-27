import discord
from discord.ext import commands
import time

client = discord.Client()
url = 'https://www.w3schools.com/python/demopage.php'

payload = {
    'content': "gamer"
}

header = {
    'authorization': 'Pm3hNvqIp2u-WwC1EuWgSbsC3cS_PAZR'
}

async def killkenny(message):
    await message.channel.send("SHUT THE FUCK UP")
    await message.author.voice.channel.connect()
    time.sleep(1)
    gamer = await message.guild.fetch_member(234395307759108106)
    await gamer.edit(voice_channel=None)
    await leave(message)

async def leave(message):
    server = message.guild.voice_client
    await server.disconnect()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    gamer = message.content.lower()

    #url = 'https://discord.com/api/v8/channels/' + str(message.channel.id) + '/webhooks'
    #x = requests.post(url, data=payload, headers=header)
    #print(x.text)


    if gamer.find('doing') != -1:
        string = gamer
        user = message.author
        index = string.find('doing') + 4
        string = string.split('doing')
        await message.channel.send("I'm" + string[1])

    if gamer.find("-play fart with extra reverb") != -1:
        await killkenny(message)

    if gamer.find('-play https://youtu.be/hr7GyFM7pX4') != -1:
        await killkenny(message)

    if gamer.find("-p fart with extra reverb") != -1:
        await killkenny(message)

    if gamer.find("join me bitch") != -1:
        await message.channel.send("ok")
        gamer = await message.author.voice.channel.connect()
        await message.author.edit(voice_channel=None)

client.run('ODMyMDA0MzgzOTIyNDU0NTM4.YHdedw.psGZCz_8d7hyi-Y6B5KZZMvO-Xc')