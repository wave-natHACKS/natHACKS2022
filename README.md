#### natHACKS2022 - Wave Bot

## Objective: Train a ML model which senses the emotional feeling of user based on the pulse of their brainwave. The ML model is deployed as a discord bot.


## ~250 word summary:
In the back-end, we trained a convolutional neural network model that takes in a short brain signal image to predict whether the person is saying something sad, happy, disgusted, angry, fear, or neutral. For our training data, we extracted the EEG wave data from the open source database, Zuco 2.0. This database recorded  patients’ brain signals while they were reading English phrases. We used this word to EEG mapping and divided them into the 6 emotion classes above using word2vec word embedder. Ultimately, we plotted the EEG signal and fed the plot image to convolutional neural network (CNN) to train our model. 

In the front-end, we created a discord bot to interact with the users via various commands.
Wave is a complex bot with easy-to-use commands like !start and !about, which describes the purpose of the bot. The discord bot is deployed using a free cloud platform called, "Heroku," to stay online without having to run the script on a local computer. It can also restrict different users and channels to communicate.
Once a user sends a ".npy" file containing the brain wave data, Wave will run the data pre-processing and modelling to predict the emotion. 

As a discord bot, it is very user-friendly and quickly can be deployed anywhere on your desktop, laptop, or even mobile devices. 
It also has an indefinite possibility and opportunities to grow and improve upon.


### More detailed explanation of Data Preparation and Model Creation


## Data Preparation
> 1. We Chose Zuco 2..0 dataset.
> 2. Extracted alpha, beta, gamma and theta waves and plot them as a normal plot for each type of wave
> 2.1 zuco 2.0 dataset provided a matlab files with all the brain wave data. For each english word, it had corresponding alpha, beta, gamma, and theta information
 we extracted that and put them in a dictionary to use this map for furthur processing
> 3. Stack each plot into a single image (stack them like in RGB channel). 
> 4. Save stacked image in .npy format. This is to retain each channel’s information and preventing it to be converted into simple RGB image
> 5. use word2vec word embedder to help classify which the word. We used the cosine similarity algorithm of word2vec to greedily chose the most similar label for this word
> 6. Store path to image, word and classification (happiness, sadness, etc) in single csv file

## Model Creation
> 1. Prepare dataset (image and label pair). Normalize the image to prevent model paramters to become gigantic.
> 2. Create model. There are multiple ways to build models in tensorflow (and that’s why I am not a big fan of tensorflow), but we will stick to the method which uses Sequential class. Refer to tutorial for this.
> 3. Compile model and fit. There are bunch of options to compile, like optimizer or loss. Nowadays people usually use Adam with a learning rate of 1e-4 ~ 1e-5 for optimizer since it is known to wrok well. For loss function, choose CrossEntropy or its variant. This is due to the format of data in multiclass supervised learning. 
> 4. After the successful run, you might want to save it immediately. Some process takes 10 hours or beyond, so make sure to save. 
> 5. After saving the model, you can test your trained model on some test dataset and check the accuracy or other evaluation metrics to evaluate the performance.

## github branches
> in modules branch, there is code that did data processing and the training of model
