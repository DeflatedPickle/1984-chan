from discord import Guild
from discord.ext.commands import Cog

from config import read_config, write_config


# noinspection PyUnusedLocal
class CogGuild(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_guild_join(self, guild: Guild):
        await self.bot.wait_until_ready()

        config = read_config()

        config[guild.id] = {
            "channel": None,
        }

        write_config(config)

    @Cog.listener()
    async def on_guild_update(self, before: Guild, after: Guild):
        await self.bot.wait_until_ready()
