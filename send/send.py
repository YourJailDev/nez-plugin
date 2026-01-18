import discord
from discord.ext import commands

class CustomEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="send")
    async def send_embed(self, ctx, title: str, *, description: str):
        """
        Sends an embed with a custom title, description,
        and any images attached to the message.
        Usage: .send MyTitle This is the description
        (attach images when sending the command)
        """

        attachments = ctx.message.attachments

        # If no images are attached, just send one embed
        if not attachments:
            embed = discord.Embed(
                title=title,
                description=description,
                color=0xB4175E
            )
            await ctx.send(embed=embed)
            return

        # If images ARE attached, send one embed per image
        for i, attachment in enumerate(attachments):
            if attachment.content_type and attachment.content_type.startswith("image/"):
                embed = discord.Embed(
                    title=title if i == 0 else None,  # title only on first embed
                    description=description if i == 0 else None,
                    color=0xB4175E
                )
                embed.set_image(url=attachment.url)
                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CustomEmbed(bot))
