from tkinter import *
from random import randrange as rnd, choice
import time
import math

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
Player = input("Input your name:");


def change_position(listOfCoord, numberOfballs):
    for number in range(numberOfballs):
        listOfCoord[number][0] += listOfCoord[number][3]
        listOfCoord[number][1] += listOfCoord[number][4]
        if (listOfCoord[number][0] + listOfCoord[number][2] > 800) or (
                listOfCoord[number][0] - listOfCoord[number][2] < 0):
            listOfCoord[number][3] = -listOfCoord[number][3]
        if listOfCoord[number][1] + listOfCoord[number][2] > 600 or listOfCoord[number][1] - listOfCoord[number][2] < 0:
            listOfCoord[number][4] = -listOfCoord[number][4]
        for numbers in range(numberOfballs):
            if numbers != number:
                if (((listOfCoord[numbers][0] - listOfCoord[number][0]) ** 2 + (
                        listOfCoord[numbers][1] - listOfCoord[number][1]) ** 2) ** 0.5) <= listOfCoord[number][2] + \
                        listOfCoord[numbers][2]:
                    tmp_vx = listOfCoord[numbers][3]
                    tmp_vy = listOfCoord[numbers][4]
                    listOfCoord[numbers][3] = listOfCoord[number][3]
                    listOfCoord[numbers][4] = listOfCoord[number][4]
                    listOfCoord[number][3] = tmp_vx
                    listOfCoord[number][4] = tmp_vy


def new_ball(numberOfPoints, timespent):
    global listOfCoord, numberOfballs
    listOfCoord = [[0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0], [0], [0], [0]]
    listOfCoord[10][0] = numberOfPoints
    listOfCoord[12][0] = timespent
    canv.delete(ALL)
    numberOfballs = rnd(1, 10)
    listOfCoord[11][0] = 0
    for number in range(numberOfballs):
        listOfCoord[number][0] = rnd(100, 700)
        listOfCoord[number][1] = rnd(100, 500)
        listOfCoord[number][2] = rnd(30, 50)
        listOfCoord[number][3] = rnd(-5, 5)
        listOfCoord[number][4] = rnd(-5, 5)
        listOfCoord[number][5] = choice(colors)
    print(listOfCoord)
    show_new_position(listOfCoord, numberOfballs)


def show_new_position(listOfCoord, numberOfballs):
    change_position(listOfCoord, numberOfballs)
    canv.delete(ALL)

    for number in range(numberOfballs):
        canv.create_oval(listOfCoord[number][0] - listOfCoord[number][2],
                         listOfCoord[number][1] - listOfCoord[number][2],
                         listOfCoord[number][0] + listOfCoord[number][2],
                         listOfCoord[number][1] + listOfCoord[number][2],
                         fill=listOfCoord[number][5], width=0)
    canv.create_rectangle(10, 10, 270 + len(Player) * 10, 60, fill='orange')
    textToPrint = Player + " score: " + str(listOfCoord[10][0])
    canv.create_text(20, 35, text=textToPrint,
                     justify=CENTER, font="Verdana 14", anchor=W)
    timeToShow = "Time: " + str(listOfCoord[12][0] // 1000)
    canv.create_text(260 + len(Player) * 10, 35, text=timeToShow,
                     justify=CENTER, font="Verdana 14", anchor=E)


def score(bang, number):
    if bang == 0:
        pass

    elif bang == 1:
        listOfCoord[10][0] += abs(listOfCoord[number][3]) * 10 + abs(listOfCoord[number][4]) * 10 - listOfCoord[number][
            2]
        for count in range(len(listOfCoord[number]) - 1):
            listOfCoord[number][count] = 0
        listOfCoord[11][0] += 1
        if listOfCoord[11][0] == numberOfballs:
            new_ball(listOfCoord[10][0], listOfCoord[12][0])
    elif bang == -1:
        listOfCoord[10][0] -= 1


def tick():
    show_new_position(listOfCoord, numberOfballs)
    listOfCoord[12][0] += 5
    root.after(5, tick)


def click(event):
    print(listOfCoord)
    print(event.x, event.y)
    got_it = 0
    for number in range(numberOfballs):
        if (((event.x - listOfCoord[number][0]) ** 2 + (event.y - listOfCoord[number][1]) ** 2) ** 0.5) <= \
                listOfCoord[number][2]:
            print("BANG!")
            score(1, number)
            got_it += 1
            break
    if got_it == 0:
        score(-1, 0)


new_ball(0, 0)
tick()

canv.bind('<Button-1>', click)

root.mainloop()