import discord
from discord.ext import commands
from config import settings
import math
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


def sub(x: float, y: float):
    return x - y

def sum(x: float, y: float):
    return x + y

def div(x: float, y: float):
    return x / y

def sqrt(x: float):
    return math.sqrt(x)

def mylt(x: float, y: float):
    return x * y

@bot.event
async def on_ready():
    print('Bot_calc к работе готов')

@bot.command()
async def команды(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} Доступны следующие действия после знака "!": \n!сложение\n!вычитание\n!деление\n!умножение\n!корень\nНапиши !сложение 2 2 ')

@bot.event
async def on_member_join(member):
    await member.send('Приветствую. Я великий математик, чтобы узнать, что я умею набери !команды')

    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == 'основной':
            await bot.get_channel(ch.id).send(f'{member}, круто, что ты с нами, проверь личку, там небольшой гайд!')

@bot.command()
async def сложение(ctx, x: float, y: float):
    res = sum(x, y)
    await ctx.send(f'Ответ: {res}')

@bot.command()
async def вычитание(ctx, x: float, y: float):
    res = sub(x, y)
    await ctx.send(f'Ответ: {res}')

@bot.command()
async def деление(ctx, x: float, y: float):
    res = div(x, y)
    await ctx.send(f'Ответ: {res}')

@bot.command()
async def корень(ctx, x: float):
    res = sqrt(x)
    await ctx.send(f'Ответ: {res}')

@bot.command()
async def умножение(ctx, x: float, y: float):
    res = mylt(x, y)
    await ctx.send(f'Ответ: {res}')


bot.run(settings['token'])
