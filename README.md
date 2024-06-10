# Herobrine Bot
Run a Minecraft Server through Discord!
Created by Hashir (with the help of Jackie).

## Recommendations
Based on the operating system, there is varying level of speed and ability. I recommend using MacOS/Linux for the best performance. However, it is set up to support any environment.

## Requirements
Make sure you have the packages listed in `requirements.txt`. Additionally, for Windows, make sure you have Docker Desktop and it is running.

## Environmental Variables
Create a file named `.env`. This file should include two lines: one for your discord token and one for your server jar file name.

Sample .env file:
```
token=LSXkc33cKe3
mc_jar=spigot.jar
```

## Server Location
Please put all your server files and your server.jar in the `./server` directory. This works without any edits if your server is on Port 25565. If there are more ports/other ports must be modified, you must update `docker-compose.yml` and `dockerfile` to account for them.

**NOTE: it is best to import your server once it is already functioning. i.e. don't accept the EULA here, do it before.**

## Running on Unix Based Systems
Run `main.py`.

## Running on Windows Based Systems
**RUNNING main.py directly in Windows will break any command related to the console, including stop.** 
To circumvent this, We will use Docker to create a WSL environment that will let us run the project to its full extent. Run `start.bat` to set up the Docker Environment. Note that if you make any changes to the bot files, it will need time to regenerate the whole Docker volume. Make sure to delete old images. 

## Bot Commands
`!ping` - Check's bot's responsiveness
`!start` - Starts the minecraft server.
`!stop` - Stops a running minecraft server.
`!status` - Checks whether a minecraft server is running or not.
`!console args` - Admin only command: Let's you type in the console (used for operating players, for example)
  -> example: `!console say hi` or `!op hash1r`
