import discord


async def sendMessage(message):
    try:
        response = "https://tenor.com/view/cat-nuh-uh-meow-sniff-incorrect-gif-11442321997337963097"
        await message.channel.send(response)
    except Exception as e:
        print(e)


def runBot():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if client.user.mentioned_in(message):
            await sendMessage(message)



    client.run("MTIxODMxMjM5NzAzOTg2NTkwNw.GzAQ-h.vZxGF1AG34AsMVFk2YL79ixcHyCS2vj7x-AB5E")
