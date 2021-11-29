import json
from json import JSONDecodeError

from discord import Intents, Activity, ActivityType
from discord.ext.commands import Bot
from discord_slash import SlashCommand

from cogs.guild import CogGuild
from cogs.message import CogMessage
from cogs.slash import CogSlash
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


@bot.event
async def on_ready():
    print(f"1984-chan is connected to {len(bot.guilds)} guilds")
    print("this is literally 1984")

    await bot.change_presence(activity=Activity(type=ActivityType.watching, name="you"))


bot.add_cog(CogMessage(bot, config))
bot.add_cog(CogGuild(bot, config))
bot.add_cog(CogUser(bot, config))

bot.add_cog(CogSlash(bot, config))

bot.run(botid)
