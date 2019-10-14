#This file will contain the methods and class that will deal with all the data

#importing supporting libraries
import numpy as np
import pandas as pd

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
            character_data_set = self.data
            season_data_set = self.data[(self.data.Speaker == character)]
            lines = len(season_data_set)
            rows.append(character)
            rows.append(int(lines))
            season_data.append(rows)
        return season_data

# data = Data()
# #data.test()
# data.seasonLineCountByCharacter(2)
