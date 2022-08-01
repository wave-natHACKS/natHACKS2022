### natHACKS2022

## Objective: Train a ML model which senses the emotional feeling of user based on the pulse of their brainwave. The ML model is deployed as a discord bot.


## ~250 word summary:
In the back-end, we trained a convolutional neural network model that takes in a short brain signal image to predict whether the person is feeling sad, happy, disgusted, angry, fear, or neutral. For our training data, we extracted the EEG wave data from the open source database, Zuco 2.0. This database recorded  patients’ brain signals while they were reading English phrases. We used this word to EEG mapping and divided them into the 6 emotion classes above using word2vec word embedder. Ultimately, we plotted the EEG signal and fed the plot image to convolutional neural network (CNN) to train our model. 

In the front-end, we created a discord bot to interact with the users via various commands.
Wave is a complex bot with easy-to-use commands like !start and !about, which describes the purpose of the bot. The discord bot is deployed using a free cloud platform called, "Heroku," to stay online without having to run the script on a local computer. It can also restrict different users and channels to communicate.
Once a user sends a ".npy" file containing the brain wave data, Wave will run the data pre-processing and modelling to predict the emotion. 

As a discord bot, it is very user-friendly and quickly can be deployed anywhere on your desktop, laptop, or even mobile devices. 
It also has an indefinite possibility and opportunities to grow and improve upon.
