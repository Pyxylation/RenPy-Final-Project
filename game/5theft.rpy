# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label theft:

    # 10 years

    #salary increase
    # $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(10, "salaryNick")) Nick job capped
    # $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(10, "salaryWhit")) Whitney Capped also

    #display salary
    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')
    "Nick is now 55 years old and earns $[salaryNick]
    \nWhitney is now 54 years old and earns $[salaryWhit]. Her salary is now maxed out."

    #new 401K calcualtion
    $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

    #calculate new federal tax based on income
    $fedTax()
    #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
    $ficaCalcAdd()

    #Student loan payments
    $balanceSheet.changeItemValue("nicholasLoan", int((balanceSheet.getValue("nicholasLoan") - (cashFlowStatement.getValue("studentLoan"))*10)))
    $loan = abs(balanceSheet.getValue("nicholasLoan"))
    $balanceSheet.changeItemValue("nicholasLoan", 0)
    $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc") + loan)
    "Nick has paid off his student loans!!!"

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 10, .03)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 10, .03)))

    #Stock Stuff, random between -2 and 8% increase/decrease
    #FedEx
    $oFedEx = balanceSheet.getValue("fedExStock") #original fedEx portfolio vlaue
    $stockProfit = int(stockMarket(10, "fedExStock")) #profit made during 8 years
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
    $stockProfit = int(stockMarket(10, "k&bStock")) #profit made during 8 years
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
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*10)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
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

    $randJobNum = 70
    "Random Job Number: [randJobNum]"
    # Nick may get a job at Really Big Data!
    if randJobNum >= 65 and nick10K == True:
        scene bg deskjob
        b "Hi Nick! Thanks to your help and investment in Really Big Data we have been doing really well."
        b "Our CMO just left. I was wondering if you wanted the job."
        n "I'd love it! Thank you very much!"
        "Nicks investment finally paid off. His new salary is $110000"
        $cashFlowStatement.changeItemValue("salaryNick", 110000)

    #Nick investing and that paying off
    elif randJobNum >= 65 and nick1K == True:
        scene bg deskbob #This is the normal desk with bobs name on it, not nicks!!!
        b "We are happy to report that Really Big Data is doing well!"
        b "You can finallly get a return on your investment!"
        $roiRBD = renpy.random.randint(10, 15)*1000
        $balanceSheet.incItemValue("savingsAcc", roiRBD)
        "Really Big Data gives you $[roiRBD]"


    #Nick not investing and that paying off, but you dont get anything
    elif randJobNum >=65 and nick10K == False and nick1K == False:
        scene bg deskbob #This is the normal desk with bobs name on it, not nicks!!!
        "You didnt invest, but the company is rockin"

    #The company failing regardless
    else:
        "Really Big Data has just gone bankrupt"
        "Nicks investment had potential, but it wasnt enough to keep them afloat.
            \n Seems that the new data anytics was not needed in the market. "
        $balanceSheet.removeItem("RBD")

    # scene bg identityTheft

    scene bg identitytheft

    "Freaking (Insert some company name) has had yet ANOTHER data breach! Whitney told nick not
        to trust them with personal data."
    #gotta define these before, or else other menu/if statements that use them will crap out because they doesnt exist
    $nickIsCrazy = False
    $identityStolen = False
    menu:
        "What should Nick do about this?"

        "Purchase LifeLock for $15 a month":
            "Excellent choice! Nick feel safe now! He should be fine."
            $lifePoints += 80
            $cashFlowStatement.addItem("outflows", "lifeLock", "LifeLock", 180)


        "Risk it! Because how bad could it really be? These things happen to everyone, right?":
            $lifePoints += 20
            $identityStolen = True

        "TAKE OUT ALL SAVINGS FROM THE BANK AND STORE UNDER MATRESS!!!!!":
            $balanceSheet.addItem("assets", "matressBank", "Money Under Matress", 0)
            $lifePoints += 100
            $nickIsCrazy = True
            $matressBank = balanceSheet.getValue("checkingAcc")
            $balanceSheet.removeItem("checkingAcc")
            $matressBank += balanceSheet.getValue("savingsAcc")
            $balanceSheet.removeItem("savingsAcc")
            $balanceSheet.changeItemValue("matressBank", matressBank)
            "Nick withdraws all the money from his bank account and liquidises all his investements, then adds them to his matress bank."
            "Amount of money under matress: $[matressBank]"

    if momDebt == True:
        "The creditors are back with a vengence!!!
            \nThey want the money you owe them from your moms debt"
        "You owed them $7500, but that has since incrased to $20000."
        if nickIsCrazy == True:
            $balanceSheet.decItemValue("matressBank", 20000)
        else:
            $balanceSheet.decItemValue("savingsAcc", 20000)
    else:
        jump dependent

jump dependent
