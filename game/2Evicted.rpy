# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# This is 2 years after the investment right now, we can always change it
label evicted:

    # scene bg timesChange

    #salary increase
    $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(8, "salaryNick"))
    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(8, "salaryWhit"))

    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')

    "Nick is now 33 years old and earns $[salaryNick]
    \nWhitney is now 32 years old and earns $[salaryWhit]"

    $cashFlowStatement.changeItemValue("401k", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

    #calculate new federal tax based on income
    $fedTax()

    #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
    $ficaCalcAdd()

    #Student loan payments
    $balanceSheet.changeItemValue("nicholasLoan", int((balanceSheet.getValue("nicholasLoan") - (cashFlowStatement.getValue("studentLoan"))*8)))
    $loan = balanceSheet.getValue("nicholasLoan")
    "Nick still has $[loan] of student loans to pay off. "

    #Auto loans
    "Congradulations! Auto loans have been paid off"
    $balanceSheet.changeItemValue("autoLoan", .01)
    $cashFlowStatement.changeItemValue("autoLoan", 0)
    #it only took 1.5 years to pay off the car... So, that extra 5.4K needs to be given back. 7.5*5.4K
    $balanceSheet.changeItemValue("savingsAcc", int((balanceSheet.getValue("savingsAcc"))+(5400*7.5)))
    #furnature loans
    "Congradulations! Nicks furniture loan has also been paid off!
        \nNot sure why he wanted it in the first place..."
    $balanceSheet.changeItemValue("savingsAcc", int((balanceSheet.getValue("savingsAcc"))+(2300*7.5)))
    $cashFlowStatement.changeItemValue("furnitureLoan", 0)

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 8, .03)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 8, .03)))

    #Stock Stuff, general rule 8% a year
    #FedEx
    $oFedEx = balanceSheet.getValue("fedExStock") #original fedEx price

    #$fedExUpdate =  (compInt((balanceSheet.getValue("fedExStock")), 8, (float(renpy.random.randint(-2, 8))/100)))
    $balanceSheet.changeItemValue("fedExStock", int((compInt((balanceSheet.getValue("fedExStock")), 8, (float(renpy.random.randint(-2, 8))/100)))))
    $stock = balanceSheet.getValue("fedExStock")
    $difference = stock - oFedEx
    #fedEx stock if then statement
    if stock > oFedEx:
        "FedEx is doing well at $[stock]. Thats a $[difference] increase!"
    elif stock == oFedEx:
        "FedEx has not changed at $[stock]"
    else:
        "FedEx sucks at $[stock]. Its down $[difference]."
        #block of code to run



    #Really Big data
    #$rbdSuccessGenerator = renpy.randomInt(1, 3)


    #fun money amounts to add LifePoints







    scene bg evicted

    "Oh no! Nick's Turkish landlord is tired of nick forgetting to pay
        and has his second cousin twice removed is visiting. He wants to give that cousin a place to stay."
    "Because Nick made the mistake of becoming an 'At will tenant,' he has no lease and will need to find a new house"



jump expanding
