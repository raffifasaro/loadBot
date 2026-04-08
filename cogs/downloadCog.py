import discord
from discord import app_commands
from services.downloadService import download_file

class DownloadCog(discord.ext.commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="download", description="Download media from link")
    @app_commands.describe(download_link="Link from which media is downloaded")
    async def download(self, interaction: discord.Interaction, download_link: str):
        file_path = download_file(download_link)
        if file_path:
            await interaction.response.send_message(f"Downloaded {file_path}")
        else:
            await interaction.response.send_message("Failed to download video.")

async def setup(bot):
    await bot.add_cog(DownloadCog(bot))