import discord
from discord import app_commands
from services.downloadService import compress_video, download_file, wait_for_file
import config
import os

class DownloadCog(discord.ext.commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="download", description="Download media from link")
    @app_commands.describe(download_link="Link from which media is downloaded")
    async def download(self, interaction: discord.Interaction, download_link: str):

        await interaction.response.defer()

        file_path = download_file(download_link)

        if file_path:
            print(f"Downloaded {file_path}")

            if not wait_for_file(file_path):
                await interaction.followup.send("File download timed out.")
                return

            print(f"File size: {os.path.getsize(file_path)} bytes")

            if os.path.getsize(file_path) > config.MAX_FILE_SIZE_BYTES:
                print("Compressing file")

                compressed_path = compress_video(file_path)

                if os.path.getsize(compressed_path) <= config.MAX_FILE_SIZE_BYTES:
                    await interaction.followup.send(file=discord.File(compressed_path))
                else:
                    await interaction.followup.send("Compressed file is still too large to send.")

                os.remove(compressed_path)
            else:
                await interaction.followup.send(file=discord.File(file_path))

        else:
            await interaction.followup.send("Failed to download video.")

async def setup(bot):
    await bot.add_cog(DownloadCog(bot))