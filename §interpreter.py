from List import Liste
from Variable import Variable
from Function import Function

class Lencer:
    output = ""
    def __init__(self, contentraw):
        if contentraw.startswith("open "):
            contentraw = contentraw.strip("open ")
            contentraw = Lencer.getFile(contentraw)
        content = []
        if "Â" in contentraw:
            for char in contentraw:
                if char == "Â": char = ""
                content.append(char)
            content = "".join(content)
        else: content = contentraw
        content=content.replace("|", "\n").split("\n")
        Lencer.main(content)

    def main(content):
        index = 0
        for line in content:
            index += 1
            if line == ""              : continue
            elif line.startswith("§§") : Liste.assigne(line)
            elif line.startswith("$§§"): Liste.destroy(line)
            elif line.startswith("§")  : Variable.assigne(line)
            elif line.startswith("$§") : Variable.destroy(line) 
            elif line.startswith(">>>"): Function.give_out(line)
            elif line.startswith("?")  : Function.startCondition(line)
            elif line.startswith("$?")  : Function.endCondition()

        if Function.conditions != 0: print("ERROR: Not all conditions are ended.")
        if Variable.variable != {}: print("ERROR: Not all variables are destroyed.")
        if Liste.liste != {}: print("ERROR: Not all lists are destroyed.")


    def getFile(fileName):
        try:
            with open(fileName, "r")as f:
                FileContent = f.read()
                return FileContent
        except FileNotFoundError:
            print("File not found")


lencer = Lencer(input(">>> "))