#Right now: No editing be players, because this will be populated from the cashflow statement
#We just change both cash flow AND balance sheet at the same time!
label loadBalanceSheet:
    #top level Category Class, category id, title for display
    $balanceSheet = Category("balanceSheet", "Balance Sheet")

    # Category Class params: parent category id, item id, title to display, if the category holds negative values like liabilities or outflows defaults to False
    $balanceSheet.addCategory("balanceSheet", "assets", "ASSETS")
    # Item Class params: parent category id, item id, title to display, value, if user can edit value True/False (default value of False not required)
    $balanceSheet.addItem("assets", "checkingAcc", "Checking Account", 500)
    $balanceSheet.addItem("assets", "savingsAcc", "Savings Account", 1000)

    #Investments/Savings Category in Assets category
    $balanceSheet.addCategory("assets", "invest/Save", "Investments/Savings")
    #Investments/Savings items
    $balanceSheet.addItem("invest/Save", "fedExStock", "FedEx Stock - 100 Shrs", 5000)
    $balanceSheet.addItem("invest/Save", "k&bStock", "K&B - 100 Shrs", 7200)
    $balanceSheet.addItem("invest/Save", "growthMutualFund", "Growth Mutual Fund", 13900)
    $balanceSheet.addItem("invest/Save", "401k", "401K Retirement Plan", 1500)

    #Automobiles Category in Assets category
    $balanceSheet.addCategory("assets", "automobiles", "Automobiles")
    #Automobiles item
    $balanceSheet.addItem("automobiles", "autoWhitney", "Auto - Whitney", 26474)
    $balanceSheet.addItem("automobiles", "truckNick", "Truck - Nick", 4000)
    $balanceSheet.addItem("automobiles", "motorcycleWhitney", "Motorcycle - Whitney", 1000)

    #this item is just like checking account or savings account, needs to be here for the order
    $balanceSheet.addItem("assets", "personalUseAssets", "Personal Use Assets", 17750)

    #New category, True because they need to be NEGATIVE
    $balanceSheet.addCategory("balanceSheet", "liabilities", "LIABILITIES", True)
    #Credit Card category in liabilities category, true because they need to be negative
    $balanceSheet.addCategory("liabilities", "creditCard", "Credit Card", True)
    #new items under credit Card
    $balanceSheet.addItem("creditCard", "americanExpress", "American Express", 8000)
    $balanceSheet.addItem("creditCard", "discover", "Discover", 1862)

    #Student loans in liabilities, True = NEGATIVE
    $balanceSheet.addCategory("liabilities", "studentLoans", "Student Loans", True)
    #new item under student Loans
    $balanceSheet.addItem("studentLoans", "nicholasLoan", "Nicholas (Parents own)", 45061)

    #Miscellaneous loans in liabilities, True = NEGATIVE
    $balanceSheet.addCategory("liabilities", "misLoans", "Miscellaneous Loans", True)
    #item under Miscellaneous Loans
    $balanceSheet.addItem("misLoans", "autoLoan", "Auto Loan", 8500)
    $balanceSheet.addItem("misLoans", "furnitureLoan", "Furniture Loan", 2300)














    $balanceSheet.addItem("inflows", "investIncome", "Investment Income", 1635)

    $balanceSheet.addCategory("cashflows", "outflows", "CASH OUTFLOWS", True)
    $balanceSheet.addCategory("outflows", "plannedSaving", "Planned Saving", True)
    $balanceSheet.addItem("plannedSaving", "intDiv", "Reinvested Int/Div", 1635)
    # This example shows using existing values to calculate the value. Nicks salary * 3% plush the $.50 match per dollar contributed
    $balanceSheet.addItem("plannedSaving", "401k", "401K Salary Deferrals", 1775, True)
    #balanceSheet.addItem("plannedSaving", "401k", "401K Salary Deferrals", eval('(balanceSheet.getValue("salaryNick")*.03)*.5+balanceSheet.getValue("salaryNick")*.03'), True)
    $balanceSheet.addItem("plannedSaving", "houseDownPay", "House Downpayment Saving", 1800)

    $balanceSheet.addItem("outflows", "childSup", "Child Support", 6000)
    $balanceSheet.addItem("outflows", "lifeIns", "Life Insurance Pmt to Trust", 2100)
    $balanceSheet.addItem("outflows", "rent", "Rent", 9900, True)
    $balanceSheet.addItem("outflows", "rentIns", "Rental Insurance", 720)
    $balanceSheet.addItem("outflows", "utilities", "Utilities", 2520)
    $balanceSheet.addItem("outflows", "ficaTax", "FICA Tax", 5279)
    $balanceSheet.addItem("outflows", "fedTax", "Fed Inc Tax Withholding", 7393)
    $balanceSheet.addItem("outflows", "autoLoan", "Auto Loan Payments", 5400)
    $balanceSheet.addItem("outflows", "autoIns", "Auto Insurance", 4950)
    $balanceSheet.addItem("outflows", "autoMaint", "Auto fuel/maintenance", 3600)
    $balanceSheet.addItem("outflows", "ccPayments", "Credit Card Payments", 4500)
    $balanceSheet.addItem("outflows", "studentLoan", "Student Loan Payments", 3600)
    $balanceSheet.addItem("outflows", "entertainment", "Vacation/entertainment", 1920, True)
    $balanceSheet.addItem("outflows", "furnitureLoan", "Furniture Loan Payment", 1952)
    $balanceSheet.addItem("outflows", "food", "Food", 4800)
    $balanceSheet.addItem("outflows", "personalCare", "Personal Care/Clothing", 1500, True)

    #Category Class access interface interface.

    #topLevelClassObject.getValue('itemId') get value of single item or a Category total/subtotal depending on itemId/categoryId.
    #topLevelClassObject.changeItemValue("itemId", int change value)
    #topLevelClassObject.decItemValue("itemId", int decrement value)
    #topLevelClassObject.incItemValue("itemId", int increment value)

    #$ generatedList = balanceSheet.getDisplayList() - displays Categories and Items hierachically with category subtotals and totals - see result in cash flow menu item

    #example interface usage from game/dialogs

    #$food = balanceSheet.getValue('food')

    #e "Your food budget is: $[food]."
    #$food = balanceSheet.changeItemValue("food", 2500)
    #$food = balanceSheet.getValue('food')
    #e "Your on a diet and your food savings is apparent, you're food budget is now: $[food]."

    #$rent = balanceSheet.getValue('rent')
    #e "Your current rent is: $[rent]."
    #$rent = balanceSheet.decItemValue("rent", 100)
    #$rent = balanceSheet.getValue('rent')
    #e "Congrats your rent has been lowered by $100, it is now: $[rent]."

    #$iflows = balanceSheet.getValue('inflows')
    #e "Your current inflows is: $[iflows]."
    #$oflows = balanceSheet.getValue('outflows')
    #e "Your current outflows is: $[oflows]."
    #$pSavings = abs(balanceSheet.getValue('plannedSaving'))
    #e "Your current planned savings is: $[pSavings]."
    #$balanceSheet.incItemValue("401k", 100)
    #$pSavings = abs(balanceSheet.getValue('plannedSaving'))
    #e "You got a raise and now can save $100 more in your 401k, your planned saving is now: $[pSavings]."

    #$cf = balanceSheet.getValue('cashflows')
