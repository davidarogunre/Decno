import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import pyjokes
from random import randint
import asyncio
from discord_slash import SlashCommand
load_dotenv()
Token = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix="!", intents = intents) 
id1 = 962336520101064794

def Guild(id):
    return bot.get_guild(id)
@bot.event
async def on_ready():
    print('Connected')

@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome to Our Discord Channel", description="Welcome to David's Discord channel where he does amazing things", color= 0x00FFFF)
    await member.send(embed=embed)
@bot.command(name='joke', help="To get science and technology jokes")
async def joke(ctx):
    jokes = pyjokes.get_joke(language='en', category="neutral")
    await ctx.send(f"`{jokes}`")
def get_message(guild_connection):
    member_count = guild_connection.member_count-1
    if member_count == 1:
        return (f"There is {member_count} member")
    elif member_count > 1 or member_count == 0:
        return (f"There are {member_count} members")


@bot.command(name='users', help='Number of users')
async def users(ctx):
    channels = "bot-commands"
    if str(ctx.channel) == channels:
        server1 = Guild(id1)
        await ctx.send(f"`{get_message(server1)}`")
    else:
        await ctx.send("`You cannot use this command in this channel, go to #bot-commands`")


@bot.command(name="send", help="Send messages to users")
async def send(ctx, member: discord.Member, * ,text):
    await member.send(text)
    await ctx.send('Your message has sent')

@bot.command(name="sharefile", help="Helps to share files")
async def sharefile(ctx, file):
    await ctx.send(file=discord.File('C:/Users/Itari/Desktop' + f'/{file}'))

options = ['rock', 'paper', 'scissors']

@bot.command(name="rps", help="Play a rock paper scissors game")
async def rps(ctx, human):
    if str(ctx.channel) == 'rock-paper-scissors':
        choice = randint(0,2)
        computer = options[choice]
        if human.lower() == 'rock':
            if computer == 'rock':
                await ctx.send('It\'s a tie')
            elif computer == 'paper':
                await ctx.send('You lost')
            elif computer == 'scissors':
                await ctx.send('You won')
        elif human.lower() == 'paper':
            if computer == 'rock':
                await ctx.send('You win')
            elif computer == 'paper':
                await ctx.send('It\'s a tie')
            elif computer == 'scissors':
                await ctx.send('You lost')
        elif human.lower() == 'scissors':
            if computer == 'rock':
                await ctx.send('You lost')
            elif computer == 'paper':
                await ctx.send('You won')
            elif computer == 'scissors':
                await ctx.send('It\'s a tie')
    else:
        await ctx.send('You can only play rock paper scissors in #rock-paper-scissors')
slash = SlashCommand(bot, sync_commands = True)
@slash.slash(description='pingpong')
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name='wiggle', help="wiggle")
async def wiggle(ctx, wiggle):
    value = randint(20, 80)
    for i in range(0, value):
        global spaces
        if i<value/2:
            space = ' '*i
            spaces = space
        elif i>=value/2:
            length = len(spaces)
            space = ' '*(length-1)
            spaces = space
        await ctx.send(f"`{spaces}{wiggle}`")
        
        
bot.run(Token)