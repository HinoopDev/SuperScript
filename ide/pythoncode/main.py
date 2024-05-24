import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.scrolledtext import ScrolledText

from main_Interpreter import Lencer
from Error import Error


#---------------------------------------------------------------window
root = tk.Tk()
root.title("Editor v.2")
root.config(bg="#454545")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")


#---------------------------------------------------------------Vars
runing = True

bFont = ("Courier New", 14, "bold")
tFont = ("Courier New", 14)

inFg = "#DEDEDE"

keywordFG   = "#FF8C00"
konditionFG = "#00AAAA"
methodFG    = "#00FF00"
numberFG    = "#8A2BE2"
KommentarFG = "#565656"
errorBG     = "#FF0000"
EndLineFG   = "#000000"
EndLineBG   = "#00FFFF"


defaultfileName = ""
saveFilePath =  ""
fileContent = ""


#---------------------------------------------------------------Defs
def openfile() -> None:
    '''opens code from diferent file'''
    global defaultfileName, fileContent
    filePath = askopenfilename(filetypes=[("Super Script", "*.ss"), ("Python File", "*.py")])
    if filePath != "":
        defaultfileName = filePath
        inputText.delete(1.0, tk.END)
        with open(filePath, "r")as f:
            fileContent = f.read()
            inputText.insert(tk.END, fileContent)
        outputText.insert(tk.END, f"\nopend : {filePath}\n")
        root.title(filePath)

def save() -> None:
    '''saves the written code'''
    global saveFilePath
    tosave = inputText.get("1.0", tk.END)
    fileName= asksaveasfilename(filetypes=[("Super Script", "*.ss"), ("Python File", "*.py")])
    saveFilePath = fileName
    if fileName.endswith(".ss"):
        with open(fileName, "w")as f:
            f.write(tosave)
    elif not fileName.endswith(".ss") and not fileName.endswith(".py"):
        with open(f"{fileName}.ss", "w")as f:
            f.write(tosave)
            fileName = f"{fileName}.ss"
    else: 
        with open(fileName, "w")as f:
            f.write(tosave)
    outputText.insert(tk.END, f"\nsaved as : {fileName}\n")
    root.title(fileName)

def run() -> None:
    '''runs the code'''
    global output
    if saveFilePath == "":
        Error.main(0)
    else:
        Lencer.reset()
        output = Lencer.prep(inputText.get("1.0", tk.END), outputText)
        outputText.insert(tk.END, f"\n{output}")

def exitCode() -> None:
    '''exits the code'''
    global runing
    runing = False



def checkHighlight() -> None:
    '''makes the symbole highlighting'''
    start = "1.0"
    end = "end"

    for mylist in wordlist:
        num = int(wordlist.index(mylist))

        for word in mylist:
            inputText.mark_set("matchStart" , start)
            inputText.mark_set("matchEnd"   , start)
            inputText.mark_set("SearchLimit", end)

            mycount = tk.IntVar()

            while True:
                index = inputText.search(word, "matchEnd", "SearchLimit", count=mycount, regexp=False)

                if index == "": break
                if mycount.get() == 0: break

                inputText.mark_set("matchStart", index)
                inputText.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))
                inputText.tag_add(tags[num], "matchStart", "matchEnd")

def scan() -> None:
    '''heighlights patterns in the code'''
    text = inputText
    start = 1.0
    end = "end"
    count = tk.IntVar()
    regexp_patterns = [r'//.*', r'".*"']#Kommentar, string
    for pattern in regexp_patterns:
        text.mark_set("startMark", start)
        text.mark_set("endMark",   end)
        num = int(regexp_patterns.index(pattern))
        while True:
            index = text.search(pattern, "startMark", "endMark", count=count, regexp=True)
            if index=="": break
            if num == 0:
                text.tag_add(tags[6], index, index + "lineend")
            elif num == 1:
                text.tag_add(tags[3], index, "%s+%sc"%(index, count.get()))
            text.mark_set("startMark", "%s+%sc"%(index, count.get()))

def scanOutput() -> None:
    
    text = outputText
    start = 1.0
    end = "end"
    count = tk.IntVar()
    regexp_patterns = r'ERROR: .*'
    text.mark_set("startMark", start)
    text.mark_set("endMark",   end)
    num = int(0)
    while True:
        index = text.search(regexp_patterns, "startMark", "endMark", count=count, regexp=True)
        if index=="": break
        if num == 0:
            text.tag_add("ERROR", index, index + "lineend")
        text.mark_set("startMark", "%s+%sc"%(index, count.get()))


#---------------------------------------------------------------Buttons
buttonFrame = tk.Frame(root, bg="#232323", width=int(root.winfo_width()*0.2), height=int(root.winfo_height()))

openButton = tk.Button(buttonFrame, text="open", bg=inFg, font=(bFont), command=lambda:openfile())
saveButton = tk.Button(buttonFrame, text="save", bg=inFg, font=(bFont), command=lambda:save())
runButton  = tk.Button(buttonFrame, text="run" , bg=inFg, font=(bFont), command=lambda:run ())
exitButton = tk.Button(buttonFrame, text="exit", bg=inFg, font=(bFont), command=lambda:exitCode())



#---------------------------------------------------------------Text
labelFrame = tk.Frame(root, bg="#454545")
inputText  = ScrolledText(labelFrame, width=int(root.winfo_screenwidth()*0.114), height=int(root.winfo_screenheight())*0.02, bg=inFg, font=tFont)
outputText = ScrolledText(labelFrame, width=int(root.winfo_screenwidth()*0.114), height=int(root.winfo_screenheight())*0.02, bg=inFg, font=tFont)

#Tags
inputText.tag_configure("keywords",    foreground=keywordFG)
inputText.tag_configure("konditionen", foreground=konditionFG)
inputText.tag_configure("methodes",    foreground=methodFG)
inputText.tag_configure("IntStr",      foreground=numberFG)
inputText.tag_configure("Kommentar",   foreground=KommentarFG)
inputText.tag_configure("Error",       background=errorBG)
inputText.tag_configure("EndLine",     background=EndLineBG, foreground=EndLineFG)

outputText.tag_configure("ERROR", background=errorBG)

tags     = ["keywords", "konditionen", "methodes", "IntStr", "Error", "EndLine", "Kommentar"]
wordlist = [Lencer.KEY_WORDS, Lencer.METHODES, Lencer.CONDITION, ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], [" "], ["|", "'"]]


#---------------------------------------------------------------footer
footerFrame = tk.Frame(root)
impressum   = tk.Label(footerFrame, text=("IDE created by TPA                                                                                                                  \n"
                                          "Superscript created ba TPA                                                                                                          \n"), font=inFg, bg="#454545")


#---------------------------------------------------------------grid
buttonFrame.grid(row=0, column=0, sticky="NS")
openButton.grid (row=0, column=0, sticky="EW", padx=4, pady=2)
saveButton.grid (row=1, column=0, sticky="EW", padx=4, pady=2)
runButton.grid  (row=2, column=0, sticky="EW", padx=4, pady=2)
exitButton.grid (row=3, column=0, sticky="EW", padx=4, pady=2)

labelFrame.grid(row=0, column=1)
inputText .grid(row=0, column=0, padx=4, pady=2)
outputText.grid(row=1, column=0, padx=4, pady=2)

footerFrame.grid(row=2, column=0, columnspan=2)
impressum.pack(side="left", anchor="w", expand=True, fill="both")


#------------------------------------------------------------------mainloop
while runing:
    scan()
    scanOutput()
    checkHighlight()
    root.update()