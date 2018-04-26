# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# This is 2 years after the investment right now, we can always change it
label evicted:

    scene bg 8yearslater
    " "
    # scene bg timesChange
    # 8 years
    #salary increase
    $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(8, "salaryNick"))
    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(8, "salaryWhit"))

    $salaryNick = cashFlowStatement.getValue('salaryNick')
    $salaryWhit = cashFlowStatement.getValue('salaryWhit')

    #401K calcualtion
    $cashFlowStatement.changeItemValue("401K", int(eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03')))

    #calculate new federal tax based on income
    $fedTax()
    #FICA tax, Social security = 6.2% and Medicare is 1.45%, flat tax under 200K, over adds .9% to Medicare
    $ficaCalcAdd()

    #Student loan payments
    $balanceSheet.changeItemValue("nicholasLoan", int((balanceSheet.getValue("nicholasLoan") - (cashFlowStatement.getValue("studentLoan"))*8)))
    $loan = balanceSheet.getValue("nicholasLoan")

    #Auto loans
    $balanceSheet.changeItemValue("autoLoan", 0)
    $cashFlowStatement.changeItemValue("autoLoan", 0)
    #it only took 1.5 years to pay off the car... So, that extra 5.4K needs to be given back. 7.5*5.4K
    $balanceSheet.changeItemValue("savingsAcc", int((balanceSheet.getValue("savingsAcc"))+(5400*7.5)))
    #furnature loans
    $balanceSheet.changeItemValue("savingsAcc", int((balanceSheet.getValue("savingsAcc"))+(2300*7.5)))
    $cashFlowStatement.changeItemValue("furnitureLoan", 0)
    $balanceSheet.changeItemValue("furnitureLoan", 0)

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 8, .025)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 8, .01)))

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
    $kB = "nothing"
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
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*8)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
    $k401 = balanceSheet.getValue("401K")
    #Increases 401K deferal amount in cashFlowStatement. 3% of total salary
    $cashFlowStatement.changeItemValue('401K', int(cashFlowStatement.getValue("salaryNick")*.025))

    #How much money is saved for a house
    $housePayment = cashFlowStatement.getValue("houseDownPay")
    $eightHousePay = (housePayment*8)
    $balanceSheet.changeItemValue("houseDownPay", eightHousePay)

    #Now total revenue, dont include stuff taken out for savings, and make sure to take out all the money spent.
    $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*8
    $balanceSheet.incItemValue("savingsAcc", nickCashFlow)
    $savings = balanceSheet.getValue("savingsAcc")


    scene bg yearslaterbar
    menu:
        "{size=-5}{b}{u}8 Years Later{/u}{/b}
        \n
        - Nick is now 33 years old and earns {c}[salaryNick]{/c}.
        \nWhitney is now 32 years old and earns {c}[salaryWhit]{/c}.
        \n
        \n {u}Loans{/u}
        \n
        - Nick still has {c}[loan]{/c} of student loans to pay off.
        \n- Auto loans have been paid off!
        \n- Congratulations! Nick's furniture loan has also been paid off!
        \nNot sure why he wanted it in the first place...
        \n
        \n {u}Investments{/u}
        \n - Nick's K&B portfolio is [kBStatus] Valued at: {c}[kBShare]{/c} per share.
        \n Total value is {c}[kB]{/c}. That's a {c}[kBStockGL]{/c} [kBGL]
        \n - Nick's FedEx portfolio is [fedExStatus] Valued at: {c}[fedExShare]{/c} per share.
        \n Total value is {c}[fedEx]{/c}. That's a {c}[fedExStockGL]{/c} [fedExGL]
        \n
        \n Nick now has {c}[savings]{/c} in his savings.{/size}":
            jump evictedReal
        "{size=-5}Click Here to Continue{/size}":
            jump evictedReal




label evictedReal:

    scene bg evicted
    with dissolve
    define l = Character("Landlord")

    l "Ayyyy! Nick!!! Get outta here!!!!!"

    "Oh no! Nick's Turkish landlord is tired of Nick forgetting to pay his rent,
        and his second cousin twice removed is visiting. He wants to give that cousin a place to stay."
    "Because Nick made the mistake of becoming a 'tenant at will,' he has no lease and will need to find a new place to live."


    menu:

        "Nick and Whitney need to find a place to live pronto, before his landlord goes crazy and throws away all their stuff.
            \nWhat should they do?"

        "Move in with Whitney's brother. It's free and fun to hang out with her brother again! But, only for a bit until Nick can find another place to stay.":
            "Nick and Whitney had a blast spending time with her brother again! They're both glad they decided to live together again for a bit."
            $cashFlowStatement.changeItemValue("rent", 11500)
            $lifePoints += 100

        "Find temporary housing, expensive, and Nick will be a tenant at will again.
             \nBut, it may be a fun thing to do until he finds another place for a few months and they find a great new place to live.
             \n$2,500 per month":
            $randMonth = renpy.random.randint(2, 4)
            $savings = balanceSheet.getValue("savingsAcc")
            $balanceSheet.changeItemValue("savingsAcc", (savings - (randMonth*2500)))
            $cashFlowStatement.changeItemValue("rent", 12000)
            #dont forget to google about security deposits
            $lifePoints += 80

            "Nick and Whitney had a lot of fun changing things up and living in a cool temporary apartment!
            \nIt helped their marriage become stronger."

        "Immediately find a new apartment for $1,200 a month. This will be more expensive because rent locally has increased.":
            "Congratulations! Nick found an apartment and has a proper contract with the landlord!
            \nHe's glad he won't randomly get kicked out again."
            $cashFlowStatement.changeItemValue("rent", 14400)
            #dont forget to google security deposits
            $lifePoints += 20

    #remove stuff that has been paid off, but doing it down here so people can still see it throughout the scenario
    $balanceSheet.removeItem("autoLoan")
    $cashFlowStatement.removeItem("autoLoan")
    $balanceSheet.removeItem("furnitureLoan")
    $cashFlowStatement.removeItem("furnitureLoan")



jump passing
