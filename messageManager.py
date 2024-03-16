import randomGifManager


async def sendMessage(message):
    try:
        response = randomGifManager.getRandomGif("https://tenor.com/en-GB/search/cat-reaction-gifs")
        await message.channel.send(response)
    except Exception as e:
        print(e)
