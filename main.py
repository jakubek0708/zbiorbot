#importing libraries
import discord
import asyncio
from discord.ext import *
from discord.ext import commands
from discord import Color
from dotenv import load_dotenv
# from mcstatus import MinecraftServer
import random
import time
import os
import ffmpeg

#discord token loading
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#defined client prefix
client = commands.Bot(command_prefix = '!')

#minecraft server lookup
# server = MinecraftServer.lookup("188.34.196.6")

#brawl stars check
def not_brawl_stars_check(message):
    return not "brawl stars" in message.lower()

#events:

@client.event #when bot is turned on
async def on_ready():
    print("zbior gotowy")
    await client.change_presence(activity=discord.Game(name="komendy: !komendy"))

# @client.event
# async def on_message(message):
#     if "sex" in message.content:
#         await message.delete()
#     await client.process_commands(message)

@client.command(aliases=['zbior']) #inside joke command
async def zbiór(ctx):
    print(ctx)
    zbiory = ['zbior', 'zbiot', 'zboir', 'zboit','zboier','zboitr']
    await ctx.send(random.choice(zbiory))
    await ctx.send(file=discord.File('/opt/zbiorbot/zbior.png'))

@client.command()
async def ping(ctx): #ping command
    await ctx.send('<@790211729443127307>')

@client.command(aliases = ['8kula']) #command you can ask for something
async def _8kula(ctx, question):
    odpowiedzi = ['Zapytaj Kubę on zawsze będzie wiedział',
                  'Nie wiem stary nie pytaj mnie',
                  'Powiedz skąd miałbym mieć na to odpowiedź',
                  f'{random.randint(1, 99)}',
                  'Mi się wydaję, że aczkolwiek aktualnie nie',
                  'Domyśl się',
                  'Oczywista oczywistość',
                  'W tym sęk',
                  'Trochę',
                  'Nie mam czasu spytaj jutro']

    await ctx.send(f'Pytanie: {question}\nOdpowiedź: {random.choice(odpowiedzi)}')


@client.command() #shows commands
async def komendy(ctx):

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = discord.Color.from_rgb(r, g, b)
    embed=discord.Embed(title="Komendzisze ", description="komendy jakie możesz użyć w zbiorze", color=color)
    embed.add_field(name="!8kula", value="robi 8kula wszyscy wiemy o co chodzi", inline=False)
    embed.add_field(name="!zbiór", value="bezuzyteczna komenda smierdzicie", inline=False)
    embed.add_field(name="!anime", value="wysyla dziewczynke anime (robie cos potrzebna komenda)", inline=False)
    embed.add_field(name="!dylemat", value="jakbys miał dylemat to zbiórbot pomoże ci wybrać czy coś", inline=False)
    embed.add_field(name="!husbando", value="wyświetla...", inline=False)
    embed.add_field(name="!ip", value="wyświetla ip serwera minecraft", inline=False)
    embed.add_field(name="!jd", value="jest dobrze :)))", inline=False)
    embed.add_field(name="!oof", value="oof", inline=False)
    embed.add_field(name="!ping", value="pingje mnie xddddd", inline=False)
    embed.set_footer(text=f"r {r}, g {g}, b {b}")
    await ctx.send(embed=embed)

@client.command() #you can make bot say something
async def say(ctx, *, message):
    if not_brawl_stars_check(message):
        await ctx.message.delete()
        await ctx.send(message)
    else:
        await ctx.message.delete()
        await ctx.send("Tak to prawda jebie brawl stars B)")

@client.command() #inside joke command
async def anime(ctx):
    await ctx.send('https://media.discordapp.net/attachments/722581350116360332/774297918701830154/image0.gif')
    await ctx.send(file=discord.File('/opt/zbiorbot/cutesmoooth.mp4'))
    await test.testmodule(ctx)

@client.command(aliases=['JD']) #inside joke
async def jd(ctx):
    await ctx.send(file=discord.File('/opt/zbiorbot/jd.png'))

@client.command() #command you can ask for something
async def dylemat(ctx, *, message):
  #no_yes[0] == no answers, no_yes[1] == yes answers

  no_yes = [["nie mogę się z tym zgodzić niestety", "nieprawdanie", "nie.", "nieeeeeeeeeeeeeee", "a wiesz, że nie?"], ["oczywistość", "jeszcze jak", "aczkolwiek tak", "mhm", "tak to prawda zgadzam się z tym w 100% prawda tak"]]
  if not_brawl_stars_check(message): #zbiorbot hate brawlstars
    no_or_yes_list = random.choice(no_yes) #choosing random list
    await ctx.send(random.choice(no_or_yes_list)) #choosing random thing from that list

  else:
    await ctx.send(random.choice(no_yes[0]))

@client.command() #shows ip for minecraft server
async def ip(ctx):
  await ctx.send('Nasze ip do zbiór SMP to: ```188.34.196.6```')

@client.command() #command made for my friend it displays legoshis photos (gave me nightmares)
async def husbando(ctx):
  liczba = random.randint(1, 11)
  if liczba < 11:
      photo=f"/opt/zbiorbot/legoshiphotots/tadek{liczba}.jpg"
      await ctx.send(file=discord.File(photo))
  else:
      await ctx.send('https://c.tenor.com/9wJRnApQsmYAAAAM/legoshi.gif')


@client.command(aliases=['tymek']) #made for my friend
async def oof(ctx):
    await ctx.send('https://tenor.com/view/roblox-fortnite-dance-default-memes-cool-gif-12661768')


client.run(TOKEN) #making bot run with command
