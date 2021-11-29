from datetime import datetime

from discord import Message, Embed
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
    async def on_message_edit(self, before: Message, after: Message):
        if before.content == after.content: return

        await self.bot.wait_until_ready()

        try:
            c = self.config[before.author.id]["channel"]
        except KeyError:
            c = before.channel.id

        embed = Embed(
            timestamp=datetime.now(),
        ) \
            .set_author(
            name=before.author.name,
            icon_url=before.author.avatar_url,
        ) \
            .set_footer(
            text="(edited)"
        ) \
            .add_field(
            name="before",
            value=before.content,
            inline=False,
        ) \
            .add_field(
            name="after",
            value=after.content,
            inline=False,
        )

        channel = self.bot.get_channel(c)
        await channel.send(embed=embed)
