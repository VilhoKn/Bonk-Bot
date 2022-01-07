import discord 
from discord.ext import commands
from info import TOKEN

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

bot.load_extension('cogs.bonk_command')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)