import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')





client.run('MTAxMzQ5MDU5NTA4MTIzNjU3MA.G097E3.ie-mfTQSAOeS4xt4tDhuvib0CLAVFFem39l7kU')