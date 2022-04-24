# Raviv Haham, 208387951
# Peleg Haham, 208387969

# Automatically install all the packages that should be installed for running this project
import subprocess
import sys
import pkg_resources
"""
toInstall = {'numpy', 'tqdm', 'matplotlib', 'pygame'}
allReadyInstalled = {pkg.key for pkg in pkg_resources.working_set}
finalToInstall = toInstall - allReadyInstalled
if finalToInstall:
    python = sys.executable
    subprocess.check_call([python, '-m','pip', 'install', *finalToInstall], stdout = subprocess.DEVNULL)
"""
from tkinter import *
from tkinter import messagebox
import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
from inputBox import InputArg
from button import Button

# set all the global parameters:

# set the width and the height of the screen
screenWidth = 900
screenHeight = 600
# set the amount of rows and columns
numOfRows = 200
numOfColumns = 200
# initial the screen size to be screenWidth X screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))
# set the resume flag to true
isResume = True
# set the width and the height of the side panel
sidePanelWidth = 265
sidePanelHeight = 600
# set the size of the cube to be 3 so we will get 200 X 200 metrics screen
cubeSize = 3
# N is the number of creatures
N = 14000
# D is the initial percentage of patients
D = 0.1
# R is the percentage of creatures moving fast
R = 0.3
# X is the several generations until recovery
X = 3
# P_LOW is the chance of infection - the low chance
P_LOW = 0.1
# P_HIGH is the chance of infection - the high chance
P_HIGH = 0.9
# T is the threshold value for changing the value of P as a function of the disease state
T = 0.3
# when shouldStart became true it means the user wants to start the game
shouldStart = False
# array for all the values of the elements that the user insert
setElementsArray = []
# initialize array that will save the patients percent per iteration
patientsArr = []
# the amount of the patients
patientsAmount = 1
# the number of the current iteration
numOfIteration = 0
# sign for all the possible status that creature can be
empty = 0
healthy = 1
recovering = 2
sick = 3


# if the user press on the start button we want to save all the values of all the elements and set shouldStart to true
def start_game():
    """Callback method to start the game."""
    global P_LOW, P_HIGH, X, N, D, R, T, shouldStart, setElementsArray
    for event in pygame.event.get():
        # set the event listener for all the boxes
        for box in setElementsArray:
            box.handle_event(event)
    shouldStart = True
    # check if all the input is correct, otherwise set shouldStart to False
    if float(setElementsArray[0].text) > 1:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='P_LOW should be a number between 0 to 1')
        shouldStart = False
    elif float(setElementsArray[0].text) < 0:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='P_LOW should be a number between 0 to 1')
        shouldStart = False
    else:
        P_LOW = float(setElementsArray[0].text)
    if float(setElementsArray[1].text) > 1:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='P_HIGH should be a number between 0 to 1')
        shouldStart = False
    elif float(setElementsArray[1].text) < 0:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='P_HIGH should be a number between 0 to 1')
        shouldStart = False
    else:
        P_HIGH = float(setElementsArray[1].text)
    if float(setElementsArray[2].text) > 100:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='X should be a number between 0 to 100')
        shouldStart = False
    elif float(setElementsArray[2].text) < 0:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='X should be a number between 0 to 100')
        shouldStart = False
    else:
        X = float(setElementsArray[2].text)
    if float(setElementsArray[3].text) > 40000:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='N should be a number between 0 to 40,000')
        shouldStart = False
    elif float(setElementsArray[3].text) < 0:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='N should be a number between 0 to 40,000')
        shouldStart = False
    else:
        N = float(setElementsArray[3].text)
    if float(setElementsArray[4].text) > 1:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='D should be a number between 0 to 1')
        shouldStart = False
    elif float(setElementsArray[4].text) < 0:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='D should be a number between 0 to 1')
        shouldStart = False
    else:
        D = float(setElementsArray[4].text)
    if float(setElementsArray[5].text) > 1:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='R should be a number between 0 to 1')
        shouldStart = False
    elif float(setElementsArray[5].text) < 0:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='R should be a number between 0 to 1')
        shouldStart = False
    else:
        R = float(setElementsArray[5].text)
    if float(setElementsArray[6].text) > 1:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='T should be a number between 0 to 1')
        shouldStart = False
    elif float(setElementsArray[6].text) < 0:
        Tk().wm_withdraw()
        messagebox.showinfo(title='error alert', message='T should be a number between 0 to 1')
        shouldStart = False
    else:
        T = float(setElementsArray[6].text)





# if the user press on the pause button we want to stap the model in this current iteration and set isResume to true
def stopFunc():
    global isResume, numOfIteration, patientsArr
    # set the value of isResume to false
    isResume = False
    # create a graph of all the patients amount per iteration and show it
    allIterations = np.arange(1, numOfIteration + 1)
    plt.title("The current iteration is " + str(numOfIteration))
    plt.xlabel('Iteration number')
    plt.ylabel('Patients amount')
    plt.plot(allIterations, np.array(patientsArr))
    plt.show()
    while (not isResume):
        for event in pygame.event.get():
            # quit the game if the user press on quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # check all the time is someone press on the resume button
            resume_button.handle_event(event)

# if the user press on the resume button we want to set isResume value to true
def resumeFunc():
    global isResume
    isResume = True


# this function show the first page where the user can set all the values of all the elements
def setSettings():
    global P_LOW, P_HIGH, X, N, D, R, T, shouldStart, setElementsArray
    clock = pygame.time.Clock()
    # set the cover color of the screen
    screen.fill((236, 126, 22))
    pygame.font.init()
    # get all the values of the elements that the user can insert and set
    inputArg1 = InputArg(158, 190, 65, 30, str(P_LOW))
    setElementsArray.append(inputArg1)
    inputArg2 = InputArg(245, 190, 65, 30, str(P_HIGH))
    setElementsArray.append(inputArg2)
    inputArg3 = InputArg(330, 190, 65, 30, str(X))
    setElementsArray.append(inputArg3)
    inputArg4 = InputArg(410, 190, 70, 30, str(N))
    setElementsArray.append(inputArg4)
    inputArg5 = InputArg(495, 190, 65, 30, str(D))
    setElementsArray.append(inputArg5)
    inputArg6 = InputArg(575, 190, 65, 30, str(R))
    setElementsArray.append(inputArg6)
    inputArg7 = InputArg(655, 190, 65, 30, str(T))
    setElementsArray.append(inputArg7)

    # create the start button
    all_buttons = pygame.sprite.Group()
    start_button = Button(335, 340, 180, 55, start_game, pygame.font.SysFont('comicsansms', 20), 'LET\'S START', (255, 255, 255))
    # Add the button to the buttons array
    all_buttons.add(start_button)

    # while the user don't press on the start button
    while not shouldStart:
        for event in pygame.event.get():
            # quit the game if the user press on quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # set the event listener for all the boxes
            for box in setElementsArray:
                box.handle_event(event)
            # set the event listener for all the buttons
            for button in all_buttons:
                button.handle_event(event)

        # set the cover color of the screen
        screen.fill((236, 126, 22))
        # set the font and the color of the text
        textFont = pygame.font.SysFont('comicsansms', 40)
        textColor = pygame.Color('blue')
        # create a txtSurface for each row and write the text
        txtSurface = textFont.render("Set All The Values", True, textColor)
        screen.blit(txtSurface, (245, 80))
        # set the font and the color of the text
        textFont = pygame.font.SysFont('Helvetica', 22)
        textColor = pygame.Color('black')
        txtSurface = textFont.render('P LOW', True, textColor)
        screen.blit(txtSurface, (160, 160))
        txtSurface = textFont.render("P HIGH", True, textColor)
        screen.blit(txtSurface, (245, 160))
        txtSurface = textFont.render("X", True, textColor)
        screen.blit(txtSurface, (352, 160))
        txtSurface = textFont.render("N", True, textColor)
        screen.blit(txtSurface, (432, 160))
        txtSurface = textFont.render("D", True, textColor)
        screen.blit(txtSurface, (520, 160))
        txtSurface = textFont.render("R", True, textColor)
        screen.blit(txtSurface, (595, 160))
        txtSurface = textFont.render("T", True, textColor)
        screen.blit(txtSurface, (680, 160))

        # set the font and the color of the text
        textFont = pygame.font.SysFont('Helvetica', 14)
        textColor = pygame.Color('black')
        txtSurface = textFont.render("P LOW - Chance of being infected when the patients percent is greater than T.", True, textColor)
        screen.blit(txtSurface, (18, 450))
        txtSurface = textFont.render("P HIGH - Chance of being infected when the patients percent is less than T.", True, textColor)
        screen.blit(txtSurface, (18, 470))
        txtSurface = textFont.render("X - Number of generations until recovery.", True, textColor)
        screen.blit(txtSurface, (18, 490))
        txtSurface = textFont.render("N - The number of creatures.", True, textColor)
        screen.blit(txtSurface, (18, 510))
        txtSurface = textFont.render("D - Percentage of the infected creatures in the initial state.", True, textColor)
        screen.blit(txtSurface, (495, 450))
        txtSurface = textFont.render("R - Percentage of creatures that move faster.", True, textColor)
        screen.blit(txtSurface, (495, 470))
        txtSurface = textFont.render("T - Threshold value of the percentage of patients to change the value of P as", True, textColor)
        screen.blit(txtSurface, (495, 490))
        txtSurface = textFont.render("a function of the disease state.", True, textColor)
        screen.blit(txtSurface, (514, 505))

        # set the font and the color of the text
        textFont = pygame.font.SysFont('Helvetica', 22)
        textColor = pygame.Color('black')
        pygame.draw.rect(screen, (0, 0, 0), (100, 575, 10, 10))
        txtSurface = textFont.render("= Empty cell   |", True, textColor)
        screen.blit(txtSurface, (115, 566))
        pygame.draw.rect(screen, (216, 230, 229), (252, 575, 10, 10))
        txtSurface = textFont.render("= Healthy creature   |", True, textColor)
        screen.blit(txtSurface, (267, 566))
        pygame.draw.rect(screen, (255, 0, 0), (452, 575, 10, 10))
        txtSurface = textFont.render("= Sick creature   |", True, textColor)
        screen.blit(txtSurface, (467, 566))
        pygame.draw.rect(screen, (255, 255, 37), (622, 575, 10, 10))
        txtSurface = textFont.render("= Recovering creature   ", True, textColor)
        screen.blit(txtSurface, (637, 566))

        # draw all the boxes
        for box in setElementsArray:
            box.draw(screen)

        # draw all the buttons
        all_buttons.update(pygame.time.Clock().tick(30) / 1000)
        all_buttons.draw(screen)

        pygame.display.flip()
        clock.tick(30)



# The nextLocationSlow function create a move to the slow (regular) creature and return it's new location
def nextLocationSlow(oldBoard,newBoard, x, y):
    maxAttempts = 5
    while maxAttempts > 0:
        xMove = random.randint(-1, 1)
        yMove = random.randint(-1, 1)
        currentRow = (x + xMove + numOfRows)
        currentRow = currentRow % numOfRows
        currentColumn = (y + yMove + numOfColumns)
        currentColumn = currentColumn % numOfColumns
        # check if the random cell is empty in both of the boards
        if ((oldBoard[currentRow][currentColumn][1] == empty) and (newBoard[currentRow][currentColumn][1] == empty)):
            return currentRow, currentColumn
        maxAttempts = maxAttempts - 1
    # if the randomization wasn't succeed we want to create array of all the valid cells
    emptyIndexArr = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            currentX = (x + i + numOfRows)
            currentX = currentX % numOfRows
            currentY = (y + j + numOfColumns)
            currentY = currentY % numOfColumns
            # check if the random cell is empty in both of the boards
            if ((oldBoard[currentX][currentY][1] == empty) and (newBoard[currentX][currentY][1] == empty)):
                emptyIndexArr.append((currentX, currentY))
    if len(emptyIndexArr) > 0:
        selectedIndex = np.random.choice(np.arange(0, len(emptyIndexArr)))
        return emptyIndexArr[selectedIndex][0], emptyIndexArr[selectedIndex][1]
    # stay in the same place
    return x, y


# The nextLocationSlow function create a move to the fast creature and return it's new location
def nextLocationFast(oldBoard,newBoard, x, y):
    maxAttempts = 5
    while maxAttempts > 0:
        xMove = random.randint(-1, 1)
        xMove = xMove * 10
        yMove = random.randint(-1, 1)
        yMove = yMove * 10
        currentRow = (x + xMove + numOfRows)
        currentRow = currentRow % numOfRows
        currentColumn = (y + yMove + numOfColumns)
        currentColumn = currentColumn % numOfColumns
        # check if the random cell is empty in both of the boards
        if ((oldBoard[currentRow][currentColumn][1] == empty) and (newBoard[currentRow][currentColumn][1] == empty)):
            return currentRow, currentColumn
        maxAttempts = maxAttempts - 1
    # if the randomization wasn't succeed we want to create array of all the valid cells
    emptyIndexArr = []
    for i in [-10, 0, 10]:
        for j in [-10, 0, 10]:
            currentX = (x + i + numOfRows)
            currentX = currentX % numOfRows
            currentY = (y + j + numOfColumns)
            currentY = currentY % numOfColumns
            # check if the random cell is empty in both of the boards
            if ((oldBoard[currentX][currentY][1] == empty) and (newBoard[currentX][currentY][1] == empty)):
                emptyIndexArr.append((currentX, currentY))
    if len(emptyIndexArr) > 0:
        selectedIndex = np.random.choice(np.arange(0, len(emptyIndexArr)))
        return emptyIndexArr[selectedIndex][0], emptyIndexArr[selectedIndex][1]
    # stay in the same place
    return x, y




if __name__ == '__main__':
    # call to setSettings function to show the "set options page"
    setSettings()
    # create a pause button
    all_buttons = pygame.sprite.Group()
    pause_button = Button(655, 510, 100, 55, stopFunc, pygame.font.SysFont('comicsansms', 17), 'PAUSE',
                          (255, 255, 255))
    # create a resume button
    resume_button = Button(775, 510, 100, 55, resumeFunc, pygame.font.SysFont('comicsansms', 17), 'RESUME',
                          (255, 255, 255))
    # Add the button to the buttons array
    all_buttons.add(pause_button, resume_button)

    # set the cover color of the screen
    screen.fill((255, 249, 189))
    # initialize the board
    board = []
    for i in range(numOfRows):
        currentRowArray = []
        for j in range(numOfColumns):
            currentRowArray.append(("x", empty))
        board.append(currentRowArray)

    # initialize set of the indexes of the N creatures
    creatureSet = set({})
    while len(creatureSet) != N:
        currentX = random.randint(0, 199)
        currentY = random.randint(0, 199)
        creatureSet.add((currentX, currentY))
    # set D percent of the creatures to be seek
    for currentX, currentY in creatureSet:
        randCreature = np.random.choice([healthy, sick], p=[(1 - D), D])
        if randCreature == healthy:
            # set R percent of the creatures to be faster
            speed = np.random.choice(["f", "s"], p=[R, 1 - R])
            board[currentX][currentY] = (speed, healthy)
        elif randCreature == sick:
            # set R percent of the creatures to be faster
            speed = np.random.choice(["f", "s"], p=[R, 1 - R])
            board[currentX][currentY] = (speed, sick)



    while patientsAmount != 0:
        for event in pygame.event.get():
            # quit the game if the user press on quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # set the event listener for all the buttons
            for button in all_buttons:
                button.handle_event(event)

        # set variables to count the amount of people in each type
        recoveringAmount = 0
        patientsAmount = 0
        healthyAmount = 0

        for i in range(numOfColumns):
            for j in range(numOfRows):
                x = (cubeSize * i)
                y = (cubeSize * j)
                if board[j][i][1] >= sick:
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, cubeSize, cubeSize))
                    patientsAmount = patientsAmount + 1
                elif board[j][i][1] == healthy:
                    pygame.draw.rect(screen, (216, 230, 229), (x, y, cubeSize, cubeSize))
                    healthyAmount = healthyAmount + 1
                elif board[j][i][1] == recovering:
                    pygame.draw.rect(screen, (255, 255, 37), (x, y, cubeSize, cubeSize))
                    recoveringAmount = recoveringAmount + 1
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, cubeSize, cubeSize))

        # draw all the columns lines
        y = 0
        for i in range(numOfColumns + 1):
            x = (cubeSize * i)
            pygame.draw.line(screen, (20, 20, 20), (x, y), (x, 600))
        # draw all the rows lines
        x = 0
        for j in range(numOfRows + 1):
            y = (cubeSize * j)
            pygame.draw.line(screen, (20, 20, 20), (x, y), (600, y))


        tempBoard = []
        for i in range(numOfRows):
            currentRowArray = []
            for j in range(numOfColumns):
                currentRowArray.append(("x", empty))
            tempBoard.append(currentRowArray)



        infected_prob = float(patientsAmount) / N
        if infected_prob >= T:
            current_p = P_LOW
        else:
            current_p = P_HIGH

        # check what changes we should do to create the new board (the board for the next iteration)
        for i in range(numOfColumns):
            for j in range(numOfRows):
                # check how many creatures are patients arrowed this current cell
                patientsCounter = 0
                # we don't want to count the current cell
                if board[j][i][1] >= sick:
                    patientsCounter = patientsCounter - 1
                for t in [-1, 0, 1]:
                    for k in [-1, 0, 1]:
                        currentRow = (j + t + numOfRows)
                        currentRow = currentRow % numOfRows
                        currentColumn = (i + k + numOfColumns)
                        currentColumn = currentColumn % numOfColumns
                        if board[currentRow][currentColumn][1] >= sick:
                            patientsCounter = patientsCounter + 1
                # save the current speed type and the current creature type
                creatureType = board[j][i][1]
                speed = board[j][i][0]
                # check if we should change the type of the creature from healthy to sick
                if creatureType == healthy:
                    chanceOfNotGettingInfected = (1 - current_p) ** patientsCounter
                    if chanceOfNotGettingInfected >= 1:
                        creatureType = healthy
                    else:
                        isGotInfected = np.random.choice([0, 1], p=[chanceOfNotGettingInfected, 1 - chanceOfNotGettingInfected])
                        if isGotInfected:
                            creatureType = sick
                # check if we should change the type of the creature from sick to recovering (because more then X
                # iterations has been passed)
                elif creatureType >= sick:
                    if creatureType == sick + X - 1:
                        creatureType = recovering
                    else:
                        creatureType = creatureType + 1
                # create a move for the current creature according to his type (slow or fast)
                if creatureType != empty:
                    if speed == "s":
                        currentRow, currentColumn = nextLocationSlow(board, tempBoard, j, i)
                    else:
                        currentRow, currentColumn = nextLocationFast(board, tempBoard, j, i)
                    # update the cells in the board and in the temp board
                    tempBoard[currentRow][currentColumn] = (speed, creatureType)
                    board[j][i] = (("x", empty))

        board = tempBoard
        # increasing the iteration counter by 1
        numOfIteration = numOfIteration + 1

        pygame.draw.rect(screen, (192, 212, 205), (635, 0, sidePanelWidth, sidePanelHeight))
        # set the font and the color of the text in the side panel
        textFont = pygame.font.SysFont('Helvetica', 55)
        textColor = pygame.Color('orange')
        if (numOfIteration == 1):
            cr = 20
            cg = 100
            cb = 220
        # write the text in the side panel
        txtSurface = textFont.render('COVID-19', True, textColor)
        screen.blit(txtSurface, (650, 20))
        # set the font and the color of the text in the side panel
        textFont = pygame.font.SysFont('Helvetica', 17)
        textColor = pygame.Color('black')
        txtSurface = textFont.render('ITERATION NUMBER: ' + str(numOfIteration), True, textColor)
        screen.blit(txtSurface, (640, 100))
        pygame.draw.line(screen, (cr, cg, cb), (640, 120), (781, 120))
        txtSurface = textFont.render('NUMBER OF HEALTHY PEOPLE: ' + str(healthyAmount), True, textColor)
        screen.blit(txtSurface, (640, 200))
        pygame.draw.line(screen, (cr, cg, cb), (640, 220), (853, 220))
        txtSurface = textFont.render('NUMBER OF PATIENTS: ' + str(patientsAmount), True, textColor)
        screen.blit(txtSurface, (640, 300))
        pygame.draw.line(screen, (cr, cg, cb), (640, 320), (796, 320))
        txtSurface = textFont.render('NUMBER OF RECOVERING: ' + str(recoveringAmount), True, textColor)
        screen.blit(txtSurface, (640, 400))
        pygame.draw.line(screen, (cr, cg, cb), (640, 420), (823, 420))
        # change the color of the under lines
        cr = (cr + 20) % 255
        cg = (cg + 20) % 255
        cb = (cb + 20) % 255

        # draw all the buttons
        all_buttons.update(pygame.time.Clock().tick(30) / 1000)
        all_buttons.draw(screen)

        # insert the current amount of the patients to the array
        patientsArr.append(patientsAmount)
        pygame.display.update()

    # increase the iteration counter by one when we finish to iterate the current iteration
    allIterations = np.arange(1, numOfIteration + 1)
    # create a graph of all the patients amount per iteration and show it
    plt.title("Patients amount until iteration number " + str(numOfIteration))
    plt.xlabel('Iteration number')
    plt.ylabel('Patients amount')
    plt.plot(allIterations, np.array(patientsArr))
    plt.show()
