"""
Number 7
"""

from adafruit_clue import clue
from adafruit_clue import board
from time import sleep
from random import seed
from random import randint


clue_display = clue.simple_text_display(text_scale=2,)


for i in range(3,0,-1):
    clue_display[2].text = "Instructions:"
    clue_display[2].color = clue.GREEN
    clue_display[3].text = "Player A presses A"
    clue_display[3].color = clue.WHITE
    clue_display[4].text = "Player B presses B"
    clue_display[4].color = clue.WHITE
    clue_display[5].text = "Press if the numer"
    clue_display[5].color = clue.SKY
    clue_display[6].text = " is divisible by 2"
    clue_display[6].color = clue.SKY
    clue_display[7].text = "Maximum score of 5"
    clue_display[7].color = clue.YELLOW
    clue_display[8].text = "Starts in " + str(i)
    clue_display[8].color = clue.ORANGE
    clue_display.show()

    sleep(0.2)
value = 0
while True:

    clue_display[0].text = "REACTION GAME"
    clue_display[0].color = clue.ORANGE

    clue_display[0].text = "REACTION GAME"
    clue_display[0].text = "REACTION GAME"
    clue_display[0].text = "REACTION GAME"
    clue_display[0].text = "REACTION GAME"
    clue_display[0].text = "REACTION GAME"
    clue_display[0].text = "REACTION GAME"



    # playerScoreA = 0
    # playerScoreB = 0

    # if playerScoreA == 5 or playerScoreB == 5:
    #     clue_display[2] = ""
    #     clue_display[3] = "Win the Game!"
    # else:
    #     ranNum = randint(0,100)
    #     clue_display[3].text = ranNum
    #     sleep(0.3)

        # if clue.button_a:
        #     print("press")
        # #    if ranNum % 2 == 0:
        # #        playerScoreA = playerScoreA + 1
        # else:
        #         # playerScoreA = playerScoreA - 1
        #         print("not")



    # if btnA == True  and ranNum % 2 == 0 :
    #     playerScoreA = playerScoreA + 1
    # else:
    #     playerScoreA = playerScoreA -1

    # if btnB and ranNum % 2 == 0 :
    #     playerScoreB = playerScoreB + 1
    # else:
    #     playerScoreB = playerScoreB -1


    

    # clue_display[5].text = "Player A Score: " + str(playerScoreA)
    # clue_display[5].color = clue.GREEN

    # clue_display[6].text = "Player B Score: " + str(playerScoreB)
    # clue_display[6].color = clue.SKY


    clue_display.show()