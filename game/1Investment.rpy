# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Nicks friend who is asking himm to invest in the company
define b = Character("Bob")

# The game starts here.
label Investment:

    scene bg shakinghands

    b "Hi Nick! I'm starting a new data analystics company called 'Really Big Data.' We have this new take on data
        analysis and I was wondering if you wanted to be a investor?"
    n "That sounds interesting! Let me think about it..."

    menu:
        "Nick doesnt directly have $10,000 to give.
            \n How will he invest in Really Big Data?"

        "Invest: $10,000
            \n Nick gives 1000 from savings. While Whitney sells her car and purchases a different car freeing up the needed 9,000.
                    Nick also helps the company. Remember risk can equal reward!":
                n "I would love it! Here is $10,000. Lets talk marketing stragety."

                    # 3 things define life points 1) Risk for positive change 2) Fun things 3) Stuff that strengthens the family
                $lifePoints += 80

                $balanceSheet.changeItemValue("autoWhitney", 12474)
                $balanceSheet.changeItemValue("autoLoan", 3500)
                $balanceSheet.addItem("invest/Save", "RBD", "Really Big Data Investment", 10000) #RBD = Really Big Data
                $balanceSheet.changeItemValue("savingsAcc", .01)

                #random number to determine if nick gets the job or not
                $randJobNum = renpy.random.random()
                #becase nick helped with the company, so there is a greater chance for this success
                $adjustedRandJobNum = randJobNum + .15

                "Whittney sold her car for $26,474.
                    \n She gave $9,000 for the investment, used 5000 to pay off her
                    \n She also used the other $5,000 to pay off the last year of her car loan.
                    \n She then purchased a car worth about $12,646."


        "Invest $1,000":

            $balanceSheet.addItem("invest/Save", "RBD", "Really Big Data Investment", 1000) #RBD = Really Big Data
            $balanceSheet.changeItemValue("savingsAcc", .01)
            "I'd love to invest! I can't wait to see how things go!"

        "Dont invest.":
            "Sorry Bob. I really dont have the cash flow to invest.
                \n But, thanks for the offer."



jump evicted
