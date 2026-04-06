import discord
import asyncio
import config
from discord import app_commands

class VideoBot(discord.Client):

    def __init__(self, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == "!ping":
            await message.channel.send("pong")

    async def setup_hook(self):
        @self.tree.command(name="download", description="Download media from link")
        async def download(interaction: discord.Interaction):
            await interaction.response.send_message("Downloading media")

        await self.tree.sync()

        

async def main():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = VideoBot(intents=intents)
    await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())