# CS-1-2_tweet-generator
This repo is for more than just the tweet generator itself, as the tutorial has several mini-projects within itself. Therefore, the ../mini/ folder is explicitly for these mini-projects.

The root itself, however, is dedicated to the OG Tweet Generator.

## Rearrange Words Randomly
This program will rearrange words randomly. If you give it five words, it will give those five words back in a random order.

In theory, you could recieve the same string back!

##### Instructions:
1. Type `python3 mini/rearrange.py` (don't press enter).
2. Type several parameters to shuffle afterwards.
	- For example, you could type `python3 mini/rearrange.py item1 item2 item3`
3. Press enter.
You should see that it prints a random string of your inputs to console!

## Create Random Sentances
This program will generate random sentances. The sentance length depends on the first parameter that you input, which should be an integer.

It references a dictionary and any other files that you might want it to check through. You can make lists inclusive or exclusive. Inclusive lists guarentee the word will be in the list, while exclusive means that the word will be omitted unless it is in the file. *will clarify this instruction later*

##### Instructions:
1. Type `python3 mini/wordify.py` (don't press enter).
2. This program will take in parameters. Each one will be a seperate word.