from threading import Thread

def leadingSpaces(line):
    count = ''
    for char in line:
        if char == ' ':
            count += " "
        else:
            break
    return count

def createEnvironment(fileName, setLogs=False):
    print("[Environment] Creating")
    file = open(fileName, "r")
    data = file.read()
    file.close()
    mData = ""
    debDeclared = False
    debVar = None
    for line in data.splitlines():
        if "debLang" in line:
            continue
        if "createEnvironment" in line:
            continue
        if "=" in line and "Debuger" in line:
            debDeclared = True
            debVar = line.split()[0]
        mData += line + "\n"
        if setLogs and debDeclared and mData.split()[-1] != f"{debVar}.log()" and not "def" in line and not "with" in line and not "if" in line and not "while" in line and not "for" in line and not "elif" in line and not "else" in line and not "class" in line and not "quit()" in line:
            mData += leadingSpaces(line) + f"{debVar}.log()\n"
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
    regVars: list[str] = []
    logs: list[dict[str, str]] = []

    def __init__(self, analizeFiles: tuple[str] | None = None, excludeLibs: tuple[str] | None = None) -> None:
        if analizeFiles is not None:
            self.analizeFiles(analizeFiles, excludeLibs)

    def log(self):
        self.logs.append({})
        for varName in self.regVars:
            try:
                exec(f"self.logs[-1]['{varName}'] = {varName}")
            except:
                pass

    def analizeFiles(self, analizeFiles, excludeLibs=None):
        for fileName in analizeFiles:
            file = open(fileName, "r")
            data = file.read()
            for line in data.splitlines():
                for i, word in enumerate(line.split()):
                    if "=" in word and excludeLibs is None:
                        self.regVars.append(line.split()[i-1])
                        continue
                    if "=" in word and not True in [lib in line for lib in excludeLibs]:
                        self.regVars.append(line.split()[i-1])
                        continue
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
            elif args[0] == "logs":
                if len(args) == 2:
                    compiledCommand = f"print(self.logs[{args[1]}])"
                else:
                    compiledCommand = "print(self.logs)"
            else:
                compiledCommand = command

            try:
                exec(compiledCommand)
            except Exception as error:
                print("[Error]")
                print(error)