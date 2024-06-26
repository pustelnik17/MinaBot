import discord
import MessageManager
from API_KEY import apiKey


def runBot():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if client.user.mentioned_in(message):
            await MessageManager.sendMessage(message)

    client.run(apiKey)
