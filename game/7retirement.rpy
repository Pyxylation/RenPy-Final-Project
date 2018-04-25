# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label retirement:

    #5 years
    scene bg 5yearslater

    if nickIsCrazy == False:
        #salary increase
    #    $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(5, "salaryNick"))
    #    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(5, "salaryWhit"))

        #display salary
        $salaryNick = cashFlowStatement.getValue('salaryNick')
        $salaryWhit = cashFlowStatement.getValue('salaryWhit')
        "Nick is now 65 years old and earns $[salaryNick]
        \nWhitney is now 64 years old and earns $[salaryWhit]"

        #new 401K calcualtion
        $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

        #calculate new federal tax based on income
        $fedTax()
        #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
        $ficaCalcAdd()

        #change stuff for 3% inflation, only food and fun!
        #Entertianment
        $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 5, .03)))
        #food
        $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 5, .03)))

        #Stock Stuff, random between -2 and 8% increase/decrease
        #FedEx
        $oFedEx = balanceSheet.getValue("fedExStock") #original fedEx portfolio vlaue
        $stockProfit = int(stockMarket(5, "fedExStock")) #profit made during 8 years
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
        $stockProfit = int(stockMarket(5, "k&bStock")) #profit made during 8 years
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
        $eightHousePay = (housePayment*5)
        $balanceSheet.changeItemValue("houseDownPay", eightHousePay)

        $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*5
        $balanceSheet.incItemValue("savingsAcc", nickCashFlow)
        $savings = balanceSheet.getValue("savingsAcc")
        "Nick now has $[savings] in his savings."

    else:
        "Nick is crazy. He doesnt trust the system. So, he cant get paid."


    scene bg retirement

    #TODO Total everying with the total amount
    if nickIsCrazy == True:
        $money = balanceSheet.getValue("matressBank")

    else:
        $money = (balanceSheet.getValue("checkingAcc") + balanceSheet.getValue("savingsAcc") + balanceSheet.getValue("fedExStock"))
        $money += (balanceSheet.getValue("k&bStock") + balanceSheet.getValue("growthMutualFund") + balanceSheet.getValue("401K"))

    "Congradualtions!!! Its retirement time!!!"
    "Lets see how money and life points you ended up with!
    \n Life Points [lifePoints] & Money $[money]"

    if money >= 1000000:
        menu:
            "You made it to retirement!
            \nWhere would you like to live?"
            "Beach":
                "Congrats"
            "Relaxing Subburb":
                "Great"

            "THE MOUNTIANS!!! THE GOVERNMENT IS OUT TO GET ME AND CIVILIZATION AND TECHNOLOGY HAS NOTHING FOR ME!!!" if nickIsCrazy:
                "Shoot!"

    else:
        "Sorry... You didn't make it to 1 million...
        \n You played ya'self kid..."

    scene bg credits
    "Thanks!"




#this ends the game
return
