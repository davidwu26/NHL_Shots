from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from Player import PlayerLog


# This function draws a rink based on NHL rink guidelines
# Each unit is one ft
# Parameters: ax: Axes, optional, the axes object to plot the court onto
# Return: ax: An Axes object with rink background
def drawRink(axes=None):
    # Measurements in ft
    X_LENGTH = 100
    Y_LENGTH = 85
    HALF_Y = 42.5
    LINE_WIDTH = 2

    # If axes object is not given
    if axes is None:
        axes = plt.gca() 
    # Middle faceoff zone
    centerOuterArc = Arc((0, 0), 30, 30, theta1=270, theta2=90, color="blue")
    centerInnerCircle = Circle((0, 0), radius=1, color="blue")
    centerLine = Rectangle((-LINE_WIDTH / 2, -HALF_Y), width=LINE_WIDTH,
                            height=Y_LENGTH, color="red")

    # Blueline
    blueLine = Rectangle((25, -HALF_Y), width=LINE_WIDTH, 
                            height=Y_LENGTH, color="blue")
    neutralZoneFO1 = Circle((20, -22), radius=1, color="red")
    neutralZoneFO2 = Circle((20, 22), radius=1, color="red")

    # Faceoff Circles
    outerCircleTop = Circle((69, 22), radius=15, color="red", fill=False)
    innerCircleTop = Circle((69,22), radius=1, color="red")
    outerCircleBot = Circle((69, -22), radius=15, color="red", fill=False)
    innerCircleBot = Circle((69,-22), radius=1, color="red")

    # Goal line
    goalLine = Rectangle((88, -HALF_Y), width=0.5, height=Y_LENGTH, color="red")
    # Crease
    botCrease = Rectangle((84, -4), width=4, height=0.1, color="red")
    topCrease = Rectangle((84, 3.9), width=4, height=0.1, color="red")
    creaseArc = Arc((84, 0), width=3, height=8, color="red", theta1=90, theta2=270)

    # Border
    topLine = Rectangle((-1, HALF_Y), width=89.5, height=0.1, color="black")
    botLine = Rectangle((-1, -(HALF_Y) - 0.1), width=89.5,
                         height=0.1, color="black")
    backLine = Rectangle((100, -(HALF_Y) + 6), height=Y_LENGTH-12, 
                        width=0.1, color="black")
    botArc = Arc((89, -(HALF_Y) + 5.9), width=22, height=12,
                     color="black", theta1=-100, theta2=2)
    topArc = Arc((89, (HALF_Y) - 5.9), width=22, height=12, 
                    color="black", theta1=-2, theta2=100)
    # List of elements of rink to be plotted
    rink = [centerOuterArc, centerInnerCircle, centerLine,
            blueLine, neutralZoneFO1, neutralZoneFO2,
            outerCircleTop, outerCircleBot, innerCircleBot, innerCircleTop,
            goalLine, botCrease, topCrease, creaseArc,
            topLine, botLine, backLine, botArc, topArc]

    for i in rink:
        axes.add_patch(i)    
    return axes


def basicChart(player, axes=None, s=3):
    if axes is None:
        axes = plt.gca()
    
    shotColors = {"SHOT": "green", "MISSED_SHOT": "blue", "BLOCKED_SHOT": "cyan", "GOAL": "red"}
    df = player.df
    groups = df.groupby("result")
    drawRink(axes)
    for name, group in groups:
        axes.scatter(group.x, group.y, c=shotColors[name], label=name)
    axes.set_title(player.getPlayer())
    axes.set_aspect('equal')
    axes.legend()
    return axes

def setValue(rowNumber, assignedValue):
        return assignedValue[rowNumber]

# Example with Steven Stamkos
stamkos = PlayerLog("Steven Stamkos", 2017)
ax = basicChart(stamkos, None, 20)
plt.show()