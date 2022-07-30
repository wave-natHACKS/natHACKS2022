import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

client.run("MTAwMjk5MjE0OTk1NDA1MjI3Nw.GAN41b.1KPW1OLGe2NgOXMJHpnQ9g9xRqWWeo4-jXQy5o")