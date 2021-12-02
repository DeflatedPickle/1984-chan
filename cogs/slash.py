import discord
from discord.abc import GuildChannel
from discord.ext.commands import Cog
from discord_slash import SlashContext, SlashCommandOptionType
from discord_slash.cog_ext import cog_subcommand
from discord_slash.utils.manage_commands import create_option

from config import read_config, write_config


# noinspection PyUnusedLocal,PyShadowingBuiltins
class CogSlash(Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_subcommand(
        base="channel",
        name="set",
        description="Set a channel for this bot to post to (if unset, will post to current channel)",
        options=[
            create_option(
                name="channel",
                description="The id of the channel to use",
                option_type=SlashCommandOptionType.CHANNEL,
                required=True,
            )
        ],
        # base_permissions={k: [
        #     create_permission(k, SlashCommandPermissionType.ROLE, False),
        #     create_permission(bot.get_guild(k).owner_id, SlashCommandPermissionType.USER, True),
        # ] for k in read_config()},
        guild_ids=read_config(),
    )
    async def _channel(self, ctx: SlashContext, channel: GuildChannel):
        if ctx.author.id != self.bot.get_guild(ctx.guild_id).owner_id: return
        await self.bot.wait_until_ready()

        config = read_config()

        id = discord.utils.get(self.bot.get_guild(ctx.guild_id).channels, name=channel.name).id
        config[ctx.guild_id]["channel"] = id

        write_config(config)

        await ctx.send(f"Channel set to {self.bot.get_channel(id).name}")