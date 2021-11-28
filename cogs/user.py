from discord.abc import User
from discord.ext.commands import Cog


# noinspection PyUnusedLocal
class CogUser(Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    @Cog.listener()
    async def on_user_update(self, before: User, after: User):
        await self.bot.wait_until_ready()
