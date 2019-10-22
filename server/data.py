#This file will contain the methods and class that will deal with all the data

#importing supporting libraries
import numpy as np
import pandas as pd
from textblob import TextBlob

class Data():

    def __init__(self):
        self.data = pd.read_csv('./data/SATC_all_lines.csv')

    def test(self):
        print(self.data.head())

    #This method will get the number of lines spoken by the four main charachers
    #for each season.
    def seasonLineCountByCharacter(self, season):
        #Here I get a smaller data set based on where the season is set to
        #what the user wants.
        season_data_set = self.data[(self.data.Season == season)]
        season_data = []
        #This list will hold the main characters that will be examined
        characters = ['Carrie', 'Miranda', 'Charlotte', 'Samantha']
        columns = ['Character', 'Lines']
        season_data.append(columns)
        #looping through the characters list
        for character in characters:
            rows = []
            #resetting the dataset each time we loop through the data.
            character_data_set = season_data_set
            speaker_data_set = character_data_set[(character_data_set.Speaker == character)]
            lines = len(speaker_data_set)
            rows.append(character)
            rows.append(int(lines))
            season_data.append(rows)
        return season_data

    #This method will get the sentiment of the lines spoken by the four main characters
    #for each season. How this will work is that each line, by character, will get its sentiment
    #and then an average will be found.
    def sentimentByCharacter(self, season):
        #Here I get a smaller data set based on where the season is set to
        #what the user wants.
        season_data_set = self.data[(self.data.Season == season)]
        season_data = []
        #This list will hold the main characters that will be examined
        characters = ['Carrie', 'Miranda', 'Charlotte', 'Samantha']
        columns = ['Character', 'Lines']
        season_data.append(columns)
        #looping through the characters list
        for character in characters:
            rows = []
            #resetting the dataset each time we loop through the data.
            character_data_set = season_data_set
            speaker_data_set = character_data_set[(character_data_set.Speaker == character)]
            valance_list = []
            for line in speaker_data_set['Line']:
                valance = TextBlob(line)
                valance_list.append(valance.sentiment[0])
            list_total = sum(valance_list)
            average = list_total / len(valance_list)
            rows.append(character)
            rows.append(int(average))
            season_data.append(rows)
        print(season_data)




# text = "Today was a good day"
# my_valance = TextBlob(text)
# print(my_valance)
# print(my_valance.sentiment)

data = Data()
# data.test()
data.sentimentByCharacter(1)
