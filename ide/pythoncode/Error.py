import os

class Error:
    def main(errorType:int):
        print(errorType)
        match errorType:
            case 0: Error.createFile("Run Error", "0", "Save before run.")

    def createFile(ErrorName:str, ErrorType:str, ErrorMsg:str):
        file = f'Dim Msg, Title, Style\nMsg = "ERROR {ErrorType}: {ErrorMsg}"\nTitle = "{ErrorName}"\nStyle = vbOKCancel\nWindow = MsgBox(Msg, Style, Title)'
        with open("ErrorFile.vbs", "w")as f:
            f.write(file)
        os.system("ErrorFile.vbs")
