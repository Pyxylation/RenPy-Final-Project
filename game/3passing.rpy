# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label passing:

    # 7 years
    scene sevenyears

    #salary increase
    $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(7, "salaryNick"))
    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(7, "salaryWhit"))

    #display salary
    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')
    "Nick is now 40 years old and earns $[salaryNick]
    \nWhitney is now 39 years old and earns $[salaryWhit]"

    #new 401K calcualtion
    $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

    #calculate new federal tax based on income
    $fedTax()
    #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
    $ficaCalcAdd()

    #Student loan payments
    $balanceSheet.changeItemValue("nicholasLoan", int((balanceSheet.getValue("nicholasLoan") - (cashFlowStatement.getValue("studentLoan"))*7)))
    $loan = abs(balanceSheet.getValue("nicholasLoan"))
    $balanceSheet.changeItemValue("nicholasLoan", 0)
    $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc") + loan)
    "Nick has paid off his student loans!!!"

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 7, .03)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 7, .03)))

    #Stock Stuff, random between -2 and 8% increase/decrease
    #FedEx
    $oFedEx = balanceSheet.getValue("fedExStock") #original fedEx portfolio vlaue
    $stockProfit = int(stockMarket(7, "fedExStock")) #profit made during 8 years
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
    $stockProfit = int(stockMarket(7, "k&bStock")) #profit made during 8 years
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


    #Addings 401K deferals and totaling,, DONT FORGET THE EMPLOYERS CONTRIBUTION $.50 on the dollar, up to 3% then adding to loadBalanceSheet
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*7)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
    $k401 = balanceSheet.getValue("401K")
    "Current 401K Savings $[k401]."
    #Increases 401K deferal amount in cashFlowStatement. 3% of total salary
    $cashFlowStatement.changeItemValue('401K', int(cashFlowStatement.getValue("salaryNick")*.03))

    #How much money is saved for a house
    $housePayment = cashFlowStatement.getValue("houseDownPay")
    $eightHousePay = (housePayment*7)
    $balanceSheet.changeItemValue("houseDownPay", eightHousePay)

    $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*7
    $balanceSheet.incItemValue("savingsAcc", nickCashFlow)

    $savings = balanceSheet.getValue("savingsAcc")
    "Nick now has $[savings] in his savings."



    scene bg funeral
    with dissolve
    $momDebt = False
    "Oh no! Nick's mom fell ill and died!"
    "Because Nick was an only child, she passed her estate down to him."
    "It wasnt much, only $20000. Because funerals are expensive."

    menu:
        "What does nick do now? His mom had 15000 in debt to pay."

        "Pay the debt, keep $5000":
            "You screwed up, Nick never had to pay the debt. It's not his"
            $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc")+5000)
            $lifePoints += 10

        "Contact the creditors and tell them you will pay half. You keep $7500.":
            "Sadly, when you even give $1 to the creditors the debt is yours.
            \nCreditors are slimy and they will be back for more later..."
            "The benefit now is that Nick can use this money to invest and make more before its taken"
            $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc") + 12500)
            $lifePoints += 20
            $momDebt = True

        "Dont pay any of it, keep everything. Screw them!":
            "Good decision! Nick doesnt have to pay the debt because its not his!"
            $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc")+20000)
            $lifePoints += 100




jump expanding
