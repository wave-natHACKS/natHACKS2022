import discord
import os
import time
import asyncio
import requests
import json

# Keep track of new users and messages
new_users = 0
new_messages = 0

'''
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

#Secret Token to activate the bot
DISCORD_TOKEN = read_token()
'''

client = discord.Client()


#When the brain wave is categorized as sadness, it will display an encouraging message
def emotion_sadness():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote
    
#When the brain wave is categorized as happiness, it will display a happy image
def emotion_happiness():
    file = r"https://random.dog/woof.json"
    page = requests.get(file)
    json_data = json.loads(page.text)
    link = json_data["url"]
    return link



async def update_usersandmessages():
    await client.wait_until_ready()
    global new_users, new_messages

    while not client.is_closed():
        try:
            with open("users_messages.txt", "a") as f:
                f.write(f"Time: {time.asctime(time.localtime(time.time()))}, Messages: {new_messages}, Members Joined: {new_users}\n")

            await asyncio.sleep(5)
        
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


#Displays that the bot is on
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#Upon joining the server, welcome the user
@client.event
async def on_member_join(member):
    global new_users
    new_users += 1 # increment counter

    for channel in member.guild.channels:
        if str(channel) == "welcome":
            await channel.send_message(f"""Welcome to the server! {member.mention}""")

    
#Restricted to the specific channel where only specific users can communicate with the bot
@client.event
async def on_message(message):
    global new_messages
    new_messages += 1 # increment counter

    id = client.get_guild(991909090517340170)
    bad_words = ["shit", "fuck", "bitch", "shut up"]
    channels = ["testing-bot"]

    for word in bad_words:
        if message.content.count(word) > 0:
            await message.channel.send("A bad word was said.")
            
            
            
    if message.content == "!help":
        embedded = discord.Embed(title="BOT Help", description="Helpful Commands...")
        embedded.add_field(name="!about", value="Description of me!")
        embedded.add_field(name="!hello", value="Greets the user")
        embedded.add_field(name="!users", value="Displays the number of users")
        embedded.add_field(name="!sad", value="Displays the sad emotion")
        embedded.add_field(name="!happy", value="Displays the happy emotion")
        embedded.add_field(name="!anger", value="Displays the angry emotion")
        embedded.add_field(name="!neutral", value="Displays the neutral emotion")
        embedded.add_field(name="!disgust", value="Displays the disgust emotion")
        embedded.add_field(name="!fear", value="Displays the fear emotion")
        embedded.add_field(name="!bored",value="Enter it to find out...")
        
        await message.channel.send(content=None,embed=embedded)
    
    if message.content == "!about":
        await message.channel.send("We as humans, we have multiple ways to express our emotions.")  
        time.sleep(1)
        await message.channel.send("Facial expression, body language, and so on.")
        time.sleep(1)
        await message.channel.send("While these effectively express our emotional feelings, none of them will outperform the brainwave to express one’s emotions.")
        time.sleep(1)
        await message.channel.send("I reveal the human’s emotional feeling based on the pulse of brainwave, using the machine learning model.")

    if message.content == "!bored":
        await message.channel.send("How does a brain say 'Hello?'")
        time.sleep(1)
        await message.channel.send("Brain wave!")
        time.sleep(1)
        await message.channel.send("This is where I got my name from.. " + "\U0001F601")

    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hello there!")
   
        if message.content == "!users":
            await message.channel.send(f"""We currently have {id.member_count} members!""")

        if message.content.find("!dispusrs&msgs") != -1:
            await message.channel.send(f"Time: {time.asctime(time.localtime(time.time()))}, Messages: {new_messages}, Members Joined: {new_users}")
        
        if message.content.find("!sad") != -1:
            
            embedded_sad1 = discord.Embed(title="Detecting Emotions...")
            await message.channel.send(content=None,embed=embedded_sad1)
            time.sleep(2)

            embedded_sad2 = discord.Embed(title="Experiment Result")
            embedded_sad2.add_field(name="Emotion detected is:",value="SADNESS")
            await message.channel.send(content=None,embed=embedded_sad2)

            emoji_sad = '\U0001F614'	
            await message.add_reaction(emoji_sad)

            quote = emotion_sadness()
            await message.channel.send(quote + "\n")            
        
        if message.content.find("!happy") != -1:

            embedded_happy1 = discord.Embed(title="Detecting Emotions...")
            await message.channel.send(content=None,embed=embedded_happy1)
            time.sleep(2)

            embedded_happy2 = discord.Embed(title="Experiment Result")
            embedded_happy2.add_field(name="Emotion detected is:",value="HAPPINESS")
            await message.channel.send(content=None,embed=embedded_happy2)

            emoji_happy = '\U0001F604'	
            await message.add_reaction(emoji_happy)

            link = emotion_happiness()
            await message.channel.send(link)
        
        if message.content.find("!fear") != -1:

            embedded_fear1 = discord.Embed(title="Detecting Emotions...")
            await message.channel.send(content=None,embed=embedded_fear1)
            time.sleep(2)

            embedded_fear2 = discord.Embed(title="Experiment Result")
            embedded_fear2.add_field(name="Emotion detected is:",value="FEAR")
            await message.channel.send(content=None,embed=embedded_fear2)


            emoji_fear = '\U0001F628'
            await message.add_reaction(emoji_fear) 

            #Send the messages with fear
            await message.channel.send("You...")
            time.sleep(1)
            await message.channel.send("are")
            time.sleep(0.2)
            await message.channel.send(".")
            time.sleep(0.2)
            await message.channel.send(".")
            time.sleep(0.2)
            await message.channel.send(".\n")
            time.sleep(0.3)
            await message.channel.send("scared.....")
            time.sleep(3)
            await message.channel.send("BOO!")
        

        if message.content.find("!anger") != -1:

            embedded_anger1 = discord.Embed(title="Detecting Emotions...")
            await message.channel.send(content=None,embed=embedded_anger1)
            time.sleep(2)

            embedded_anger2 = discord.Embed(title="Experiment Result")
            embedded_anger2.add_field(name="Emotion detected is:",value="ANGER")
            await message.channel.send(content=None,embed=embedded_anger2)

            emoji_anger = '\U0001F621'
            await message.add_reaction(emoji_anger)

            await message.channel.send('Hey' + message.author.mention + '...')
            time.sleep(0.5)
            await message.channel.send('No one heals themselves')
            time.sleep(1.5)
            await message.channel.send('by wounding another.')
            
        if message.content.find("!disgust") != -1:

            embedded_disgust1 = discord.Embed(title="Detecting Emotions...")
            await message.channel.send(content=None,embed=embedded_disgust1)
            time.sleep(2)

            embedded_disgust2 = discord.Embed(title="Experiment Result")
            embedded_disgust2.add_field(name="Emotion detected is:",value="DISGUST")
            await message.channel.send(content=None,embed=embedded_disgust2)

            emoji_disgust = '\U0001F922'
            await message.add_reaction(emoji_disgust)

            await message.channel.send("What are you disgusted about?" + message.author.mention)
            time.sleep(1)
            quick_message = await message.channel.send("Did you look at yourself in the mirror again?")
            time.sleep(1.25)
            await quick_message.delete()

        if message.content.find("!neutral") != -1:

            embedded_neutral1 = discord.Embed(title="Detecting Emotions...")
            await message.channel.send(content=None,embed=embedded_neutral1)
            time.sleep(2)

            embedded_neutral2 = discord.Embed(title="Experiment Result")
            embedded_neutral2.add_field(name="Emotion detected is:",value="NEUTRAL")
            await message.channel.send(content=None,embed=embedded_neutral2)

            emoji_neutral = '\U0001F610'
            await message.add_reaction(emoji_neutral)

            await message.channel.send("You could use a smile I bet.")
            time.sleep(2) 
            await message.channel.send("The opposite of artificial intelligence is..")
            time.sleep(1)
            await message.channel.send("Real Stupid.")
            time.sleep(1)
            await message.channel.send("Hahaha!!! ")
            
            

################################
#.npy file is received
################################

#Run update_usersandmessages constantly
client.loop.create_task(update_usersandmessages())

#Run the bot
client.run(os.environ["DISCORD_TOKEN"])