from threading import Thread

def createEnvironment(fileName):
    print("[Environment] Creating")
    file = open(fileName, "r")
    data = file.read()
    file.close()
    mData = ""
    for line in data.splitlines():
        if "debLang" in line:
            continue
        if "createEnvironment" in line:
            continue
        mData += line + "\n"
    debFile = open("debLang.py", "r")
    debData = debFile.read()
    debFile.close()
    outFile = open(f"d_{fileName}", "w")
    outFile.write("")
    outFile = open(f"d_{fileName}", "a")
    outFile.write(debData)
    outFile.write("\n")
    outFile.write(mData)
    outFile.close()
    print(f"[Evironment] Created as d_{fileName}")
    input()
    quit()

class Debuger:
    regVars = []

    def __init__(self, analizeFiles: tuple[str] = None) -> None:
        if analizeFiles is None:
            return
        for fileName in analizeFiles:
            file = open(fileName, "r")
            data = file.read()
            for line in data.splitlines():
                for i, word in enumerate(line.split()):
                    if "=" in word:
                        self.regVars.append(line.split()[i-1])
            file.close()

    def start(self):

        print("[Python Syntax]")
        app = Thread(target=self.console)
        app.start()

    def console(self):
        while True:
            command = input(">>")

            args = command.split()

            if args[0] == "p":
                compiledCommand = f"print({args[1]})"
            elif args[0] == "vars":
                compiledCommand = f"print(self.regVars)"
            else:
                compiledCommand = command

            try:
                exec(compiledCommand)
            except Exception as error:
                print("[Error]")
                print(error)