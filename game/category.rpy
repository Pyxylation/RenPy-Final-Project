# Class for assets liabilities and balance sheet
# Also includes the setup of cashflow and balancesheet with inital values

init -2 python:
    cashflow = {}
    balancesheet = {}
    displayList = []

    class Category(object):
        """Represents a grouping of items and subcategories"""

        def __init__(self, catId, title, negative=False):
            self.catId = catId
            self.itemId = catId
            self.title = title
            self.negative = negative
            self.catList = []

        def addItem(self, parentId, itemId, title, value, userEdit=False):
            if self.catId == parentId:
                if isinstance(self, Category):
                    self.addSubItem(itemId, title, value, userEdit)
                    return True
            for item in self.catList:
                if item.itemId == parentId:
                    if isinstance(item, Category):
                        item.addSubItem(itemId, title, value, userEdit)
                elif isinstance(item, Category):
                    item.addItem(parentId, itemId, title, value, userEdit)
            return False

        def addSubItem(self, itemId, title, value, userEdit=False):
            self.catList.append(Item(itemId, title, value, userEdit))

        def addCategory(self, parentId, catId, title, negative=False):
            if self.catId == parentId:
                    if isinstance(self, Category):
                        self.addSubCategory(catId, title, negative)
            for item in self.catList:
                if item.itemId == parentId:
                    if isinstance(item, Category):
                        item.addSubCategory(catId, title, negative)
                elif isinstance(item, Category):
                    item.addCategory(parentId, catId, title, negative)
            return False

        def addSubCategory(self, catId, title, negative):
            self.catList.append(Category(catId, title, negative))

        def removeItem(self, catId):
            for index, item in enumerate(self.catList):
                if item.itemId == catId:
                    del self.catList[index]
                    return True
                elif isinstance(item, Category):
                    item.removeItem(catId)

            return False

        def incItemValue(self, itemId, value):
            self.returnValue = 0
            for item in self.catList:
                if item.itemId == itemId:
                    item.value += value
                    return item.value
                elif isinstance(item, Category):
                    self.returnValue = item.incItemValue(itemId, value)
                    if self.returnValue:
                        return self.returnValue

        def decItemValue(self, itemId, value):
            self.returnValue = 0
            for item in self.catList:
                if item.itemId == itemId:
                    item.value -= value
                    return item.value
                elif isinstance(item, Category):
                    self.returnValue = item.decItemValue(itemId, value)
                    if self.returnValue:
                        return self.returnValue
            #return "Item " + itemId + " not found."

        def changeItemValueOrig(self, itemId, value):
            for item in self.catList:
                if item.itemId == itemId:
                    item.value = value
                    return True
                elif isinstance(item, Category):
                    item.changeItemValue(itemId, value)

            return False

        def changeItemValue(self, itemId, value):
            self.item = self.findItem(itemId)
            if isinstance(self.item, Item):
                self.item.value = value
                return self.item.value
            return "Item " + itemId + " not found."

        def getValueItem(self, catId):
            self.returnValue = 0
            for item in self.catList:
                if item.itemId == catId:
                    return item.value
                elif isinstance(item, Category):
                    self.returnValue = item.getValueItem(catId)
                    if self.returnValue:
                        return self.returnValue

        def findItem(self, itemId):
            self.returnValue = 0
            for item in self.catList:
                if item.itemId == itemId:
                    return item
                elif isinstance(item, Category):
                    self.returnValue = item.findItem(itemId)
                    if self.returnValue:
                        return self.returnValue

        def getValue(self, catId):
            self.returnValue = None
            if (self.catId == catId):
                #this is the top level Category
                return self.tallyValue(self.negative)
            for item in self.catList:
                if item.itemId == catId:
                    if isinstance(item, Item):
                        return item.value
                    return item.tallyValue(item.negative)
                elif isinstance(item, Category):
                    self.returnValue = item.getValue(catId)
                    if self.returnValue is not None:
                        return self.returnValue

        def tallyValueOrig(self):
            self.itemTally = 0
            for item in self.catList:
                if isinstance(item, Category):
                    self.itemTally += item.tallyValue()
                elif isinstance(item, Item):
                    self.itemTally += item.value
            return self.itemTally

        def tallyValue(self, negative=False):
            self.itemTally = 0
            self.negative = negative
            for item in self.catList:
                if isinstance(item, Category):
                    self.itemTally += item.tallyValue(item.negative)
                elif isinstance(item, Item):
                    if self.negative:
                        self.itemTally += item.value*-1
                    else:
                        self.itemTally += item.value
            return self.itemTally

        def printCategory(self, level=0):
            self.itemTally = 0
            self.level = level + 1
            print(" "*self.level + self.title + " " + self.catId)
            for item in self.catList:
                if isinstance(item, Category):
                    self.itemTally += item.printCategory(self.level)
                    #print(" "*self.level + " " + self.title + ":     " + str(self.itemTally))
                elif isinstance(item, Item):
                    item.printItem(self.level)
                    self.itemTally += item.value
            print(" "*self.level + " " + self.title + ":     " + str(self.itemTally))
            return self.itemTally

        def genDisplayList(self, level=0):
            self.itemTally = 0
            self.level = level + 1
            displayList.append(displayItem(self.catId, "CategoryTitle", self.title, self.level, 0))
            for item in self.catList:
                if isinstance(item, Category):
                    self.itemTally += item.genDisplayList(self.level)
                elif isinstance(item, Item):
                    displayList.append(displayItem(item.itemId, "Item", item.title, self.level, item.value, item.userEdit))
                    self.itemTally += item.value
            displayList.append(displayItem(self.catId, "CategorySumary", self.title, self.level, self.itemTally))
            return self.itemTally

        def genDisplayList2(self, level=0, negative=False):
            self.itemTally = 0
            self.level = level + 1
            self.negative = negative
            displayList.append(displayItem(self.catId, "CategoryTitle", self.title, self.level, 0))
            for item in self.catList:
                if isinstance(item, Category):
                    self.itemTally += item.genDisplayList2(self.level, item.negative)
                elif isinstance(item, Item):
                    displayList.append(displayItem(item.itemId, "Item", item.title, self.level, item.value, item.userEdit))
                    if self.negative:
                        self.itemTally += item.value*-1
                    else:
                        self.itemTally += item.value
            displayList.append(displayItem(self.catId, "CategorySumary", self.title, self.level, self.talleyDisplay(self.itemTally)))
            return self.itemTally

        def talleyDisplay(self,tally):
            if tally < 0:
                return "(" + str(abs(tally)) + ")"
            else:
                return str(tally)

        def getDisplayList(self):
            """Generate a list of the Category structure for user display"""
            del displayList[:]
            self.genDisplayList2()
            return displayList

    class displayItem(object):
        """display list item for the Category structure for user display"""

        def __init__(self, itemId, kind, title, level, value, userEdit=False):
            self.itemId = itemId
            self.userEdit = userEdit
            self.kind = kind
            self.title = title
            self.level = level
            self.value = value

    class Item(object):
        """Represents a single line item with a value"""

        def __init__(self, itemId, title, value, userEdit=False):
            self.itemId = itemId
            self.title = title
            self.value = value
            self.userEdit = userEdit

        def printItem(self, level=0):
            print(" "*level + " " + self.title + " " + str(self.value))
