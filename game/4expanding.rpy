# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label expanding:

    # 5 years

    #salary increase
    # $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(5, "salaryNick")), nicks salary gets capped
    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(5, "salaryWhit"))

    #display salary
    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')
    "Nick is now 45 years old and earns $[salaryNick]. His salary has maxed out at his current job.
    \nWhitney is now 44 years old and earns $[salaryWhit]"

    #new 401K calcualtion
    $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

    #calculate new federal tax based on income
    $fedTax()
    #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
    $ficaCalcAdd()

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
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*5)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
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



    scene bg neighborhood
    with dissolve

    "BOOM! Its time have a kid! 99\%\ effective didnt matter here"
    "Suprise baby"

    $randBaby = renpy.random.randint(0, 1)

    if randBaby == 0:
        scene bg boy
        $randBoy = renpy.random.choice(["Noah", "Liam", "Jacob", "William", "Ethan", "James", "Micheal", "Beenjamin'", "Elijah", "Daniel", "Aiden", "Logan", "Matthew", "Lucas", "Jackson", "David", "Oliver"])
        "           Its a boy!!!!"
        "Nick and Whittney named him [randBoy]! "
    else:
        scene bg girl
        $randGirl = renpy.random.choice(["Emma", "Olivia", "Sophia", "Ava", "Isabella", "M.I.A.", "Abigail", "Emily", "Charlotte", "Harper", "Madison", "Amelia", "Elizabeth", "Sofia", "Evelyn", "Chloe", "Ella"])
        "           It's a girl!!!"
        "Nick and Whittney named her [randGirl]! "

    $cashFlowStatement.addItem("outflows", "child", "Cost of a Child", 13000)

    scene bg neighborhood
    with dissolve

    "Since Nick and Whitney now have a baby, they want to buy their very own house!"

    menu:
        #FIXME Figure out house prices
        "Where should they live?"
        "City: $400000 15 year loan with a rate of 7.5\%\ Average $3708 monthly mortgage payment":
            #scene bg cityHouse
            "Congradualtions! Nick and Whitney are city-slickers now!"
            $balanceSheet.removeItem("houseDownPay")
            $lifePoints += 120
        "Suburb: $200000, 15 year loan with a rate of 7.5\%\ Average $1854 monthly mortgage payment": #Need escape character for a %, so \%\
            #scene bg subHouse
            "Congradulations! Nick and Whitney own a house in the subburb now!"
            $balanceSheet.removeItem("houseDownPay")
            $lifePoints += 85


jump theft
