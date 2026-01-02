import discord
from discord.ext import commands

PRESET_EMBED = discord.Embed(
    title="Title",
    description=(
        "Hello"
    ),
    color=0x5865F2
)
PRESET_EMBED.set_footer(text="myEurowings")


class EventEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="event")
    async def send_event_embed(self, ctx):
        """Manually sends the preset event embed"""
        await ctx.send(embed=PRESET_EMBED)

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
        await thread.channel.send(embed=PRESET_EMBED)


async def setup(bot):
    await bot.add_cog(EventEmbed(bot))
