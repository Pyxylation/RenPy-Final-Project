# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label dependent:

    # 5 years
    scene bg 5yearslater

    #salary increase
    #$cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(5, "salaryNick"))
    #$cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(5, "salaryWhit"))

    #display salary
    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')

    #new 401K calcualtion
    $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

    #calculate new federal tax based on income
    $fedTax()
    #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
    $ficaCalcAdd()

    $cashFlowStatement.removeItem("mortgagePayment")
    $houseValue = balanceSheet.getValue("house")
    $balanceSheet.addItem("assets", "house", "House", houseValue)

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 5, .03)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 5, .01)))

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
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*7)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
    $k401 = balanceSheet.getValue("401K")
    #Increases 401K deferal amount in cashFlowStatement. 3% of total salary
    $cashFlowStatement.changeItemValue('401K', int(cashFlowStatement.getValue("salaryNick")*.025))

    if nickIsCrazy == True:
        $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*5
        $matress = balanceSheet.getValue("matressBank")
        $location = "under his matress."
    else:
        $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*5
        $balanceSheet.incItemValue("savingsAcc", nickCashFlow)

        $savings = balanceSheet.getValue("savingsAcc")
        $location = "in his savings."


    scene bg yearslaterbar
    menu:
        "{size=-5}{b}{u}5 Years Later{/u}{/b}
        \n
        - Nick is now 60 years old and earns {c}[salaryNick]{/c}.
        \n- Whitney is now 59 years old and earns {c}[salaryWhit]{/c}. Her salary has maxed out at her current job.
        \n
        \n {u}Mortgage{/u}
        \n- Congradulations!!! Nick and Whitney have paid off their house!!!
        \n
        \n {u}Investments{/u}
        \n - Nick's K&B portfolio is [kBStatus] Valued at: {c}[kBShare]{/c} per share.
        \n Total value is {c}[kB]{/c}. That's is a {c}[kBStockGL]{/c} [kBGL]
        \n - Nick's FedEx portfolio is [fedExStatus] Valued at: {c}[fedExShare]{/c} per share.
        \n Total value is {c}[fedEx]{/c}. That's a {c}[fedExStockGL]{/c} [fedExGL]
        \n
        \n - Nick now has {c}[savings]{/c} [location]{/size}":
            jump dependentReal
        "{size=-5}Click Here to Continue{/size}":
            jump dependentReal


label dependentReal:

    scene bg brokenleg

    "Oh no! Nick's dad broke his leg and realizes that he is unable to take care of himself alone."
    $crazyBrokenLeg = False
    menu:
        "How should Nick help his dad?"
        "Pay monthly rent at a nursing home for dad, $5,500":
            $lifePoints += 20
            $cashFlowStatement.addItem("outflows", "nursing", "Nursing Home", 5500)
            "Nick's dad is grateful for his help in paying for a nursing home!
            \nNick will make sure to visit often!"

        "Hire in-home nurse so Nick's dad can still live at his home, $4,500":
            $lifePoints += 50
            $cashFlowStatement.addItem("outflows", "nurse", "In-Home Nurse", 4500)
            "Nick's dad is happy that he can continue to live at home and get the help he needs."

        "Whitney quits her job and takes care of Nick's dad at their house, $1,000":
            $lifePoints += 150
            $cashFlowStatement.addItem("outflows", "medication", "Nick's Dad Medication", 5500)
            $cashFlowStatement.changeItemValue("salaryWhit", 0)
            "Nick's dad is ecstatic that he can live and spend time with Nick and Whitney again!"

        "NICK DOESNT NEED THE COMPROMISED MEDICAL SYSTEM TO MAKE HIS DAD WORSE!
        \nNICK'S DAD MOVES IN WITH HIM AND NICK FIXES THE BROKEN BONE HIMSELF!" if nickIsCrazy:
            $lifePoints += 120

    #likelyhood that he loses money from identity being stolen
    $stolenRand = renpy.random.randint(0, 100)
    if nickIsCrazy == False and identityStolen == True and stolenRand <= 75:
        $stolenMultiplied = stolenRand * 1000
        $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc")-stolenMultiplied)
        "Oh no!!! You should have paid for Life Lock! You lost {c}[stolenMultiplied]{/c}."
    else:
        jump retirement






jump retirement
