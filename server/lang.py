#This file will deal with some of the language processing aspects of this project
##Import libararies
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

class Lang():

    def test(self):
        my_stopwords = set(STOPWORDS)
        two_cities = """It was the best of times, it was the worst of times, it was the age of
        wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of
        incredulity, it was the season of Light, it was the season of Darkness, it was the spring
        of hope, it was the winter of despair, we had everything before us, we had nothing before
        us, we were all going direct to Heaven, we were all going direct the other way—in short,
        the period was so far like the present period, that some of its noisiest authorities insisted
        on its being received, for good or for evil, in the superlative degree of comparison only."""
        my_cloud = WordCloud(background_color='white', stopwords=my_stopwords).generate(two_cities)
        plt.imshow(my_cloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

# lang = Lang()
# lang.test()

#example 1
## Define the stopwords list
# my_stopwords = set(STOPWORDS)
# my_stopwords.update(['movie', 'movies', 'film', 'films', 'watch', 'br'])

#Generate and show the word cloud
# my_cloud = WordCloud(background_color='white', stopwords=my_stopwords).generate(name_string)
# plt.imshow(my_cloud, interpolation='bilinear')

### Example 2

# two_cities = """It was the best of times, it was the worst of times, it was the age of
# wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of
# incredulity, it was the season of Light, it was the season of Darkness, it was the spring
# of hope, it was the winter of despair, we had everything before us, we had nothing before
# us, we were all going direct to Heaven, we were all going direct the other way—in short,
# the period was so far like the present period, that some of its noisiest authorities insisted
# on its being received, for good or for evil, in the superlative degree of comparison only."""

#cloud = WordCloud().generate(two_cities) # ?WordCloud

#my_cloud = WordCloud(background_color='white', stopwords=my_stopwords).generate(descriptions)

# plt.imshow(cloud, interpolation='bilinear')
#
# plt.axis('off')
# plt.show()
