import discord


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!help'):
        await message.channel.send('Hello!')
    if message.content.startswith('!apk'):
        await message.channel.send('Kamu Bisa Download Aplikasi Android WRT Disini : https://wrt.my.id/aplikasi-android-wrt/')


client.run('OTI3OTU2NTk0NTQzNjk3OTgw.YdRw7A.haOfwsvirCLiffBh9zwYtswtMdg')
