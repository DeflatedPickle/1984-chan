import json
from json import JSONDecodeError

from discord import Intents
from discord.ext.commands import Bot
from discord_slash import SlashCommand

from cogs.guild import CogGuild
from cogs.message import CogMessage
from cogs.user import CogUser

with open("token.txt") as f:
    botid = f.readline().strip()

with open("config.json", 'w+') as f:
    try:
        config = json.load(f)
    except JSONDecodeError:
        config = json.loads('{}')
        f.write("{}")

bot = Bot(
    command_prefix="!",
    self_bot=True,
    help_command=None,
    intents=Intents.default(),
)
slash = SlashCommand(bot)

bot.add_cog(CogMessage(bot, config))
bot.add_cog(CogGuild(bot, config))
bot.add_cog(CogUser(bot, config))

bot.run(botid)
