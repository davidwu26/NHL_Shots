# NHL_Shots
This project scrapes the NHL Statistics API for a given season and returns a shot map for a specified player.

## `scrapeShots.py`
This script takes as input a season (Game length must be changed due to COVID seasons and Seattle Kraken Expansion) and saves every player's shot distribution in a text file.

## `Player.py`
This class serves as an object for each player and sets up a Pandas dataframe with his shot data.

## `DrawRink.py`
This script draws a plot of an ice rink and a player's shot distribution for a season.

