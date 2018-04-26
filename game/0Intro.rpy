# The script of the game goes in this file.

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
        cashFlowStatement.changeItemValue("fedTax", int((cashFlowStatement.getValue("salaryNick") + cashFlowStatement.getValue("salaryWhit") - cashFlowStatement.getValue("401K"))*.25))
        return
    #calculate FICA and add it to cashFlowStatement
    def ficaCalcAdd(): #interest needs to be in DECIMALS
        cashFlowStatement.changeItemValue("ficaTax", int(((salaryWhit + salaryNick)*.0765)))
        return
    def stockMarket(years, stockName): #random stock price generator over X years!
        i = 0
        profits = 0
        while i <= years:
            stockValue = balanceSheet.getValue(stockName)
            randNum = (float(renpy.random.randint(-3, 8))/100)
            newValue = int(stockValue*(1+randNum))
            balanceSheet.changeItemValue(stockName, newValue)
            profits += (stockValue*(randNum))
            i += 1
        return profits

    #use: "Your savings is {c}[savingsTotal]{/c}" results in: Your Savings is $7,500
    def c_tag(tag, argument, contents):

        result = []

        for kind, text in contents:

            if kind == renpy.TEXT_TEXT:
                try:
                    convertedText = "$" + locale.format("%.0f", float(text), grouping=True)
                except ValueError:
                    convertedText = text
        result.append((kind, convertedText))

        return result

    config.custom_text_tags["c"] = c_tag

# The game starts here.
label start:
    call loadCashflow
    call loadBalanceSheet

    $lifePoints = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # file formats need to be either .png or .jpg, dont use .gif
    scene bg introhousereversegrey
    "Welcome to 'The Clintons: No, Not the Famous Ones!'"
    "This game will be a guide to helping Nick Clinton make financial decisions throughout his life."
    "There are two goals of the game:
        \nFirst: You need to help Nick collect 1 Million dollars for retirement
        \nSecond: Nick needs to amass Life Points (LP), which represents the quality of Nick's life experiences"

jump Investment
