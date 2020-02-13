
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
import typing

@bot.event
async def on_ready():
	print ("Logged")

@bot.command(pass_context= True)
async def топер(ctx, arg: str):
	author = ctx.message.author
	await ctx.send(f"{author.mention} сам ты "+ arg)
	

@bot.command(pass_context= True)
async def add(ctx, a: int,b: int):
	await ctx.send(a + b)

@bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):   
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        	

@bot.command()
@commands.has_permissions(manage_roles= True)
async def mute(ctx, member:discord.Member):
	mute_role = discord.utils.get(ctx.message.guild.roles, name= "Muted")
	await member.add_roles(mute_role)

bot.run("NjU5OTYyNzU0MDEwMTg1NzU0.XkTa5g.4sygeI6Z9YZfmmojrD1azFFpH8U")
    	
 

	



