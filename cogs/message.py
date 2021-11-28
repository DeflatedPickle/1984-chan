from datetime import datetime

from discord import Message, Embed, RawMessageUpdateEvent
from discord.ext.commands import Cog


# noinspection PyUnusedLocal
class CogMessage(Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    @Cog.listener()
    async def on_message_delete(self, message: Message):
        await self.bot.wait_until_ready()

        try:
            c = self.config[message.guild.id]["channel"]
        except KeyError:
            c = message.channel.id

        embed = Embed(
            description=message.content,
            timestamp=datetime.now(),
        ) \
            .set_author(
            name=message.author.name,
            icon_url=message.author.avatar_url,
        ) \
            .set_footer(
            text="(deleted)"
        )

        channel = self.bot.get_channel(c)
        await channel.send(embed=embed)

    # we're using the raw one as the message could be too old to be in the cache
    @Cog.listener()
    async def on_raw_message_edit(self, payload: RawMessageUpdateEvent):
        await self.bot.wait_until_ready()
