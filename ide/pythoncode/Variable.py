class Variable:
    variable = {}
    
    def assigne(lamVar):
        lamVar = lamVar[1:]
        if "=>" in lamVar:
            lamVar = lamVar.split("=>")
            VarName = lamVar[1]
            VarValu = Variable.whitchAssignement(lamVar[0], VarName)
            Variable.variable[VarName] = VarValu


    def whitchAssignement(lamVar, VarName):
        if   "&" in lamVar: return Variable.add     (lamVar)
        elif "~" in lamVar: return Variable.subtract(lamVar)
        elif "@" in lamVar: return Variable.multiply(lamVar)
        elif "#" in lamVar: return Variable.divide  (lamVar)
        elif lamVar in Variable.variable: 
            lamVar = Variable.variable[lamVar]
        else: return lamVar

    def add(lamVar):            #Keywword &
        lamVar = lamVar.split("&")

        if Variable.allint(lamVar):
            return str(int(lamVar[0]) + int(lamVar[1]))
        elif Variable.inVariable1(lamVar):
            return str(int(Variable.variable[lamVar[0]]) + int(lamVar[1]))
        elif Variable.inVariable2(lamVar):
            return str(int(Variable.variable[lamVar[1]]) + int(lamVar[0]))
        elif Variable.bothVar(lamVar):
            return str(int(Variable.variable[lamVar[0]]) + int(Variable.variable[lamVar[1]]))
        return None

    def subtract(lamVar):            #Keywword ~
        lamVar = lamVar.split("~")

        if Variable.allint(lamVar):
            return str(int(lamVar[0]) - int(lamVar[1]))
        elif Variable.inVariable1(lamVar):
            return str(int(Variable.variable[lamVar[0]]) - int(lamVar[1]))
        elif Variable.inVariable2(lamVar):
            return str(int(lamVar[0]) - int(Variable.variable[lamVar[1]]))
        elif Variable.bothVar(lamVar):
            return str(int(Variable.variable[lamVar[0]]) - int(Variable.variable[lamVar[1]]))
        return None
        
    def multiply(lamVar):            #Keywword @
        lamVar = lamVar.split("@")

        if Variable.allint(lamVar):
            return str(int(lamVar[0]) * int(lamVar[1]))
        elif Variable.inVariable1(lamVar):
            return str(int(Variable.variable[lamVar[0]]) * int(lamVar[1]))
        elif Variable.inVariable2(lamVar):
            return str(int(Variable.variable[lamVar[1]]) * int(lamVar[0]))
        elif Variable.bothVar(lamVar):
            return str(int(Variable.variable[lamVar[0]]) * int(Variable.variable[lamVar[1]]))
        return None
        
    def divide(lamVar):            #Keywword #
        lamVar = lamVar.split("#")

        if Variable.allint(lamVar):
            return str(int(lamVar[0]) / int(lamVar[1]))
        elif Variable.inVariable1(lamVar):
            return str(int(Variable.variable[lamVar[0]]) / int(lamVar[1]))
        elif Variable.inVariable2(lamVar):
            return str(int(lamVar[0]) / int(Variable.variable[lamVar[1]]))
        elif Variable.bothVar(lamVar):
            return str(int(Variable.variable[lamVar[0]]) / int(Variable.variable[lamVar[1]]))
        return None
    

    def destroy(VarName):
        VarName = VarName.strip("$§")
        if VarName in Variable.variable:
            Variable.variable.pop(VarName)


    def inVariable1(VarNames):
        if VarNames[1].isnumeric() and VarNames[0] in Variable.variable:
            if Variable.variable[VarNames[0]]:
                return True
        return False
    def inVariable2(VarNames):
        if VarNames[0].isnumeric() and VarNames[1] in Variable.variable:
            if Variable.variable[VarNames[1]]:
                return True
        return False
    def bothVar(VarNames):
        if VarNames[0] in Variable.variable and VarNames[1] in Variable.variable:
            if Variable.variable[VarNames[0]] and Variable.variable[VarNames[1]]:
                return True
        return False
    def allint(VarNames):
        if VarNames[0].isnumeric() and VarNames[1].isnumeric():
            return True
        return False