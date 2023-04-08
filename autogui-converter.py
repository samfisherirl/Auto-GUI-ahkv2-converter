from pathlib import Path
from sys import argv
cwd = Path(__file__).parent
from random import randrange

class GUIAdd:
    def __init__(self, type, dimensions):
        type = type.strip()
        self.type = f"this.MyGUI.Add{type}"
        self.x = ""
        self.y = ""
        self.w = ""
        self.h = "" 
            
        self.g = ""
        self.v = ""
        self.func = ""
        self.var = ""
        self.string = ""
        self.name = ""
        self.dimension(dimensions)
        self.string = self.stringify()

    def dimension(self, dimensions):
        dims = dimensions[0].split(" ")
        for i in dims:
            if "x" in i:
                self.updateValue("x", i)
            if "y" in i:
                self.updateValue("y", i)
            if "h" in i:
                self.updateValue("h", i)
            if "w" in i:
                self.updateValue("w", i)

        try:
            [self.updateValue("g", i[1:]) if i != "" and "g" in i[0] else self.updateValue("v", i[1:]) if i != "" and "v" in i[0] else print() for i in dimensions[0].split(" ")]
        except Exception as e:
            print(str(e))
    
    def updateValue(self, obj, i):
        if not "+" in i:
            setattr(self, obj, i.strip())

    def stringify(self):
        if self.v == "" and self.g == "":
            x = randrange(10, 99)
            x = int(x)
            self.g = str(f"element{x}")
        elif self.v != "" and self.g == "":
            self.g = self.v
        self.var = f"this.{self.g}_"
        val = "(){\n\t\n\n\t\t}"
        if self.name == "":
            self.name = self.g
        self.func = f"{self.g}_click{val}"
        return f"""this.{self.g}_ := {self.type}(\"{self.x} {self.y} {self.w} {self.h}\", \"{self.name}\")\n\tthis.{self.g}_.OnEvent("Click", this.{self.g}_click)"""

    

class Converter:
    def __init__(self):
        self.file = cwd / "ahk_before_conversion.ahk"
        self.out = cwd / "ahk_after_conversion.ahk"
        self.contents = []
        self.elements = []
        self.objects = []
        self.prelude = self.preluder()
        self.this_ = ""
        self.functions = ""

    def reader(self):
        with open(self.file, "r") as f:
            self.contents = f.readlines()
            
    def iterator(self):
        [self.process(i) for i in self.contents]

    def process(self, i):
        self.convert(i.split(","))

    def convert(self, split):
        if "Gui Add" in split[0]:
            self.handleAdd(split[1:])
        elif "Gui Font" in split[0]:
            pass
        
    def handleAdd(self, list):
        if len(list) == 2:
            x = GUIAdd(str(list[0]), (list[1:]))
            self.objects.append(x)
        if len(list) == 3:
            x = GUIAdd(str(list[0]), (list[1:]))
            x.name = list[2]
            self.objects.append(x)
        
    def preluder(self):
        return """#SingleInstance Force
#Requires AutoHotkey v2
#Warn all, Off

G := MyGui_Create()
{
    __New() {
    this.MyGUI := Gui(,"NameHere")\n"""


    def textbody(self):
        x = [f"{self.this_}\n\t{i.string}" for i in self.objects]
        for i in x:
            self.this_ = str(f"{self.this_}{i}")
        y = [f"{self.functions}\n\t{i.func}" for i in self.objects]
        for i in y:
            self.functions = str(f"{self.functions}{i}")
        self.this_ = str(self.this_ + "\n\t}")
        self.functions = str(self.functions + "\n}")
        
    def printer(self):
        with open(self.out, "w") as f:
            f.write(str(f"{self.prelude}{self.this_}{self.functions}\n\n"))
        print(str(f"{self.prelude}{self.this_}{self.functions}\n\n"))
        
    def setpath(self, file):
        if file[1] == "-":
            file = file.replace("--", "") 
        if file[0] == "-":
            file = file.replace("-", "") 
        file = Path(file)
        self.file = file
        p = file.parent
        s = file.stem
        self.out = Path(f"{p}\\{s}__v2.ahk")
        
if __name__ == "__main__":
    convert = Converter()
    print(str(argv))
    if len(argv) > 1:
        convert.setpath(argv[1])
        
    convert.reader()
    convert.iterator()
    convert.textbody()
    convert.printer()