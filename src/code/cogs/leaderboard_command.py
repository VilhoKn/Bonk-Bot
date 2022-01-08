import discord
import random
from discord.commands import slash_command
from discord.ext import commands

import utils

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
            leaderboard_string = split_message[1]
            if leaderboard_string.lower() == "leaderboard" or leaderboard_string.lower() == "leader":
                data = await utils.get_command_usage()
                winners = {}
                for i in data["bonk"]:
                    splitted = i.split("'")
                    username = splitted[0]
                    _id = int(splitted[-1])
                    mem = self.bot.get_user(_id)
                    
                desc = f""
                embed = discord.Embed(description = desc)
                await message.channel.send(embed=embed)
                try:
                    await utils.update_commands("help", message.author)
                except Exception as e:
                    print("Error: " + e)


def setup(bot):
    bot.add_cog(Help(bot))