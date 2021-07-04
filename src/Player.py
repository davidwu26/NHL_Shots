import matplotlib.pyplot as plt
import json
import pandas as pd
from scrapeShots import getRegularSeasonShots
from os import path

# This class sets up a Player class with his stats
class PlayerLog:
    def __init__(self, player, season):
        self.player = player
        self.season = season
        self.df = self.getDF()

    def getDF(self):
        tf = "shots{year1}{year2}.txt"
        # Check if file exists, if not then scrape it
        if not path.exists(tf.format(year1=self.season, year2=self.season+1)):
            getRegularSeasonShots(self.season)
        # Open file
        with open(tf.format(year1=self.season, year2=self.season+1)) as data:
            shots = json.load(data)
        data.close
        # Set up dataframe
        df = pd.DataFrame(shots[self.player], columns=['result', 'team', 'x', 'y'])
        return df

    def getPlayer(self):
        return self.player
