from discord.abc import User
from discord.ext.commands import Cog


# noinspection PyUnusedLocal
class CogUser(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_user_update(self, before: User, after: User):
        await self.bot.wait_until_ready()
