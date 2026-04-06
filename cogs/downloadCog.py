import discord
from discord import app_commands

class DownloadCog(discord.ext.commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="download", description="Download media from link")
    async def download(self, interaction: discord.Interaction):
        await interaction.response.send_message("Downloading media")

async def setup(bot):
    await bot.add_cog(DownloadCog(bot))