label loadCashflow:
    #top level Category Class, category id, title for display
    $cashFlowStatement = Category("cashflows", "STATEMENT OF CASHFLOWS")

    # Category Class params: parent category id, item id, title to display, if the category holds negative values like liabilities or outflows defaults to False
    $cashFlowStatement.addCategory("cashflows", "inflows", "CASH INFLOWS")
    # Item Class params: parent category id, item id, title to display, value, if user can edit value True/False (default value of False not required)
    $cashFlowStatement.addItem("inflows", "salaryNick", "Salary-Nicholas", 39000)
    $cashFlowStatement.addItem("inflows", "salaryWhit", "Salary-Whitney", 30000)
    $cashFlowStatement.addItem("inflows", "investIncome", "Investment Income", 1635)

    $cashFlowStatement.addCategory("cashflows", "outflows", "CASH OUTFLOWS", True)
    $cashFlowStatement.addCategory("outflows", "plannedSaving", "Planned Saving", True)
    $cashFlowStatement.addItem("plannedSaving", "intDiv", "Reinvested Int/Div", 1635)
    # This example shows using existing values to calculate the value. Nicks salary * 3% plush the $.50 match per dollar contributed
    $cashFlowStatement.addItem("plannedSaving", "401K", "401K Salary Deferrals", 1170)
    #cashFlowStatement.addItem("plannedSaving", "401k", "401K Salary Deferrals", eval('(cashFlowStatement.getValue("salaryNick")*.03)*.5+cashFlowStatement.getValue("salaryNick")*.03'), True)
    $cashFlowStatement.addItem("plannedSaving", "houseDownPay", "House Downpayment Saving", 1800)

    $cashFlowStatement.addItem("outflows", "childSup", "Child Support", 6000)
    $cashFlowStatement.addItem("outflows", "lifeIns", "Life Insurance Pmt to Trust", 2100)
    $cashFlowStatement.addItem("outflows", "rent", "Rent", 9900)
    $cashFlowStatement.addItem("outflows", "rentIns", "Rental Insurance", 720)
    $cashFlowStatement.addItem("outflows", "utilities", "Utilities", 2520)
    $cashFlowStatement.addItem("outflows", "ficaTax", "FICA Tax", 5279)
    $cashFlowStatement.addItem("outflows", "fedTax", "Fed Inc Tax Withholding", 7393)
    $cashFlowStatement.addItem("outflows", "autoLoan", "Auto Loan Payments", 5400)
    $cashFlowStatement.addItem("outflows", "autoIns", "Auto Insurance", 4950)
    $cashFlowStatement.addItem("outflows", "autoMaint", "Auto fuel/maintenance", 3600)
    $cashFlowStatement.addItem("outflows", "ccPayments", "Credit Card Payments", 8000)
    $cashFlowStatement.addItem("outflows", "studentLoan", "Student Loan Payments", 3600)
    $cashFlowStatement.addItem("outflows", "furnitureLoan", "Furniture Loan Payment", 1952)
    $cashFlowStatement.addItem("outflows", "entertainment", "Vacation/entertainment", 1920)
    $cashFlowStatement.addItem("outflows", "food", "Food", 4800)
    $cashFlowStatement.addItem("outflows", "personalCare", "Personal Care/Clothing", 1500)

    #Category Class access interface interface.

    #topLevelClassObject.getValue('itemId') get value of single item or a Category total/subtotal depending on itemId/categoryId.
    #topLevelClassObject.changeItemValue("itemId", int change value)
    #topLevelClassObject.decItemValue("itemId", int decrement value)
    #topLevelClassObject.incItemValue("itemId", int increment value)

    #$ generatedList = cashFlowStatement.getDisplayList() - displays Categories and Items hierachically with category subtotals and totals - see result in cash flow menu item

    #example interface usage from game/dialogs

    #$food = cashFlowStatement.getValue('food')

    #e "Your food budget is: $[food]."
    #$food = cashFlowStatement.changeItemValue("food", 2500)
    #$food = cashFlowStatement.getValue('food')
    #e "Your on a diet and your food savings is apparent, you're food budget is now: $[food]."

    #$rent = cashFlowStatement.getValue('rent')
    #e "Your current rent is: $[rent]."
    #$rent = cashFlowStatement.decItemValue("rent", 100)
    #$rent = cashFlowStatement.getValue('rent')
    #e "Congrats your rent has been lowered by $100, it is now: $[rent]."

    #$iflows = cashFlowStatement.getValue('inflows')
    #e "Your current inflows is: $[iflows]."
    #$oflows = cashFlowStatement.getValue('outflows')
    #e "Your current outflows is: $[oflows]."
    #$pSavings = abs(cashFlowStatement.getValue('plannedSaving'))
    #e "Your current planned savings is: $[pSavings]."
    #$cashFlowStatement.incItemValue("401k", 100)
    #$pSavings = abs(cashFlowStatement.getValue('plannedSaving'))
    #e "You got a raise and now can save $100 more in your 401k, your planned saving is now: $[pSavings]."

    #$cf = cashFlowStatement.getValue('cashflows')
