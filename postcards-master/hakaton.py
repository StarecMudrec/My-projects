import random
import discord
from discord.ext import commands
from postcard import Postcard

intents = discord.Intents(messages=True, guilds=True)
intents.typing = True
intents.presences = True
intents.message_content = True

config = {
    'token': 'MTA1Nzk0OTA2MTI4Nzc4ODY0NQ.GXgulM.xEvkNQe3b0q1UBqjLI5tqX_k2YtK-hwDKSWTe8',
    'prefix': 'Скинь мне пожалуйста ',
}

bot = commands.Bot(command_prefix=config['prefix'], intents = intents)

@bot.command()
#@commands.has_role("KIBRIK")
async def новогоднюю_гифку(ctx):
    postcard = Postcard()
    postcard.draw_and_save('Card.gif')
    await ctx.send(file = discord.File('Card.gif'))

@bot.command()
#@commands.has_role("KIBRIK")
async def Большой_Жопа(ctx):
    await ctx.send('JOPA')

bot.run(config['token'])