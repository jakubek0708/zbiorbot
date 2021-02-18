import discord
from discord.ext import *
from discord.ext import commands
from discord import Color
import random
import time
import ffmpeg


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("zbior gotowy")


@client.command(aliases=['zbior'])
async def zbiór(ctx):
    print(ctx)
    zbiory = ['zbior', 'zbiot', 'zboir', 'zboit','zboier','zboitr']
    await ctx.send(random.choice(zbiory))
    await ctx.send(file=discord.File('zbior.png'))


@client.command(aliases = ['8kula'])
async def _8kula(ctx, *, question):
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


@client.command()
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
    embed.add_field(name="!senpai", value="wyświetla...", inline=False)
    embed.add_field(name="!CBT", value="( ͡~ ͜ʖ ͡°)", inline=False)
    embed.set_footer(text=f"r {r}, g {g}, b {b}")
    await ctx.send(embed=embed)

@client.command()
async def anime(ctx):
    await ctx.send('https://media.discordapp.net/attachments/722581350116360332/774297918701830154/image0.gif')
    await ctx.send(file=discord.File('cutesmoooth.mp4'))


@client.command()
async def dylemat(ctx):
  await ctx.send(random.choice(["oczywistość", "a wiesz, że nie?", "jeszcze jak", "aczkolwiek tak", "nie.", "nieeeeeeeeeeeeeee"]))




@client.command()
async def senpai(ctx):
  liczba = random.randint(1, 10)
  str=f"tadek{liczba}.jpg"
  await ctx.send(file=discord.File(str))



@client.command()
async def beemovie(ctx):
  with open('jazz.txt') as plik:
    for linia in plik:
      await ctx.send(linia.strip().split())


@client.command(aliases=['CBT'])
async def cbt(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    channel = ctx.author.voice.channel
    await channel.connect()
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('cbt.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    while voice_client.is_playing():
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(4) #
        while voice_client.is_playing():
            break
        else:
            await voice_client.disconnect()



@client.command()
async def top10najlepszerzeczypolska2021numer1(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/763447893913763840/806786062453964870/avatar-damedane.mp4')




client.run('NzkwMjExNzI5NDQzMTI3MzA3.X99UBQ.0y2IXIMv60B9ozAGcRw6ER-1CFA')
