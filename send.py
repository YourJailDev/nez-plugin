import discord
from discord.ext import commands

class CustomEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="send")
    async def send_embed(self, ctx, title: str, *, description: str):
        """
        Sends an embed with a custom title and description.
        Usage: .send MyTitle This is the description
        """

        embed = discord.Embed(title=title, description=description, color=0x00FFAA)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CustomEmbed(bot))
