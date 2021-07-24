print ("Starter mobil script...")

loop = True

class FileObj():
    def __init__(self):
        self.filnavn = ""
        self.innhold = []
    def add_content(self, string):
        self.innhold.append(string)
    def show_content(self):
        print ("List entries:", len(self.innhold))
        for entry in self.innhold:
            print ("    ", entry)
    def save_content(self):
        if self.filnavn == "":
            print ("specify filename first!")
            return False
        with open(self.filnavn, "w", encoding="UTF-8") as f:
            for entry in self.innhold:
                f.writelines(entry+"\n")
            f.close()
        return True

fileobj = FileObj()
while loop:
    cmd = input("-: ")
    if (cmd.lower() == "q"): loop = False
    #fileobj = FileObj()
    if (cmd.lower() == "h"):
        print ("commands= FILE, ADD, SAVE, SHOW")
    if (cmd.lower() == "file"):
        inp = input("filename:")
        fileobj.filnavn=inp
    if (cmd.lower() == "add"):
        inp = input("add:\n")
        fileobj.add_content(inp)
    if (cmd.lower() == "save"):
        fileobj.save_content()
    if (cmd.lower() == "show"): fileobj.show_content()
