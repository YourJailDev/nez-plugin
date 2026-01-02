import discord
from discord.ext import commands

class PresetEventEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
        embed = discord.Embed(
            title="Title",
            description=(
                "Hello"
            ),
            color=0x5865F2
        )

        embed.set_footer(text="myEurowings")
        await thread.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(PresetEventEmbed(bot))
