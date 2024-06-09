import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import subprocess

load_dotenv()

config = {
    "app_id": os.getenv("app_id"),
    "public_key": os.getenv("public_key"),
    "private_key": os.getenv("private_key"),
    "token": os.getenv("token")
}

intents = discord.Intents.default()
intents.message_content = True
server_process = None

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    await bot.change_presence(activity=discord.Game(name="Server Offline"))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def start(ctx):
    global server_process
    await ctx.send("Starting the server..")
    
    try:
        server_process = subprocess.Popen([r"C:\Users\hashi\Downloads\Server\start.bat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        await bot.change_presence(activity=discord.Game(name="Server Online"))
        await ctx.send("Server started successfully!")
    except Exception as e:
        await ctx.send(f"Failed to start the server. Error: {e}")
        await bot.change_presence(activity=discord.Game(name="Server Offline"))

@bot.command()
async def stop(ctx):
    global server_process
    if server_process is not None:
        await ctx.send("Stopping the server..")
        try:
            server_process.stdin.write('stop\r')
            server_process.stdin.flush()
            server_process.wait(timeout=60)
            server_process = None
            await ctx.send("Server stopped successfully!")
        except Exception as e:
            await ctx.send(f"Failed to stop server. Error: {e}")
    else:
        await ctx.send("Server is not running.")

bot.run(config["token"])
