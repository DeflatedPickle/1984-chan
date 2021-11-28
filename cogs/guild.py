from discord import Guild
from discord.ext.commands import Cog


# noinspection PyUnusedLocal
class CogGuild(Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    @Cog.listener()
    async def on_guild_join(self, guild: Guild):
        await self.bot.wait_until_ready()

        self.config[guild.id] = {
            "channel": None,
        }

    @Cog.listener()
    async def on_guild_update(self, before: Guild, after: Guild):
        await self.bot.wait_until_ready()
