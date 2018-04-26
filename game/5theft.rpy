# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.
label theft:

    # 10 years
    scene bg 10yearslater
    " "
    #salary increase
    # $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(10, "salaryNick")) Nick job capped
    # $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(10, "salaryWhit")) Whitney Capped also

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
    $balanceSheet.changeItemValue("nicholasLoan", int((balanceSheet.getValue("nicholasLoan") - (cashFlowStatement.getValue("studentLoan"))*10)))
    $loan = abs(balanceSheet.getValue("nicholasLoan"))
    $balanceSheet.changeItemValue("nicholasLoan", 0)
    $balanceSheet.changeItemValue("savingsAcc", balanceSheet.getValue("savingsAcc") + loan)

    #Mortgage payment
    $housePay = cashFlowStatement.getValue("mortgagePayment")*5

    #change stuff for 3% inflation, only food and fun!
    #Entertianment
    $cashFlowStatement.changeItemValue("entertainment", int(compInt((cashFlowStatement.getValue("entertainment")), 10, .025)))
    #food
    $cashFlowStatement.changeItemValue("food", int(compInt((cashFlowStatement.getValue("food")), 10, .01)))

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
    $balanceSheet.changeItemValue("401K", (cashFlowStatement.getValue("401K")*10)+ (cashFlowStatement.getValue("401K")*4) + balanceSheet.getValue("401K"))
    $k401 = balanceSheet.getValue("401K")
    #Increases 401K deferal amount in cashFlowStatement. 3% of total salary
    $cashFlowStatement.changeItemValue('401K', int(cashFlowStatement.getValue("salaryNick")*.025))

    $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*7
    $balanceSheet.incItemValue("savingsAcc", nickCashFlow)

    $savings = balanceSheet.getValue("savingsAcc")


    scene bg yearslaterbar
    menu:
        "{size=-5}{b}{u}10 Years Later{/u}{/b}
        \n
        - Nick is now 55 years old and earns {c}[salaryNick]{/c}.
        \n- Whitney is now 54 years old and earns {c}[salaryWhit]{/c}. Her salary has maxed out at her current job.
        \n
        \n {u}Loan{/u}
        \n- Nick has paid off his student loans!!!
        \n
        \n {u}Mortgage{/u}
        \n- Nick nad Whitney still have {c}[housePay]{/c} of their mortgage to pay off.
        \n
        \n {u}Investments{/u}
        \n - Nick's K&B portfolio is [kBStatus] Valued at: {c}[kBShare]{/c} per share.
        \n Total value is {c}[kB]{/c}. That's is a {c}[kBStockGL]{/c} [kBGL]
        \n - Nick's FedEx portfolio is [fedExStatus] Valued at: {c}[fedExShare]{/c} per share.
        \n Total value is {c}[fedEx]{/c}. That's a {c}[fedExStockGL]{/c} [fedExGL]
        \n
        \n - Nick now has {c}[savings]{/c} in his savings.{/size}":
            jump theftReal
        "{size=-5}Click Here to Continue{/size}":
            jump theftReal

label theftReal:


    $randJobNum = 70
    # Nick may get a job at Really Big Data!
    if randJobNum >= 65 and nick10K == True:
        scene bg deskjob
        w "Hi Nick! Thanks to your help and investment in Really Big Data, we have been doing really well."
        w "Our CMO just left. I was wondering if you wanted the job."
        n "I'd love it! Thank you very much!"
        "Nicks investment finally paid off. His new salary is $110,000"
        $cashFlowStatement.changeItemValue("salaryNick", 110000)

    #Nick investing and that paying off
    elif randJobNum >= 65 and nick1K == True:
        scene bg deskwill #This is the normal desk with wills name on it, not nicks!!!
        w "We are happy to report that Really Big Data is doing well!"
        w "You can finally get a return on your investment!"
        $roiRBD = renpy.random.randint(10, 15)*1000
        $balanceSheet.incItemValue("savingsAcc", roiRBD)
        "Really Big Data gives you {c}[roiRBD]{/c}"


    #Nick not investing and that paying off, but you dont get anything
    elif randJobNum >=65 and nick10K == False and nick1K == False:
        scene bg deskwill #This is the normal desk with wills name on it, not nicks!!!
        "You didn't invest, but the company is rockin'"

    #The company failing regardless
    else:
        "Really Big Data has just gone bankrupt!"
        "Nick's investment had potential, but it wasn't enough to keep them afloat.
            \n Seems that the new data analytics was not needed in the market. "
        $balanceSheet.removeItem("RBD")

    # scene bg identityTheft

    scene bg identitytheft

    "Equifax has had yet ANOTHER data breach! Whitney told Nick not
        to trust them with their personal data."
    #gotta define these before, or else other menu/if statements that use them will crap out because they doesnt exist
    $nickIsCrazy = False
    $identityStolen = False
    menu:
        "What should Nick do about this?"

        "Purchase LifeLock for $15 a month":
            "Excellent choice! Nick feels safe now! He should be fine."
            $lifePoints += 80
            $cashFlowStatement.addItem("outflows", "lifeLock", "LifeLock", 180)


        "Risk it! Because how bad could it really be? These things happen to everyone, right?":
            $lifePoints += 20
            $identityStolen = True

        "TAKE OUT ALL SAVINGS FROM THE BANK AND STORE IT UNDER HIS MATRESS!!!!!":
            $balanceSheet.addItem("assets", "matressBank", "Money Under Matress", 0)
            $lifePoints += 100
            $nickIsCrazy = True
            $matressBank = balanceSheet.getValue("checkingAcc")
            $balanceSheet.changeItemValue("checkingAcc", 0)
            $matressBank += balanceSheet.getValue("savingsAcc")
            $balanceSheet.changeItemValue("savingsAcc", 0)
            $balanceSheet.changeItemValue("matressBank", matressBank)
            "Nick withdraws all the money from his bank account. He decides not to liquidize his assets quite yet."
            "Amount of money under matress: {c}[matressBank]{/c}"

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
