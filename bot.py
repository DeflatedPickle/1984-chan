from better_profanity import profanity
from discord import Intents, Activity, ActivityType
from discord.ext.commands import Bot
from discord_slash import SlashCommand

from cogs.smartass import CogSmartAss
from config import read_config, write_config, read_id

intents = Intents.default()
intents.members = True

bot = Bot(
    command_prefix="!",
    self_bot=True,
    help_command=None,
    intents=intents,
)
slash = SlashCommand(
    bot,
    sync_commands=True,
)


@bot.event
async def on_ready():
    print(f"1984-chan is connected to {len(bot.guilds)} guilds")
    print("this is literally 1984")

    config = read_config()

    for i in bot.guilds:
        if i.id not in config:
            config[i.id] = {
                "channel": None,
                "censor": False,
            }

    write_config(config)

    await bot.change_presence(activity=Activity(type=ActivityType.watching, name="you"))


if __name__ == "__main__":
    from cogs.message import CogMessage
    from cogs.slash import CogSlash

    profanity.load_censor_words()

    bot.add_cog(CogMessage(bot))
    bot.add_cog(CogSlash(bot))
    bot.add_cog(CogSmartAss(bot))

    bot.run(read_id())
