import discord
import asyncio
import config

class VideoBot(discord.Client):

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == "!ping":
            await message.channel.send("pong")


async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = VideoBot(intents=intents)
    await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())