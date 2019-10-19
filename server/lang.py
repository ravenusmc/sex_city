#This file will deal with some of the language processing aspects of this project
##Import libararies
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

class Lang():

    def __init__(self):
        self.data = pd.read_csv('./data/SATC_all_lines.csv')

    def seasonWordCloud(self, season):
        season_data_set = self.data[(self.data.Season == season)]
        count = 0
        #This is the specific place that
        line_count = season_data_set.index[0]
        lines = []
        while count < len(season_data_set):
            try:
                line = str(season_data_set['Line'][line_count])
            except KeyError:
                print('Error, but program will continue to function')
            lines.append(line)
            count += 1
            line_count += 1
        lines = ' '.join(lines)
        my_stopwords = set(STOPWORDS)
        word_cloud = WordCloud(background_color='white', stopwords=my_stopwords).generate(lines)
        plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()


lang = Lang()
lang.seasonWordCloud(6)
