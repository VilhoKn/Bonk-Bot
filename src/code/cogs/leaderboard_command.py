import discord
import random
from discord.commands import slash_command
from discord.ext import commands

import utils

class Leaderboard(commands.Cog):
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
                leader_board = {}
                total = []
                desimaali = 0.1
                
                for i in data["bonk"]:
                    if i == "total":
                        continue
                    splitted = i.split("'")
                    username = splitted[1]
                    _id = int(splitted[-2])
                    mem = self.bot.get_user(_id)
                    if not mem:
                        continue
                    key = data["bonk"][i]
                    print(leader_board.values())
                    if key in leader_board.keys():
                      print("key in")
                      key += desimaali
                      desimaali += 0.1
                    leader_board[key] = _id
                    total.append(key)

                total = sorted(total, reverse=True)
                print(total)
                desc = ""
                index = 1
                for amt in total:
                    _id = leader_board[amt]
                    print(amt)
                    showable = int(amt) if isinstance(amt, float) else amt
                    
                    member = self.bot.get_user(_id)
                    name = member.name
                    desc += f"**{name}**: {showable}\n"
                    if index == 5:
                        break
                    else:
                        index += 1

                embed = discord.Embed(title="Bonk Leaderboard",description = desc)
                await message.channel.send(embed=embed)
                try:
                    await utils.update_commands("leaderboard", message.author)
                except Exception as e:
                    print("Error: " + e)


def setup(bot):
    bot.add_cog(Leaderboard(bot))
