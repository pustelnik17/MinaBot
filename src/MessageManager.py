import RandomGifManager


async def sendMessage(message):
    try:
        response = RandomGifManager.getRandomGif("https://giphy.com/search/cat")
        await message.channel.send(response)
    except Exception as e:
        print(e)
