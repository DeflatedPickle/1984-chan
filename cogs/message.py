from datetime import datetime

from discord import Message, Embed, Colour
from discord.ext.commands import Cog
from better_profanity import profanity

from config import read_config


# noinspection PyUnusedLocal
class CogMessage(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot: return
        await self.bot.wait_until_ready()

        config = read_config()
        censor = config[message.guild.id]["censor"]

        if not censor or not profanity.contains_profanity(message.content): return

        embed = Embed(
            description=profanity.censor(message.content, censor_char="!"),
            colour=Colour.purple(),
            timestamp=datetime.now(),
        ) \
            .set_author(
            name=message.author.name,
            icon_url=message.author.avatar_url,
        ) \
            .set_footer(
            text="(censored)"
        )

        await message.delete()
        channel = self.bot.get_channel(message.channel.id)
        await channel.send(embed=embed)

    @Cog.listener()
    async def on_message_delete(self, message: Message):
        if message.author.bot: return
        await self.bot.wait_until_ready()

        config = read_config()
        c = config[message.guild.id]["channel"] or message.channel.id
        censor = config[message.guild.id]["censor"]

        embed = Embed(
            title=f"#{message.channel.name}",
            description=message.content if not censor else profanity.censor(message.content, censor_char="!"),
            colour=Colour.red(),
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

        config = read_config()

        c = config[before.guild.id]["channel"] or before.channel.id
        censor = config[before.guild.id]["censor"]

        embed = Embed(
            title=f"#{before.channel.name}",
            colour=Colour.orange(),
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
            value=before.content if not censor else profanity.censor(before.content, censor_char="!"),
            inline=False,
        ) \
            .add_field(
            name="after",
            value=before.content if not censor else profanity.censor(after.content, censor_char="!"),
            inline=False,
        )

        channel = self.bot.get_channel(c)
        await channel.send(embed=embed)
