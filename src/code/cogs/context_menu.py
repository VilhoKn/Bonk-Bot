import discord
from discord.commands import user_command

from utils import get_links


class ContextMenuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @user_command(name='Bonk')
    async def _bonk_user(self, ctx, member):
        desc = f"**{ctx.author.display_name}** BONKED **{member.display_name}**"
        embed = discord.Embed(description = desc)

        bonks = await get_links()
        embed.set_image(url=random.choice(bonks))

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ContextMenuCog(bot))