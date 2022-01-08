import discord 
from discord.ext import commands
import random

from utils import get_links
from info import TOKEN

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

bot.load_extension('cogs.bonk_command')
bot.load_extension('cogs.help_command')
bot.load_extension('cogs.leaderboard_command')

@bot.user_command(name="Bonk this person")
async def callbackname(ctx, member : discord.Member):
    desc = f"**{ctx.author.display_name}** bonked **{member.display_name}**"
    embed = discord.Embed(description = desc)

    bonks = await get_links()
    embed.set_image(url=random.choice(bonks))

    await ctx.respond(embed=embed)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing,name='Bonk help'))

bot.run(TOKEN)