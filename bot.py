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





client.run('MTAxMzQ5MDU5NTA4MTIzNjU3MA.G2Rut6.iFLJO9e-kDNKi1-lMhvx784X9KzKI4ohEjlv5g')
