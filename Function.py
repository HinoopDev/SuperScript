from Variable import Variable
from List import Liste


class Function:
    conditions = 0
    inCondition = False
    def give_out(togive):
        togive = togive.strip(">>>")
        if togive.startswith("§§"):
            togive = Function.giveList(togive)
        elif togive.startswith("§"):
            togive = Function.giveVar(togive)
        print(togive)

    def giveVar(togive):
        togive = togive.strip("§")
        if "=>" in togive: 
            togive = Variable.whitchAssignement(togive.split("=>"))
        else: togive = Variable.variable[togive]
        return togive
    
    def giveList(togive):
        togive = togive.strip("§§")
        if togive in Liste.liste: return Liste.liste[togive]

    
    def startCondition(tocondition):
        Function.conditions += 1
        tocondition = tocondition[1:]
        tocondition = tocondition.split("'")
        condition = tocondition[0]
        toInterpret = tocondition[1:]
        while Function.isCondition(condition):
            Function.inCondition = True
            Function.interpret(toInterpret)
        else: Function.inCondition = False
    
    def isCondition(condition):
        if "&&" in condition:
            condition = condition.split("&&")
            if condition[0].startswith("§§"):
                condition[0] = Liste.liste[condition[0]]
            elif condition[0].startswith("§"):
                if "=>" in condition[0]:
                    condition[0] = Variable.whitchAssignement(condition[0].strip("§").split("=>"))
                else: 
                    if condition[0].strip("§") in Variable.variable: condition[0] = Variable.variable[condition[0].strip("§")]

            if condition[1].startswith("§§"):
                condition[1] = Liste.liste[condition[1]]
            elif condition[1].startswith("§"):
                if "=>" in condition[1]:
                    condition[1] = Variable.whitchAssignement(condition[1].strip("§").split("=>"))
                else: 
                    if condition[1].strip("§") in Variable.variable: condition[1] = Variable.variable[condition[1].strip("§")]
            return condition[0] == condition[1]

        if "~~" in condition:
            condition = condition.split("~~")
            if condition[0].startswith("§§"):
                condition[0] = Liste.liste[condition[0]]
            elif condition[0].startswith("§"):
                if "=>" in condition[0]:
                    condition[0] = Variable.whitchAssignement(condition[0].strip("§").split("=>"))
                else: 
                    if condition[0].strip("§") in Variable.variable: condition[0] = Variable.variable[condition[0].strip("§")]

            if condition[1].startswith("§§"):
                condition[1] = Liste.liste[condition[1]]
            elif condition[1].startswith("§"):
                if "=>" in condition[1]:
                    condition[1] = Variable.whitchAssignement(condition[1].strip("§").split("=>"))
                else: 
                    if condition[1].strip("§") in Variable.variable: condition[1] = Variable.variable[condition[1].strip("§")]
            return condition[0] != condition[1]

        if "!!" in condition:
            condition = condition.split("!!")
            if condition[0].startswith("§§"):
                condition[0] = Liste.liste[condition[0]]
            elif condition[0].startswith("§"):
                if "=>" in condition[0]:
                    condition[0] = Variable.whitchAssignement(condition[0].strip("§").split("=>"))
                else: 
                    if condition[0].strip("§") in Variable.variable: condition[0] = Variable.variable[condition[0].strip("§")]

            if condition[1].startswith("§§"):
                condition[1] = Liste.liste[condition[1]]
            elif condition[1].startswith("§"):
                if "=>" in condition[1]:
                    condition[1] = Variable.whitchAssignement(condition[1].strip("§").split("=>"))
                else: 
                    if condition[1].strip("§") in Variable.variable: condition[1] = Variable.variable[condition[1].strip("§")]
            return int(condition[0]) < int(condition[1])

        if "^^" in condition:
            condition = condition.split("^^")
            if condition[0].startswith("§§"):
                condition[0] = Liste.liste[condition[0]]
            elif condition[0].startswith("§"):
                if "=>" in condition[0]:
                    condition[0] = Variable.whitchAssignement(condition[0].strip("§").split("=>"))
                else: 
                    if condition[0].strip("§") in Variable.variable: condition[0] = Variable.variable[condition[0].strip("§")]

            if condition[1].startswith("§§"):
                condition[1] = Liste.liste[condition[1]]
            elif condition[1].startswith("§"):
                if "=>" in condition[1]:
                    condition[1] = Variable.whitchAssignement(condition[1].strip("§").split("=>"))
                else: 
                    if condition[1].strip("§") in Variable.variable: condition[1] = Variable.variable[condition[1].strip("§")]
            return int(condition[0]) > int(condition[1])
        return False

    def endCondition():
        if not Function.inCondition:
            Function.conditions -= 1

    def interpret(tointerpret:list):
        for line in tointerpret:
            if line.startswith("§§"):    Liste.assigne(line)
            elif line.startswith("§"):   Variable.assigne(line)
            elif line.startswith("$§§"): Liste.destroy(line)
            elif line.startswith("$§"):  Variable.destroy(line)
            elif line.startswith(">>>"): Function.give_out(line)
            elif line.startswith("?"):   print("ERROR: Condition in conditions in not allowed.")
            elif line.startswith("$?"):  Function.endCondition()