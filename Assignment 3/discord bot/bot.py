# This Python program is a Discord bot designed to manage and track member activities in a Discord server. It uses the discord.py library to interact with the Discord API.
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import nest_asyncio
import csv

# Load environment variables from a .env file if present
load_dotenv()

# token and guild from the discord developer portal
TOKEN = "MTEzOTU4Njg1Nzc5ODIyMTk5NA.GQAx5f.b_sSGsjJJ_UwQgERAD25-A-Wt-YQ7fu_E1wkto"
GUILD = "sukhpreet.saini2020's server"

# File name to store member information
fname = "memberList.csv"

# nest_asyncio to allow running async event loop in sync environment
nest_asyncio.apply()

# bot intents to capture specific events
intents = discord.Intents.all()

# bot instance with specified command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# This is to executed when the bot is ready to start
@bot.event
async def on_ready():
    print(f"{bot.user} is ready.")
    guild = discord.utils.get(bot.guilds, name=GUILD)
    if guild is None:
        print(f"Bot is not a member of the server '{GUILD}'.")
        return

    print(f"{bot.user} is scraping the following server:")
    print(f"{guild.name} (id: {guild.id})")
    await update_member_list(guild)

# This function is executed when a new member joins the server
@bot.event
async def on_member_join(member):
    join_date = member.joined_at.strftime('%Y-%m-%d %H:%M:%S')
    with open(fname, mode="a", encoding="utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([f"{member.name}#{member.discriminator}", str(join_date), "Active"])

# This function is executed when a member leaves the server
@bot.event
async def on_member_remove(member):
    data = []
    with open(fname, mode='r', encoding='utf8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    data = [row for row in data if row[0] != f"{member.name}#{member.discriminator}"]

    for row in data:
        if row[0] == f"{member.name}#{member.discriminator}":
            row[2] = "Removed"
            break

    with open(fname, mode='w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# Update the member list in the CSV file
async def update_member_list(guild):
    with open(fname, mode="w", encoding="utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Username', 'Join Date', 'Status'])

        for member in guild.members:
            join_date = member.joined_at.strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([f"{member.name}#{member.discriminator}", str(join_date), "Active"])

# Kick a member from the server
@bot.command()
async def kick_member(ctx, member: discord.Member):
    try:
        await member.kick(reason="Kicked by the bot")
        print(f"Kicked {member.name}#{member.discriminator} from the server.")
    except discord.Forbidden:
        print(f"Bot does not have permissions to kick {member.name}#{member.discriminator}.")

# Run the bot with the specified token
bot.run(TOKEN)


# [Running] python -u "c:\Users\PC\Desktop\work\college work\Sem 2\python- 1112 (5 - 7.50pm)\weeks\week 13\project\bot.py"
# [2023-08-11 14:46:11] [INFO    ] discord.client: logging in using static token
# [2023-08-11 14:46:12] [INFO    ] discord.gateway: Shard ID None has connected to Gateway (Session ID: 103cb7075702444ca8ae99a388056636).
# bot1139586857798221994#1483 is ready.
# bot1139586857798221994#1483 is scraping the following server:
# sukhpreet.saini2020's server (id: 1139608384648253470)


# [Running] python -u "c:\Users\PC\Desktop\work\college work\Sem 2\python- 1112 (5 - 7.50pm)\weeks\week 13\project\bot.py"
# [2023-08-11 15:29:10] [INFO    ] discord.client: logging in using static token
# [2023-08-11 15:29:11] [INFO    ] discord.gateway: Shard ID None has connected to Gateway (Session ID: 665de17ba9475e74d4da43a91bab6bea).
# bot1139586857798221994#1483 is ready.
# bot1139586857798221994#1483 is scraping the following server:
# sukhpreet.saini2020's server (id: 1139608384648253470)

# [Done] exited with code=1 in 887.464 seconds

# [Running] python -u "c:\Users\PC\Desktop\work\college work\Sem 2\python- 1112 (5 - 7.50pm)\weeks\week 13\project\bot.py"
# [2023-08-11 15:47:26] [INFO    ] discord.client: logging in using static token
# [2023-08-11 15:47:26] [INFO    ] discord.gateway: Shard ID None has connected to Gateway (Session ID: aeaecf7c21da945765868c71ba9583be).
# bot1139586857798221994#1483 is ready.
# bot1139586857798221994#1483 is scraping the following server:
# sukhpreet.saini2020's server (id: 1139608384648253470)
# Kicked shivam_38209_13435#0 from the server.

# [Done] exited with code=1 in 152.914 seconds

# [Running] python -u "c:\Users\PC\Desktop\work\college work\Sem 2\python- 1112 (5 - 7.50pm)\weeks\week 13\project\bot.py"
# [2023-08-11 15:50:01] [INFO    ] discord.client: logging in using static token
# [2023-08-11 15:50:02] [INFO    ] discord.gateway: Shard ID None has connected to Gateway (Session ID: 43e330e145bacd5fd87c1ca7e443da51).
# bot1139586857798221994#1483 is ready.
# bot1139586857798221994#1483 is scraping the following server:
# sukhpreet.saini2020's server (id: 1139608384648253470)