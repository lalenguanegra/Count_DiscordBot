import discord 
import sys 
import subprocess 
from subprocess import call 
from discord.ext import commands 
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_command_error(ctx, error): 
  await ctx.send(f"An error occurred: {str(error)}")

@bot.command() 
async def submit(ctx, *args): 
  userInput = ' '.join(args) 
  uiCount = userInput.count('a') 
  uiCount2 = userInput.count('A') 
  await ctx.send("You said: \n" + userInput) 
  await ctx.send("There are:\n") 
  sum = (uiCount + uiCount2) 
  await ctx.send(sum) 
  await ctx.send("A's present.") 

bot.run('token)
