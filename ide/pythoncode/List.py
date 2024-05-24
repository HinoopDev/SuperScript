from Variable import Variable

class Liste:
    liste = {}

    def assigne(lamList):
        lamList = lamList[2:]

        if "=>" in lamList: state = Liste.create(lamList)
        elif "&" in lamList: state = Liste.add(lamList)
        elif "~" in lamList: state = Liste.delete(lamList)
    
    def create(lamList):        #Keyword =>
        lamList = lamList.split("=>")
        ListName = lamList[1]
        if "-" in lamList[0]:
            lamVal   = lamList[0].split("-")
        else: lamVal = [lamList[0], ""]
        endVal   = []
        for Val in lamVal:
            if Val.startswith("§§"): endVal.append(Liste.liste[Val.strip("§§")])
            elif Val.startswith("§"):
                if "=>" in Val: endVal.append(Variable.whitchAssignement(Val.strip("§").split("=>")))
                else: endVal.append(Variable.variable[Val.strip("§")])
            else: endVal.append(Val)
        Liste.liste[ListName] = endVal

    def add(lamList):           #Keyword &
        lamList = lamList.split("&")
        if Liste.isList(lamList[0]):
            if lamList[1].startswith("§§"): print("ERROR: No lists in lists allowed.")
            elif lamList[1].startswith("§"):
                if "=>" in lamList[1]: Liste.liste[lamList[0]].append(Variable.whitchAssignement(lamList[1].strip("§").split("=>")))
                else: Liste.liste[lamList[0]].append(Variable.variable[lamList[1].strip("§")])
            else: Liste.liste[lamList[0]].append(lamList[1])
            return 0
        return -1

    def delete(lamList):        #Keyword ~
        lamList = lamList.split("~")
        if Liste.isList(lamList[0]):
            try:
                if lamList[1].startswith("§§"): print("ERROR: Ther can't be lists inside of lists")
                elif lamList[1].startswith("§"):
                    if "=>" in lamList[1]: Liste.liste[lamList[0]].remove(Variable.whitchAssignement(lamList[1].strip("§").split("=>")))
                    else: Liste.liste[lamList[0]].remove(Variable.variable[lamList[1].strip("§")])
                else: Liste.list[lamList[0]].remove(lamList[1])
            except ValueError:
                    print("ERROR: Item not in list")
            return 0
        return -1

    
    def destroy(ListName):
        ListName = ListName.strip("$§§")
        if Liste.isList(ListName):
            Liste.liste.pop(ListName)


    def isList(listName):
        if listName in Liste.liste:
            return True
        return False
    