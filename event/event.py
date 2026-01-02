import discord
from discord.ext import commands
from datetime import datetime, timezone

class EventCreator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="event")
    @commands.has_permissions(manage_events=True)
    async def create_event(
        self,
        ctx,
        name: str,
        description: str,
        start_time: str,
        end_time: str
    ):
        """
        Usage:
        ?event "Name" "Description" 2026-01-03T18:00 2026-01-03T20:00
        """

        guild = ctx.guild
        if not guild:
            return await ctx.send("❌ This command must be used in a server.")

        # ⏰ Parse timestamps
        try:
            start = datetime.fromisoformat(start_time).replace(tzinfo=timezone.utc)
            end = datetime.fromisoformat(end_time).replace(tzinfo=timezone.utc)
        except ValueError:
            return await ctx.send(
                "❌ Invalid time format.\n"
                "Use: `YYYY-MM-DDTHH:MM` (example: 2026-01-03T18:00)"
            )

        if end <= start:
            return await ctx.send("❌ End time must be after start time.")

        event = await guild.create_scheduled_event(
            name=name,
            description=description,
            start_time=start,
            end_time=end,
            privacy_level=discord.PrivacyLevel.guild_only,
            entity_type=discord.EntityType.external,
            location="Server Event"
        )

        await ctx.send(f"✅ **Event created:** `{event.name}`")

async def setup(bot):
    await bot.add_cog(EventCreator(bot))
