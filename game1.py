from SECRET import token
#import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def hackathon(ctx: commands.Context):
    await ctx.send("RUHACKS 2022")

#def mcquiz():
#  await ctx.send("Hello from a function")

bot.run(token)