import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
from asyncio import subprocess

load_dotenv()

config = {
    "token": os.getenv("token"),
    "start_server": f"cd server && java -Xms4G -Xmx4G -XX:+UseG1GC -jar {os.getenv('mc_jar')} nogui",
}

intents = discord.Intents.default()
intents.message_content = True
serv_proc = None

bot = commands.Bot(command_prefix="!", intents=intents)

async def send_input(text):
    global serv_proc

    serv_proc.stdin.write(f'{text}\n'.encode())
    await serv_proc.stdin.drain()

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def status(ctx):
    await ctx.send("Server is running!") if serv_proc is not None else await ctx.send("Server is not running, or server has been started manually!")

@bot.command()
async def start(ctx):
    global serv_proc

    if serv_proc is None:
        await ctx.send("Minecraft server starting up...")
        try:
            serv_proc = await subprocess.create_subprocess_shell(config["start_server"], shell=True, stdin=subprocess.PIPE)
        
        except Exception as e:
            print(e)
            await ctx.send("Failed to start Minecraft server! Error: " + str(e))
            serv_proc = None

    else:
        await ctx.send("Server is already running!")

@bot.command()
async def stop(ctx):
    global serv_proc
    if serv_proc is not None:
        await ctx.send("Stopping Minecraft server...")
        await send_input("stop")
        await serv_proc.wait()
        
        serv_proc = None
        
        await ctx.send("Server stopped!")
    else:
        await ctx.send("Server is not running!")

@bot.command()
@has_permissions(administrator=True)
async def console(ctx, *, text):
    global serv_proc
    if serv_proc is not None:
        if text == "stop":
            await ctx.send("Please use the !stop command to stop the server!")
            return
        await send_input(text)
        await ctx.send("Command sent!")
    else:
        await ctx.send("Server is not running!")

bot.run(config["token"])
