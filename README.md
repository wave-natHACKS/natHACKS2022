#### natHACKS2022 - Wave Bot

## Objective: Train a ML model which senses the emotional feeling of user based on the pulse of their brainwave. The ML model is deployed as a discord bot.


## ~250 word summary:
In the back-end, we trained a convolutional neural network model that takes in a short brain signal image to predict whether the person is feeling sad, happy, disgusted, angry, fear, or neutral. For our training data, we extracted the EEG wave data from the open source database, Zuco 2.0. This database recorded  patients’ brain signals while they were reading English phrases. We used this word to EEG mapping and divided them into the 6 emotion classes above using word2vec word embedder. Ultimately, we plotted the EEG signal and fed the plot image to convolutional neural network (CNN) to train our model. 

In the front-end, we created a discord bot to interact with the users via various commands.
Wave is a complex bot with easy-to-use commands like !start and !about, which describes the purpose of the bot. The discord bot is deployed using a free cloud platform called, "Heroku," to stay online without having to run the script on a local computer. It can also restrict different users and channels to communicate.
Once a user sends a ".npy" file containing the brain wave data, Wave will run the data pre-processing and modelling to predict the emotion. 

As a discord bot, it is very user-friendly and quickly can be deployed anywhere on your desktop, laptop, or even mobile devices. 
It also has an indefinite possibility and opportunities to grow and improve upon.


### More detailed explanation of Data Preparation and Model Creation

## Data Preparation
> 1. From the [ZuCo 2.0 dataset](https://osf.io/2urht/) (CC-By Attribution 4.0 International), select random preprocessed datasets. Then, extract the brainwave (alpha, beta, gamma, theta) data and corresponding words.
> 2. For each word, monochromatically plot (without axes) the alpha, beta, theta and gamma brainwave and stack all of them in channel direction (similar to the way that RGB image is formed).
> 3. For each word, compute the similarity between each classes of emotions ["sadness", "happiness", "disgust", "neutral", "anger", "fear"]. Obtaining a word embedder (in this case pretrained word2vec), we are able to compute similarity between two words. Thus, we compare word and the name of emotions listed in last sentence.
> 4. Save stacked image in .npy format. This is to retain each channel’s information and preventing it to be converted into simple RGB or RGBA image
> 5. Store file name of images, word and classification (happiness, sadness, etc) in single csv file
  
Please refer to [this](https://colab.research.google.com/drive/11KG2RCPyd_Uj-Mb2Kp1BplEjscrnwjBi) google colab notebook to view the sample run of the data preparation code.

## Model Creation
> 1. Prepare dataset (image and label pair). If labels are not onehot encoded, do so (I can provide script for this). Make sure to check that your images are in the expected shape.
> 2. Create simple multiclass classification CNN model. Stack few CNN layers and predict soft label. 
> 3. Compile model and fit. 
> 4. Save model after training. 
  
Please refer to [this](https://colab.research.google.com/drive/1SO6GayShC47S1m67pjFdXUDzejM6vJVC#scrollTo=rJA7JDhdaDEt) google colab notebook to view the sample model training run.
