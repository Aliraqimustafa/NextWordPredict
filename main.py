# Load Data
import NextWord
from datasets import load_dataset

imdb_dataset = load_dataset("imdb")
data = []
for row in imdb_dataset['train']:
    data.append(row['text']) 
for row in imdb_dataset['test']:
    data.append(row['text']) 
for row in imdb_dataset['unsupervised']:
    data.append(row['text']) 

# Save Data

with open('imdb.txt','w') as file:
    for row in data:
        file.write(row)

# Load Data after save it
path_data = 'imdb.txt'
data = open(path_data).read().lower()


# Set NextWord obj
NW = NextWord(data)

# Train obj for data
NW.train()

# Predictions
NW.predict('The')