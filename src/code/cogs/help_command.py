import discord
import random
from discord.commands import slash_command
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        
        split_message = message.content.split(" ")
		
        if len(split_message) < 2:
            return
        if split_message[0].lower() == "bonk":
            help_string = split_message[1]
            if help_string.lower() == "help":
                desc = f"**Bonk Bot** is a fun bot made to bonk people.\nUsing it is simple, just type `bonk @member`"
                embed = discord.Embed(description = desc)
                embed.set_footer(text="Pfp by BunnySimps#0001 • Developer Sivakka#4938")

                await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))