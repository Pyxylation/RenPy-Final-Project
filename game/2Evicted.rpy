# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# This is 2 years after the investment right now, we can always change it
label evicted:

    scene bg space

    # scene bg timesChange
    # 8 years
    #salary increase
    $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(8, "salaryNick"))
    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(8, "salaryWhit"))

    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')

    "Nick is now 33 years old and earns $[salaryNick]
    \nWhitney is now 32 years old and earns $[salaryWhit]"

    #401K calcualtion
    $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

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
    $balanceSheet.changeItemValue("autoLoan", 0)
    $cashFlowStatement.changeItemValue("autoLoan", 0)
    #it only took 1.5 years to pay off the car... So, that extra 5.4K needs to be given back. 7.5*5.4K
    $balanceSheet.changeItemValue("savingsAcc", int((balanceSheet.getValue("savingsAcc"))+(5400*7.5)))
    #furnature loans
    "Congradulations! Nicks furniture loan has also been paid off!
        \nNot sure why he wanted it in the first place..."
    $balanceSheet.changeItemValue("savingsAcc", int((balanceSheet.getValue("savingsAcc"))+(2300*7.5)))
    $cashFlowStatement.changeItemValue("furnitureLoan", 0)
    $balanceSheet.changeItemValue("furnitureLoan", 0)

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 8, .03)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 8, .03)))

    #Stock Stuff, random between -2 and 8% increase/decrease
    #FedEx
    $oFedEx = balanceSheet.getValue("fedExStock") #original fedEx portfolio vlaue
    $stockProfit = int(stockMarket(8, "fedExStock")) #profit made during 8 years
    $fedEx = int(balanceSheet.getValue("fedExStock")) #current fedEx protfolio value
    $share = int(fedEx/100) #price of stock per share

    #fedEx stock if then statement
    if fedEx > oFedEx:
        "Nicks FedEx portfolio is looking good! Valued at: $[share] per share.
        \n Total value is $[fedEx]. Thats $[stockProfit] in earnings!"
    elif fedEx == oFedEx:
        "FedEx portfolio valued at [fedEx] at $[share] per share"
    else:
        "Nicks FedEx portfolio is down. Valued at: $[share] per share.
        \n Total value is $[fedEx]. Thats $[stockProfit] loss"

    #K&B
    $oKB = balanceSheet.getValue("k&bStock") #original fedEx portfolio vlaue
    $stockProfit = int(stockMarket(8, "k&bStock")) #profit made during 8 years
    $kB = int(balanceSheet.getValue("k&bStock")) #current fedEx protfolio value
    $share = int(kB/100) #price of stock per share

    #fedEx stock if then statement
    if kB > oKB:
        "Nicks FedEx portfolio is looking good! Valued at: $[share] per share.
        \n Total value is $[kB]. Thats $[stockProfit] in earnings!"
    elif kB == oKB:
        "FedEx portfolio valued at [kB] at $[share] per share"
    else:
        "Nicks FedEx portfolio is down. Valued at: $[share] per share.
        \n Total value is $[kB]. Thats $[stockProfit] loss"

        $adjustedRandJobNum = 0
    #Really Big data
    "Finally, lets see if Really Big Data is doing well"
    #RNG 1=doing well, 2=doing okay, 3=doing badly, but there is still a chance
    $rdbRand = renpy.random.randint(0, 100)

    if rdbRand < 45:
        "Theyre doing well and gaining reputation for great business analytics"
        $randJobNum += 10
    elif rdbRand >= 45 and rdbRand < 80:
        "They have been doing okay, but still working on improving their business"
    elif rdbRand >= 80:
        "They haven't been doing that well... Hopefully they can improve in the future."
        $randJobNum -= 5


    #Addings 401K deferals and totaling,, DONT FORGET THE EMPLOYERS CONTRIBUTION $.50 on the dollar, up to 3% then adding to loadBalanceSheet
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*8)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
    $k401 = balanceSheet.getValue("401K")
    "Current 401K Savings $[k401]."
    #Increases 401K deferal amount in cashFlowStatement. 3% of total salary
    $cashFlowStatement.changeItemValue('401K', int(cashFlowStatement.getValue("salaryNick")*.03))

    #How much money is saved for a house
    $housePayment = cashFlowStatement.getValue("houseDownPay")
    $eightHousePay = (housePayment*8)
    $balanceSheet.changeItemValue("houseDownPay", eightHousePay)

    #Now total revenue, dont include stuff taken out for savings, and make sure to take out all the money spent.


    $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*8
    $balanceSheet.incItemValue("savingsAcc", nickCashFlow)
    "[nickCashFlow]"
    $savings = balanceSheet.getValue("savingsAcc")
    "Nick now has $[savings] in his savings."

    #TODO Figure out growth mutal fund, idk what to do with it right now.



    scene bg evicted
    with dissolve
    define l = Character("landlord")

    l "Ayyyy! Nick!!! Get outta here!!!!!"

    "Oh no! Nick's Turkish landlord is tired of Nick forgetting to pay
        and has his second cousin, twice removed is visiting. He wants to give that cousin a place to stay."
    "Because Nick made the mistake of becoming an 'At will tenant,' he has no lease and will need to find a new house"


    menu:

        "Nick and Whitney need to find a place to live quickly. Because this landlord goes crazy and throws away all their stuff.
            \nWhat should they do?"

        "Move in with Whitney's brother. Its free and fun to hangout with her brother again! But, only for a bit till Nick can find another place to stay.":
            "Nick and Whitney had an awesome time spending time with her brother together again!"
            "They're both glad they decided to live together again for a bit"
            $cashFlowStatement.changeItemValue("rent", 11500)
            $lifePoints += 100

        "Find temperary housing, expensive, and Nick will be a tenant at will again.
             \nBut, it may be a fun thing to do till he finds another place for a few months and they find a great new place to live.
             \n$2500 per month":
            $randMonth = renpy.random.randint(2, 4)
            $savings = balanceSheet.getValue("savingsAcc")
            $balanceSheet.changeItemValue("savingsAcc", (savings - (randMonth*2500)))
            $cashFlowStatement.changeItemValue("rent", 12000)
            #dont forget to google about security deposits
            $lifePoints += 80

            "Nick and Whitney had a lot of fun changing things up and living in a cool temperary apartment!
            \nIt helped their "

        "Immediately find a new appartment for $1200 a month. Will be more expensive because rent locally has increased.":
            "Congradualtions! Nick found an apartment and has a proper contract with the renter!
            \nHes glad he wont randomly get kicked out again."
            $cashFlowStatement.changeItemValue("rent", 14400)
            #dont forget to google security deposits
            $lifePoints += 20

    #remove stuff that has been paid off, but doing it down here so people can still see it throughout the scenario
    $balanceSheet.removeItem("autoLoan")
    $cashFlowStatement.removeItem("autoLoan")
    $balanceSheet.removeItem("furnitureLoan")
    $cashFlowStatement.removeItem("furnitureLoan")



jump passing
