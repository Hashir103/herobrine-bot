import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import subprocess
import threading

load_dotenv()

config = {
    "token": os.getenv("token"),
    "path": os.getenv("server_path"),
}

intents = discord.Intents.default()
intents.message_content = True
server_process = None
output_thread = None

bot = commands.Bot(command_prefix="!", intents=intents)

def read_output(process):
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    await bot.change_presence(activity=discord.Game(name="!bothelp"))

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def start(ctx):
    global server_process
    global output_thread

    server_process = subprocess.Popen([config["path"]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output_thread = threading.Thread(target=read_output, args=(server_process,))
    output_thread.start()
    await ctx.send("Minecraft server started.")

bot.run(config["token"])
