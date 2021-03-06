﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label expanding:

    # 5 years
    scene bg 5yearslater
    " "
    #salary increase
    # $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(5, "salaryNick")), nicks salary gets capped
    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(5, "salaryWhit"))

    #display salary
    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')

    #new 401K calcualtion
    $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

    #calculate new federal tax based on income
    $fedTax()
    #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
    $ficaCalcAdd()

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



    #Addings 401K deferals and totaling,, DONT FORGET THE EMPLOYERS CONTRIBUTION $.50 on the dollar, up to 3% then adding to loadBalanceSheet
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*5)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
    $k401 = balanceSheet.getValue("401K")
    #Increases 401K deferal amount in cashFlowStatement. 3% of total salary
    $cashFlowStatement.changeItemValue('401K', int(cashFlowStatement.getValue("salaryNick")*.025))

    #How much money is saved for a house
    $housePayment = cashFlowStatement.getValue("houseDownPay")
    $eightHousePay = (housePayment*5)
    $balanceSheet.changeItemValue("houseDownPay", eightHousePay)

    $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*5
    $balanceSheet.incItemValue("savingsAcc", nickCashFlow)
    $savings = balanceSheet.getValue("savingsAcc")


    scene bg yearslaterbar
    menu:
        "{size=-5}{b}{u}5 Years Later{/u}{/b}
        \n
        - Nick is now 45 years old and earns {c}[salaryNick]{/c}. His salary has maxed out at his current job.
        \n- Whitney is now 44 years old and earns {c}[salaryWhit]{/c}.
        \n
        \n {u}Investments{/u}
        \n - Nick's K&B portfolio is [kBStatus] Valued at: {c}[kBShare]{/c} per share.
        \n Total value is {c}[kB]{/c}. That's is a {c}[kBStockGL]{/c} [kBGL]
        \n - Nick's FedEx portfolio is [fedExStatus] Valued at: {c}[fedExShare]{/c} per share.
        \n Total value is {c}[fedEx]{/c}. That's a {c}[fedExStockGL]{/c} [fedExGL]
        \n
        \n - Nick now has {c}[savings]{/c} in his savings.{/size}":
            jump expandingReal
        "{size=-5}Click Here to Continue{/size}":
            jump expandingReal


label expandingReal:

    scene bg boyorgirl
    with dissolve

    "BOOM! Life finds a way! Whitney is expecting!"

    $randBaby = renpy.random.randint(0, 1)

    if randBaby == 0:
        scene bg boy
        $randBoy = renpy.random.choice(["Noah", "Liam", "Jacob", "William", "Ethan", "James", "Michael", "Beenjamin'", "Elijah", "Daniel", "Aiden", "Logan", "Matthew", "Lucas", "Jackson", "David", "Oliver"])
        "           Its a boy!!!!"
        "Nick and Whitney named him [randBoy]! "
    else:
        scene bg girl
        $randGirl = renpy.random.choice(["Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia", "Abigail", "Emily", "Charlotte", "Harper", "Madison", "Amelia", "Elizabeth", "Sofia", "Evelyn", "Chloe", "Ella"])
        "           It's a girl!!!"
        "Nick and Whitney named her [randGirl]! "

    $cashFlowStatement.addItem("outflows", "child", "Cost of a Child", 13000)

    scene bg citysuburb
    with dissolve

    "Since Nick and Whitney now have a baby, they want to buy their very own house!"

    menu:
        "Where should they live? Most house purchases require 20\%\ down payment."
        "City: $400,000 - 15 year loan with a rate of 7.5\%\ Average $2,966 monthly mortgage payment":
            scene bg city
            "Congratulations! Nick and Whitney are city-slickers now!"
            $balanceSheet.removeItem("houseDownPay")
            $cashFlowStatement.removeItem("houseDownPay")
            $cashFlowStatement.addItem("outflows", "mortgagePayment", "House Mortgage", 35592)
            $balanceSheet.addItem("misLoans", "house", "House", 320000)
            $lifePoints += 120
        "Suburb: $200,000 - 15 year loan with a rate of 7.5\%\ Average $1,483 monthly mortgage payment": #Need escape character for a %, so \%\
            scene bg suburb
            "Congratulations! Nick and Whitney own a house in the suburbs now!"
            $balanceSheet.removeItem("houseDownPay")
            $cashFlowStatement.removeItem("houseDownPay")
            $cashFlowStatement.addItem("outflows", "mortgagePayment", "House Mortgage", 2966)
            $balanceSheet.addItem("misLoans", "house", "Home", 160000)
            $lifePoints += 85


jump theft
