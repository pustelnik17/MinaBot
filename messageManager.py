import randomGifManager


async def sendMessage(message):
    try:
        response = randomGifManager.getRandomGif("https://giphy.com/search/cat")
        await message.channel.send(response)
    except Exception as e:
        print(e)
