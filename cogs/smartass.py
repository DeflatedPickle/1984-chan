from datetime import datetime

from better_profanity import profanity
from discord import Message
from discord.ext.commands import Cog


class CogSmartAss(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: Message):
        await self.bot.wait_until_ready()

        channel = self.bot.get_channel(message.channel.id)
        m = ""

        if "literally 1984" in message.content.lower():
            m = f"Actually, I hate to be that person, but it's {datetime.now().year}, not 1984." \
                      "There is no censorship going on here. It's all in your head"

        if "1984-chan" in map(lambda x: x.name, message.mentions) and profanity.contains_profanity(message.content):
            m = "Watch it, you"

        if m:
            await message.reply(content=m)
