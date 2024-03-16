import discord
import messageManager


def runBot():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if client.user.mentioned_in(message):
            await messageManager.sendMessage(message)

    client.run("MTIxODMxMjM5NzAzOTg2NTkwNw.GzAQ-h.vZxGF1AG34AsMVFk2YL79ixcHyCS2vj7x-AB5E")
