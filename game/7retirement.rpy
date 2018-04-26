# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label retirement:

    #5 years
    scene bg 5yearslater
    ""

    if nickIsCrazy == False:
        #salary increase
    #    $cashFlowStatement.changeItemValue("salaryNick", salaryIncrease(5, "salaryNick"))
    #    $cashFlowStatement.changeItemValue("salaryWhit", salaryIncrease(5, "salaryWhit"))

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



        $nickCashFlow = (cashFlowStatement.getValue("cashflows"))*5
        $balanceSheet.incItemValue("savingsAcc", nickCashFlow)
        $savings = balanceSheet.getValue("savingsAcc")

        scene bg yearslaterbar
        menu:
            "{size=-5}{b}{u}5 Years Later{/u}{/b}
            \n
            - Nick is now 65 years old and earns {c}[salaryNick]{/c}.
            \n- Whitney is now 64 years old and earns {c}[salaryWhit]{/c}. Her salary has maxed out at her current job.
            \n
            \n {u}Investments{/u}
            \n - Nick's K&B portfolio is [kBStatus] Valued at: {c}[kBShare]{/c} per share.
            \n Total value is {c}[kB]{/c}. That's is a {c}[kBStockGL]{/c} [kBGL]
            \n - Nick's FedEx portfolio is [fedExStatus] Valued at: {c}[fedExShare]{/c} per share.
            \n Total value is {c}[fedEx]{/c}. That's a {c}[fedExStockGL]{/c} [fedExGL]
            \n
            \n - Nick now has {c}[savings]{/c} in his savings. {/size}":
                jump retirementReal
            "{size=-5}Click Here to Continue{/size}":
                jump retirementReal

    else:
        "Nick is crazy. He doesn't trust the system and quits his job. So, he can't get paid."


label retirementReal:


    if nickIsCrazy == True:
        $money = balanceSheet.getValue("matressBank") + balanceSheet.getValue("fedExStock")
        $money += (balanceSheet.getValue("k&bStock") + balanceSheet.getValue("401K"))
    else:
        $money = (balanceSheet.getValue("checkingAcc") + balanceSheet.getValue("savingsAcc") + balanceSheet.getValue("fedExStock"))
        $money += (balanceSheet.getValue("k&bStock") + balanceSheet.getValue("401K"))

    "Congratulations!!! It's retirement time!!!"
    menu:
        "Let's see how money and life points Nick has!
        \n
        \n Life Points: [lifePoints]
        \n Total Money: {c}[money]{/c}":
            jump restofretirement
        "Click Here to Continue":
            jump restofretirement

label restofretirement:

    if money >= 1000000:

        if nickIsCrazy == True:
            scene bg mountians
            $credits = "mountians"
            "NICK RETIRES TO THE MOUNTAINS!!! THE GOVERNMENT IS OUT TO GET NICK! CIVILIZATION AND TECHNOLOGY HAS NOTHING FOR HIM!!!"

        else:
            if lifePoints <=120:
                scene bg beach
                $credits = "beach"
                "Nick made it to retirement! But, he got depression in the process..."

            else:
                scene bg beach
                $credits = "beach"
                "Congrats! Beach Retirement!"


    elif nickIsCrazy == True and money < 1000000:
        scene bg gameover
        $credits = "fail"
        "Nick went crazy and didn't make it to retirement... "


    else:
        scene bg gameover
        $credits = "fail"
        "Sorry... You didn't make it to 1 million..."


    if credits == "mountians":
        scene bg mountiancredits
        " "
    elif credits == "beach":
        scene bg beachcredits
        " "
    else:
        scene bg failcredits
        " "

#ends game
return
