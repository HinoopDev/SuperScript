from List import Liste
from Variable import Variable
from Function import Function

class Lencer:
    KEY_WORDS = ["§§", "$§§", "§", "$§", ">>>", "?", "$?"]
    METHODES  = ["&", "~", "@", "#", "=>"]
    CONDITION = ["&&", "~~", "!!", "^^"]
    output = ""
    def prep(contentraw, window):
        content = []
        if "Â" in contentraw:
            for char in contentraw:
                if char == "Â": char = ""
                content.append(char)
            content = "".join(content)
        else: content = contentraw
        content=content.replace("|", "\n").split("\n")
        return Lencer.main(content, window)
    
    def reset():
        Function.conditions = 0
        Liste.liste = {}
        Variable.variable = {}

    def main(content, window):
        output = "Run over\n\n\n"
        index = 0
        for line in content:
            print(line)
            index += 1
            if line == ""              : continue
            elif line.startswith("§§") : Liste.assigne(line)
            elif line.startswith("$§§"): Liste.destroy(line)
            elif line.startswith("§")  : Variable.assigne(line)
            elif line.startswith("$§") : Variable.destroy(line) 
            elif line.startswith(">>>"): Function.give_out(line, window)
            elif line.startswith("?")  : Function.startCondition(line, window)
            elif line.startswith("$?") : Function.endCondition()

        if Function.output     != "": output = Function.output
        if Function.conditions != 0 : output = "ERROR: Not all conditions are ended.\n"
        if Variable.variable   != {}: output = "ERROR: Not all variables are destroyed.\n"
        if Liste.liste         != {}: output = "ERROR: Not all lists are destroyed.\n"

        print(output)
        return output