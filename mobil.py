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
        with open(self.filnavn, "w", encoding="UTF-8") as f:
            for entry in self.innhold:
                f.writelines(entry)
            f.close()

fileobj = FileObj()
while loop:
    cmd = input("-: ")
    if (cmd == "q"): loop = False
    #fileobj = FileObj()
    if (cmd == "h"):
        print ("commands= ADD, SAVE, SHOW")
    
