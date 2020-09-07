import json
import requests

url = "https://statsapi.web.nhl.com/api/v1/game/{season}{type}{gameNum}/feed/live"
shotTypes = ["SHOT", "MISSED_SHOT", "BLOCKED_SHOT", "GOAL"]


# Determines number of games before and after Vegas joined league
def numGames(year):
    if year < 2017:
        return 1230
    else:
        return 1271


# Converts game number to format XXXX for API access
def numToString(num):
    num = str(num)
    while len(num) < 4:
        num = "0" + num
    return num


# Gets shots in a year and saves it to a text file 
def getRegularSeasonShots(year):
    games = numGames(year)
    shots = {}
    for i in range(1, games):
        try:
            # For each regular season game gets shots
            r = requests.get(url.format(season=year, type="02",
                             gameNum=numToString(i))).json()
        # Error Handling
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        # If a game does not have play data
        if len(r['liveData']['plays']['allPlays']) == 0:
            continue
        # Iterate through all play data to select shots
        for i in range(0, len(r['liveData']['plays']['allPlays'])):
            print(i)
            if (r['liveData']['plays']['allPlays'][i]['result']['eventTypeId'] in shotTypes):
                shooter = r['liveData']['plays']['allPlays'][i]['players'][0]['player']['fullName']
                result = r['liveData']['plays']['allPlays'][i]['result']['eventTypeId']
                if (r['liveData']['plays']['allPlays'][i]['coordinates']):
                    x = r['liveData']['plays']['allPlays'][i]['coordinates']['x']
                    y = r['liveData']['plays']['allPlays'][i]['coordinates']['y']
                    if x < 0:
                        x = -x
                        y = -y    
                else:
                    x = None
                    y = None
                team = r['liveData']['plays']['allPlays'][i]['team']['name']
                shots.setdefault(shooter, []).append({
                    'result': result,
                    'x': x,
                    'y': y,
                    'team': team})
    # Put information in text file
    with open("shots{season1}{season2}.txt".format(season1=year, season2=year+1), "w+") as outfile:
        json.dump(shots, outfile)
    outfile.close()
    print("Scraping finished!")
