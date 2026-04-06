import discord
import asyncio
import config
from discord.ext import commands
from discord import app_commands


class LoaderBot(commands.Bot):

    def __init__(self, intents, command_prefix="!"):
        super().__init__(intents=intents, command_prefix=command_prefix)

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == "!ping":
            await message.channel.send("pong")

    # Setup hook for command cogs
    async def setup_hook(self):
        await self.load_extension("cogs.downloadCog")

        await self.tree.sync()

        

async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = LoaderBot(intents=intents)
    await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())