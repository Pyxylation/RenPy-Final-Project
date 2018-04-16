﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define n = Character("Nick")

init python:
    #calculate compound interest
    def compInt(principal, years, interest): #interest needs to be in DECIMALS
        return principal*(1 + (interest/1))**years
    #calcualte salary increase
    def salaryIncrease(years, person): #interest needs to be in DECIMALS
        return int(compInt((cashFlowStatement.getValue(person)), years, (float(renpy.random.randint(3, 5))/100)))
    #calculate new federal tax
    def fedTax():
        cashFlowStatement.changeItemValue("fedTax", int((cashFlowStatement.getValue("salaryNick") + cashFlowStatement.getValue("salaryWhit") - cashFlowStatement.getValue("401k"))*.25))
        return
    #calculate FICA and add it to cashFlowStatement
    def ficaCalcAdd(): #interest needs to be in DECIMALS
        cashFlowStatement.changeItemValue("ficaTax", int(((salaryWhit + salaryNick)*.0765)))
        return



# The game starts here.
label start:
    call loadCashflow
    call loadBalanceSheet

    $lifePoints = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # file formats need to be either .png or .jpg, dont use .gif
    scene bg house
    "Welcome to (Insert Finance Simulation Game Name Here)"
    "This game will be a guide to helping you make financial decisions throughout your life"
    "There are two goals of the Game:
        \nFirst you need to collect 1 Million dollars for retirement
        \nSecond: You need to amass Life Points (LP). Which show how much life experince you got"

jump Investment
