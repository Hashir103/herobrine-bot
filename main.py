import os
import discord
from dotenv import load_dotenv

load_dotenv()

config = {
    "app_id": os.getenv("app_id"),
    "public_key": os.getenv("public_key"),
    "private_key": os.getenv("private_key"),
    "token": os.getenv("token")
}

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

client.run(config["token"])