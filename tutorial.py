import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from discord import Game
import dice
import matcher
import rollManager
import secrets

Client = discord.client
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Testing123"))
    print("Ready")


@client.event
async def on_message(message):
    if message.content.upper() == "!PING":
        userID = message.author.id
        await client.send_message(message.channel, f"<@{userID}> pong!", tts=True)

    if message.content.upper().startswith('HELLO'):
        await client.send_message(message.channel, "Hi there!")

    if matcher.isSimpleRoll(message.content):
        dieCount = matcher.getFirstNum(message.content)
        userID = message.author.id
        result = rollManager.standardRoll(dieCount, dieCount)
        await client.send_message(message.channel, f"You rolled: {dice.formatDice(result.dice)} \nHits: {result.hits}")


client.run(secrets.discClient)
