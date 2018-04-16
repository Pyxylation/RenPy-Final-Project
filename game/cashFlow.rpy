label cashFlowLabel:



    $ generatedList = cashFlowStatement.getDisplayList()

        #for i in generatedList:
        #    print (i.itemId, i.userEdit, i.kind, i.title, i.value, i.level)

    call screen cashflowScreen(adj=tutorials_adjustment)

    $ cashFlowItem = _return
    if not cashFlowItem:
        jump exitCashFlow

    if type(cashFlowItem) == bool:
        jump exitCashFlow
    #If(type(tutorial) == bool, return)
    #if not tutorial:
    #    jump exitCashFlow
    #python:
    #    if type(tutorial) == bool:
    #            Return()
    call screen input(cashFlowItem)
    $ x = _return
    #If(type(x) == bool, return)
    #$if not x:
    #   jump exitCashFlow
    #python:
        #if type(x) == bool:
        #    Return()
        #tutorial.value = x
        #cash_flow_statement[tutorial.label] = tutorial.value
        #cashFlowItem.value = x
    $pReturnValue = cashFlowStatement.changeItemValue(cashFlowItem.itemId, int(_return))
    jump cashFlowLabel

label exitCashFlow:
    return

screen input(cashFlowItem):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox

        text cashFlowItem.title style "input_prompt"
        #input id "inputResult" style "input_text" default cashFlowItem.value
        input style "input_text" default cashFlowItem.value

screen cashflowScreen(adj):

    #tag menu

    #use game_menu(_("Cash Flow Statement"), scroll="viewport"):
    modal True

    zorder 200

    frame:
        xsize 1440
        xalign .5
        ysize 850
        yalign .5
        #ypos 0

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:

                for i in generatedList:
                    if i.kind == "CategoryTitle":
                        text i.title :
                            if i.level == 1:
                                first_indent 10
                            elif i.level == 2:
                                first_indent 30
                            elif i.level == 3:
                                first_indent 50
                            xfill True

                    if i.kind == "CategorySumary":
                        fixed:
                            yfit True
                            text "Total " + i.title:
                                if i.level == 1:
                                    first_indent 50
                                elif i.level == 2:
                                    first_indent 70
                                elif i.level == 3:
                                    first_indent 90
                            text str(i.value):
                                xalign 1.0
                    if i.kind == "Item" and i.userEdit == False:
                        text i.title + ": " + str(i.value):
                            if i.level == 1:
                                first_indent 30
                            elif i.level == 2:
                                first_indent 50
                            elif i.level == 3:
                                first_indent 70
                    if i.kind == "Item" and i.userEdit:
                        textbutton i.title + ": " + str(i.value):
                            action Return(i)
                            if i.level == 1:
                                left_padding 30
                            elif i.level == 2:
                                left_padding 50
                            elif i.level == 3:
                                left_padding 70
                            xfill True
                    #else:
                    #   null height 10
                    #    text i.title + " else: " + i.kind alt ""
                    #    null height 5




        bar adjustment adj style "vscrollbar"

        textbutton _("Return to Simulation"):
            xfill True
            action Return(False)
            top_margin 10

# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()
