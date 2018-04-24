# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label dependent:

    # 5 years

    if nickIsCrazy == False:
        #salary increase
        #$cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(5, "salaryNick"))
        #$cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(5, "salaryWhit"))

        #display salary
        $salaryNick = cashFlowStatement.getValue('salaryNick')
        $salaryWhit = cashFlowStatement.getValue('salaryWhit')
        "Nick is now 60 years old and earns $[salaryNick]
        \nWhitney is now 59 years old and earns $[salaryWhit]"

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

        $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*5
        $balanceSheet.incItemValue("savingsAcc", nickCashFlow)

        $savings = balanceSheet.getValue("savingsAcc")
        "Nick now has $[savings] in his savings."


        show bg brokenbone

        "Oh no! Nicks dad broke his leg!"
        "After going to the hospital, he realizes that he is unable to take care of himself."
        $crazyBrokenLeg = False
        menu:
            "How should nick help his dad?"
            "Pay monthly rent at a nursing home for dad, $5500":
                $lifePoints += 20
                $cashFlowStatement.addItem("outflows", "nursing", "Nursing Home", 5500)
                "Nick's dad is greatful for his help in paying for a nursing home!
                \nNick will make sure to visit often!"

            "Hire in-home nurse so Nick's dad can still live at his home, $4500":
                $lifePoints += 50
                $cashFlowStatement.addItem("outflows", "nurse", "In-Home Nurse", 4500)
                "Nick's dad is happy that he can continue to live at home and get the help he needs."

            "Whitney quits her job and takes care of Nick's dad at their house, $1000":
                $lifePoints += 100
                $cashFlowStatement.addItem("outflows", "medication", "Nick's Dad Medication", 5500)
                $cashFlowStatement.removeItem("salaryWhit")
                "Nick's dad is extatic that he can live and spend time with Nick and Whitney again!"

        #likelyhood that he loses money from identity being stolen
        $stolenRand = 75 #renpy.random.randint(0, 100)
        if nickIsCrazy == False and identityStolen == True and stolenRand <= 75:
            $stolenMultiplied = stolenRand * 1000
            $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc")-stolenMultiplied)
            "Oh no!!! You should have paid for Life Lock! You lost $[stolenMultiplied]"
        else:
            jump retirement

    else:
        show bg brokenbone

        "Oh no! Nicks dad broke his leg!"
        "After going to the hospital, he realizes that he is unable to take care of himself."
        $crazyBrokenLeg = False
        menu:
            "How should nick help his dad?"
            "Pay monthly rent at a nursing home for dad, $5500":
                $lifePoints += 20
                $cashFlowStatement.addItem("outflows", "nursing", "Nursing Home", 5500)
                "Nick's dad is greatful for his help in paying for a nursing home!
                \nNick will make sure to visit often!"

            "Hire in-home nurse so Nick's dad can still live at his home, $4500":
                $lifePoints += 50
                $cashFlowStatement.addItem("outflows", "nurse", "In-Home Nurse", 4500)
                "Nick's dad is happy that he can continue to live at home and get the help he needs."

            "Whitney quits her job and takes care of Nick's dad at their house, $1000":
                $lifePoints += 100
                $cashFlowStatement.addItem("outflows", "medication", "Nick's Dad Medication", 5500)
                $cashFlowStatement.removeItem("salaryWhit")
                "Nick's dad is extatic that he can live and spend time with Nick and Whitney again!"

            "NICK DOESNT NEED THE COMPROMISED MEDICAL SYSTEM TO MAKE HIS DAD WORSE
            \nNICKS DAD MOVES IN WITH HIM AND NICK FIXES THE BROKEN BONE HIMSELF!" if nickIsCrazy:
                $lifePoints += 120



jump retirement
