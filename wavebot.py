import discord
import os
import time
import requests
import json
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers


client = discord.Client()

def get_cnn_classifier(
    in_height: int,
    in_width: int,
    in_channels: int,
    out_shape: int
) -> Sequential:
    """Construct a simple CNN model for the project.
    Reference: https://www.tensorflow.org/tutorials/images/classification
    """
    model = Sequential([
        layers.Rescaling(1./255, input_shape=(in_height, in_width, in_channels)),
        layers.Conv2D(16, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(out_shape, activation="softmax")
    ])

    return model

def load_model(path: str) -> Sequential:
    """Load trained model with saved weights."""
    model = get_cnn_classifier(300, 450, 4, 6)
    model.load_weights(path)
    return model


def predict(img: np.ndarray, model: Sequential) -> int:
    """Predict the emotion with trained model."""
    assert img.shape == (300, 450, 4), "The shape of image is not suitable. It must be (300, 450, 4)"
    
    # expand dimension to suite the model
    img = np.expand_dims(img, axis=0)

    # classes
    pred = model.predict(img)
    return np.argmax(pred)

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

#Displays that the bot is on
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
#Restricted to the specific channel where only specific users can communicate with the bot
@client.event
async def on_message(message):

    id = client.get_guild(991909090517340170) 
    channels = ["testing-bot"]

    # First checking if the user has sent a .npy file and save it, if yes.
    if message.attachments == "[]":
        return
    else:
        print(message.attachments)
        if message.attachments != []:
            filename = message.attachments[0].filename
            check = filename[-4:]

            if check == ".npy":
                await message.attachments[0].save(filename)
                print("Saving .npy file succeeded")

                file = np.load(filename)
                print(file.shape)

                embedded = discord.Embed(title="Saving .npy File", description=filename)
                await message.channel.send(content=None,embed=embedded)

                time.sleep(0.5)
        
                time.sleep(1)
                embedded = discord.Embed(title="Status Update:", description=filename + "saved successfully.")
                await message.channel.send(content=None,embed=embedded)
                
                time.sleep(1.5)
                embedded = discord.Embed(title="Beginning Data Pre-processing and Modelling", description= "")
                await message.channel.send(content=None,embed=embedded)

                model = load_model("C:\natHACKS2022\data.h5")
                index = predict(file, model)

                embedded = discord.Embed(title="Detecting Emotions...")
                await message.channel.send(content=None,embed=embedded)
                time.sleep(2)

                if index == 0:

                    embedded_anger = discord.Embed(title="Experiment Result")
                    embedded_anger.add_field(name="Emotion detected is:",value="ANGER")
                    await message.channel.send(content=None,embed=embedded_anger)

                    emoji_anger = '\U0001F621'
                    await message.add_reaction(emoji_anger)

                    await message.channel.send('Hey' + message.author.mention + '...')
                    time.sleep(0.5)
                    await message.channel.send('No one heals themselves')
                    time.sleep(1.5)
                    await message.channel.send('by wounding another.')

                elif index == 1:

                    embedded_disgust = discord.Embed(title="Experiment Result")
                    embedded_disgust.add_field(name="Emotion detected is:",value="DISGUST")
                    await message.channel.send(content=None,embed=embedded_disgust)

                    emoji_disgust = '\U0001F922'
                    await message.add_reaction(emoji_disgust)

                    await message.channel.send("What are you disgusted about?" + message.author.mention)
                    time.sleep(1)
                    quick_message = await message.channel.send("Did you look at yourself in the mirror again?")
                    time.sleep(1.75)
                    await quick_message.delete()  

                elif index == 2:

                    embedded_fear = discord.Embed(title="Experiment Result")
                    embedded_fear.add_field(name="Emotion detected is:",value="FEAR")
                    await message.channel.send(content=None,embed=embedded_fear)


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

                elif index == 3:

                    embedded_happy = discord.Embed(title="Experiment Result")
                    embedded_happy.add_field(name="Emotion detected is:",value="HAPPINESS")
                    await message.channel.send(content=None,embed=embedded_happy)

                    emoji_happy = '\U0001F604'	
                    await message.add_reaction(emoji_happy)

                    link = emotion_happiness()
                    await message.channel.send(link)

                elif index == 4:

                    embedded_neutral = discord.Embed(title="Experiment Result")
                    embedded_neutral.add_field(name="Emotion detected is:",value="NEUTRAL")
                    await message.channel.send(content=None,embed=embedded_neutral)

                    emoji_neutral = '\U0001F610'
                    await message.add_reaction(emoji_neutral)

                    await message.channel.send("You could use a smile I bet.")
                    time.sleep(2) 
                    await message.channel.send("The opposite of artificial intelligence is..")
                    time.sleep(1)
                    await message.channel.send("Real Stupid.")
                    time.sleep(1)
                    await message.channel.send("Hahaha!!! ")

                elif index == 5:
                    
                    embedded_sad = discord.Embed(title="Experiment Result")
                    embedded_sad.add_field(name="Emotion detected is:",value="SADNESS")
                    await message.channel.send(content=None,embed=embedded_sad)

                    emoji_sad = '\U0001F614'	
                    await message.add_reaction(emoji_sad)

                    quote = emotion_sadness()
                    await message.channel.send(quote + "\n")   

    """
    Data pre-processing and modelling

    """  
    
    # !help will contain every single bot command  
    if message.content == "!help":
        embedded = discord.Embed(title="BOT Help", description="Helpful Commands...")
        embedded.add_field(name="!about", value="Detailed description of the bot")
        embedded.add_field(name="!start", value="Greets the user")
        embedded.add_field(name="!sad", value="Displays the sad emotion")
        embedded.add_field(name="!happy", value="Displays the happy emotion")
        embedded.add_field(name="!anger", value="Displays the angry emotion")
        embedded.add_field(name="!neutral", value="Displays the neutral emotion")
        embedded.add_field(name="!disgust", value="Displays the disgust emotion")
        embedded.add_field(name="!fear", value="Displays the fear emotion")
        embedded.add_field(name="!bored",value="If you are bored, enter the command to find out...")
        await message.channel.send(content=None,embed=embedded)
    

    # !about command
    if message.content == "!about":
        await message.channel.send("We as humans, we have multiple ways to express our emotions.")  
        time.sleep(2)
        await message.channel.send("Facial expression, body language, and so on.")
        time.sleep(2)
        await message.channel.send("While these effectively express our emotional feelings, none of them will outperform the brainwave to express one’s emotions.")
        time.sleep(2)
        await message.channel.send("I reveal the human’s emotional feeling based on the pulse of brainwave, using the machine learning model.")


    # !bored command
    if message.content == "!bored":
        await message.channel.send("How does a brain say 'Hello?'")
        time.sleep(1)
        await message.channel.send("Brain wave!")
        time.sleep(1)
        await message.channel.send("This is where I got my name from.. " + "\U0001F601")


    # the following commands are restricted to the specific channels
    if str(message.channel) in channels:

        # !start command
        if message.content.find("!start") != -1:
            await message.channel.send("Hello there " + message.author.mention + "!")
            time.sleep(0.5)
            await message.channel.send("I am Wave and you can predict anyone's emotions based on their brain waves!")
            time.sleep(2.5)
            await message.channel.send("To start,")
            time.sleep(0.5)
            await message.channel.send("Send a .npy file containing data on brain waves.")
            time.sleep(1.5)
            await message.channel.send("Go make yourself coffee or cup of tea..")
            time.sleep(1.25)
            await message.channel.send("In a minute or so, the brain waves will be translated to an emotion!")
            await message.channel.send("\U0001F60E")


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
            time.sleep(1.75)
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
            

#Run the bot
client.run(os.environ["DISCORD_TOKEN"])