########## All URLs ############
demo = 'https://scratch.mit.edu/projects/151017985/#fullscreen'

cY = 'https://scratch.mit.edu/projects/151030464/#fullscreen'
cG = 'https://scratch.mit.edu/projects/151031590/#fullscreen'
cR = 'https://scratch.mit.edu/projects/151031688/#fullscreen'

eY = 'https://scratch.mit.edu/projects/151034263/#fullscreen'
eG = 'https://scratch.mit.edu/projects/151034195/#fullscreen'
eR = 'https://scratch.mit.edu/projects/151034096/#fullscreen'

YGR = 'https://scratch.mit.edu/projects/151027157/#fullscreen'
YRG = 'https://scratch.mit.edu/projects/151028622/#fullscreen'
GRY = 'https://scratch.mit.edu/projects/151036783/#fullscreen'
GYR = 'https://scratch.mit.edu/projects/151029293/#fullscreen'
RYG = 'https://scratch.mit.edu/projects/151029942/#fullscreen'
RGY = 'https://scratch.mit.edu/projects/151036611/#fullscreen'

RG_Y = 'https://scratch.mit.edu/projects/151030159/#fullscreen'
GR_Y = 'https://scratch.mit.edu/projects/151034348/#fullscreen'
RY_G = 'https://scratch.mit.edu/projects/151036192/#fullscreen'
YR_G = 'https://scratch.mit.edu/projects/151035899/#fullscreen'
GY_R = 'https://scratch.mit.edu/projects/151036247/#fullscreen'
YG_R = 'https://scratch.mit.edu/projects/151036340/#fullscreen'

########## DEMO ############
# open browser
import webbrowser
webbrowser.open_new(demo)

# randomize lightbulb order
import random
light = ['Y', 'G', 'R']
random.shuffle(light)
print("This is the demo order: " + str(light))

########## PRACTICE ############
# open pratice trials in the order of YR_G, GYR, cG, eR
import webbrowser, os
webbrowser.open('file://' + os.path.realpath('EI_practices.html'))

############# TEST ###########
# original puzzles (9, 12, 27), i.e. set A - 1, 3, 5: (YGR, cY), (YGR, GR_Y), (eY, RY_G)
# answer: G, Y, G
# exchange G with R
# new puzzles, i.e., set B - 2, 4, 6: (YRG, cY), (YRG, RG_Y), (eY, GY_R)
# answer: R, Y, R

# two equivalent problem sets
## set A: puzzle 1, 3, 5
testPair_A = [(YGR, cY), (YGR, GR_Y), (eY, RY_G)]
puzzle_A = [1, 3, 5]
correctIV_A = ['G', 'Y', 'G']

## set B: puzzle 2, 4, 6
testPair_B = [(YRG, cY), (YRG, RG_Y), (eY, GY_R)]
puzzle_B = [2, 4, 6]
correctIV_B = ['R', 'Y', 'R']

# scramble problem order within set
## set A
orderTest_A = list(zip(testPair_A, puzzle_A, correctIV_A))
random.shuffle(orderTest_A)
testPair_A, puzzle_A, correctIV_A = zip(*orderTest_A)

## set B
orderTest_B = list(zip(testPair_B, puzzle_B, correctIV_B))
random.shuffle(orderTest_B)
testPair_B, puzzle_B, correctIV_B = zip(*orderTest_B)

## randomize the order of the two sets
counterbalance = random.choice([1,2])

if  counterbalance == 1:
    setAB = "A";
    testPair = testPair_A + testPair_B
    puzzle = puzzle_A + puzzle_B
    correctIV = correctIV_A + correctIV_B
else:
    setAB = "B";
    testPair = testPair_B + testPair_A
    puzzle = puzzle_B + puzzle_A
    correctIV = correctIV_B + correctIV_A
print ("Set " + setAB + " comes first")

## print puzzle order
print("Prepare these pictures: " + str(puzzle))

# randomly choose a graph as the correct answer for each pair
testAnswer = [0, 0, 0, 0, 0, 0]

j = 0
while j < 6:
    testAnswer[j] = random.choice(testPair[j])
    j += 1

# and open the corresponding URLs
k = 0
while k < 6:
    webbrowser.open_new(testAnswer[k])
    k += 1

# which picture comes first in a pair?
choices= [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
choiceOrder=[0,0,0,0,0,0]

l = 0
while l < 6:
    choiceOrder[l] = random.choice(choices[l])
    l += 1

print("First choice to show in each puzzle: " + str(choiceOrder))

# print correct answers
print("Correct intervention for each puzzle: " + str(correctIV))

########## update EI temp google sheet with exp set-up ############
# https://docs.google.com/spreadsheets/d/1gyluz7Whrr3KHMEmoGBosAV59_CDIm48DF90d6LghU4/edit?usp=sharing
# coding: utf-8
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('EI_clientSecret.json', scope)
ra = gspread.authorize(credentials)

sheet = ra.open('EI temp').sheet1
sheet.update_cell(2, 1, str(light))
sheet.update_cell(2, 3, str(setAB))
sheet.update_cell(2, 4, str(puzzle))
sheet.update_cell(2, 5, str(choiceOrder))
sheet.update_cell(2, 6, str(correctIV))
