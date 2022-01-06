import discord
import random
from discord.commands import slash_command
from discord.ext import commands


class Bonk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return

        split_message = message.content.split(" ")
        if split_message[0].lower() == "bonk":
            mention_string = split_message[1]
            if mention_string[0] == "<" and mention_string[-1] == ">":
                _id = int(mention_string.replace("<", "").replace("@", "").replace(">", "").replace("!", ""))
                member = message.guild.get_member(_id)

                if not member: return

                desc = f"{ctx.author.display_name} BONKED {member.display_name}"
                embed = discord.Embed(description = desc)

                bonks = await get_links()
                embed.set_image(random.choice(bonks))

                await ctx.send(embed=embed)

    async def get_links():
        with open("../../files/text/bonk_links.txt", "r") as f:
            f_lines = f.readlines()
            BONKS = []
            for i in f_lines:
                BONKS.append(i.strip("\n"))
        return BONKS


def setup(bot):
    bot.add_cog(Bonk(bot))