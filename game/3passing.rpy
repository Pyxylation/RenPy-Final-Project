# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label passing:

    # 7 years
    scene bg 7yearslater
    " "
    #salary increase
    $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(7, "salaryNick"))
    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(7, "salaryWhit"))

    #display salary
    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')


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

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 7, .025)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 7, .01)))

    #Stock Stuff, random between -2 and 8% increase/decrease
    #FedEx
    $oFedEx = balanceSheet.getValue("fedExStock") #original fedEx portfolio vlaue
    $fedExStockGL = int(stockMarket(8, "fedExStock")) #profit made during 8 years
    $fedEx = int(balanceSheet.getValue("fedExStock")) #current fedEx protfolio value
    $fedExShare = int(fedEx/100) #price of stock per share

    #fedEx stock if then statement
    #$fedExGL = "nOTHING"
    $fedExStatus = "nothing"
    if fedEx > oFedEx:
        $fedExStatus = "looking excellent!"
        $fedExGL = "gain." #if there is loss or gain
    elif kB == oKB:
        $fedExStatus = "doing alright."
        $fedExBGL = "the same."
    else:
        $fedExStatus = "looking bad."
        $fedExGL = "loss"

    #K&B
    $oKB = balanceSheet.getValue("k&bStock") #original fedEx portfolio vlaue
    $kBStockGL = int(stockMarket(8, "k&bStock")) #profit made during 8 years
    $kB = int(balanceSheet.getValue("k&bStock")) #current fedEx protfolio value
    $kBShare = int(kB/100) #price of stock per share
    $kBGL = "nOTHING"
    $kBStatus = "nothing"
    #fedEx stock if then statement
    if kB > oKB:
        $kBStatus = "looking great!"
        $kBGL = "gain." #if there is loss or gain
    elif kB == oKB:
        $kBStatus = "doing okay."
        $kBGL = "the same."
    else:
        $kBStatus = "looking problematic."
        $kBGL = "loss"


    $adjustedRandJobNum = 0
    #Really Big Data Update
    $rdbRand = renpy.random.randint(0, 100)
    $rbdStatus = "empty"
    if rdbRand < 45:
        $rbdStatus = "Theyre doing well and gaining reputation for great business analytics"
        $randJobNum += 10
    elif rdbRand >= 45 and rdbRand < 80:
        $rbdStatus = "They have been doing okay, but still working on improving their business"
    elif rdbRand >= 80:
        $rbdStatus = "They haven't been doing that well... Hopefully they can improve in the future."
        $randJobNum -= 5

    #Addings 401K deferals and totaling,, DONT FORGET THE EMPLOYERS CONTRIBUTION $.50 on the dollar, up to 3% then adding to loadBalanceSheet
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*7)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
    $k401 = balanceSheet.getValue("401K")

    #Increases 401K deferal amount in cashFlowStatement. 3% of total salary
    $cashFlowStatement.changeItemValue('401K', int(cashFlowStatement.getValue("salaryNick")*.25))

    #How much money is saved for a house
    $housePayment = cashFlowStatement.getValue("houseDownPay")
    $eightHousePay = (housePayment*7)
    $balanceSheet.changeItemValue("houseDownPay", eightHousePay)

    $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*7
    $balanceSheet.incItemValue("savingsAcc", nickCashFlow)

    $savings = balanceSheet.getValue("savingsAcc")



    scene bg yearslaterbar
    menu:
        "{size=-5}{b}{u}7 Years Later{/u}{/b}
        \n
        - Nick is now 40 years old and earns {c}[salaryNick]{/c}.
        \n- Whitney is now 39 years old and earns {c}[salaryWhit]{/c}.
        \n
        \n {u}Loans{/u}
        \n- Congratulations! Nick has paid off his student loans!
        \n
        \n {u}Investments{/u}
        \n - Nick's K&B portfolio is [kBStatus] Valued at: {c}[kBShare]{/c} per share.
        \n Total value is {c}[kB]{/c}. That's a {c}[kBStockGL]{/c} [kBGL]
        \n - Nick's FedEx portfolio is [fedExStatus] Valued at: {c}[fedExShare]{/c} per share.
        \n Total value is {c}[fedEx]{/c}. That's a {c}[fedExStockGL]{/c} [fedExGL]
        \n
        \n {u}Really Big Data{/u}
        \n [rbdStatus]
        \n
        \n - Nick now has {c}[savings]{/c} in his savings.{/size}":
            jump funeralreal
        "{size=-5}Click Here to Continue{/size}":
            jump funeralreal


label funeralreal:
    scene bg funeral
    with dissolve
    $momDebt = False
    "Oh no! Nick's mom fell ill and passed away!"
    "Because Nick's mom was divorced and Nick was an only child, she passed her estate down to him.
    \nIt wasn't much, only $20,000, because funerals are expensive."

    menu:
        "What does Nick do now? His mom had $15,000 in debt to pay and the creditors are out in force."

        "Pay the debt, keep $5,000":
            "Nick messed up! He never had to pay the debt because it's not legally his responsibility to pay."
            $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc")+5000)
            $lifePoints += 10

        "Contact the creditors and tell them Nick will pay half. He keeps $7,500.":
            "Sadly, when you even give $1 to the creditors, you assume the debt.
            \nCreditors are slimy and they will be back for more later..."
            "The benefit now is that Nick can use this money to invest and make more before its taken."
            $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc") + 12500)
            $lifePoints += 20
            $momDebt = True

        "Don't pay any of it, keep everything! Begone creditors!":
            "Good decision! Nick doesn't have to pay the debt because it's not his!"
            $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc")+20000)
            $lifePoints += 100




jump expanding
