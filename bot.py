import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
#client = discord.Client(intents=intents)

TOKEN = ''


description = '''Python Discord Bot'''
#command prefix is what you use to run the command

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

#this runs the command
@bot.command()
async def hello(ctx):
	await ctx.send('world')

@bot.command()
async def rickroll(ctx):
	await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')


bot.run(TOKEN)
