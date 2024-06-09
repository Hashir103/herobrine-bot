import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import subprocess

load_dotenv()

config = {
    "token": os.getenv("token"),
    "start_server": f"java -Xms4G -Xmx4G -XX:+UseG1GC -jar spigot.jar nogui"
}

intents = discord.Intents.default()
intents.message_content = True
serv_proc = None

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

    # Send message to channel
    channel = bot.get_channel(1166414794639822918)
    await channel.send("Awake!")

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
            serv_proc = subprocess.Popen(config["start_server"], shell=True, stdin=subprocess.PIPE)
        
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
        serv_proc.stdin.write(b"/stop\n")
        serv_proc.stdin.flush()
        serv_proc.stdin.close()
        serv_proc.wait()
        serv_proc = None
        await ctx.send("Server stopped!")
    else:
        await ctx.send("Server is not running!")

bot.run(config["token"])
