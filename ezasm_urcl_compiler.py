import sys

# initialization
programfilepath = input("program file path: ")
activefunc = False
variablename = []
funcname = []
funcvariable = []
iflist = []
commandwords = ["VAR","RET","FUNC","EQUAL","ADD","SUB","MULT","DIV","WHILE"]
comparisons = ["=","!=",">=","<=",">","<"]
comparisondict = {
    "=": "bne",
    "!=": "bre",
    ">=": "brl",
    "<=": "brg",
    ">": "ble",
    "<": "bge"
}
returnstack = []
nearestend = []
whilecount = 0
endcount = 0

with open(programfilepath) as programfile:
    program = programfile.readlines()

#operation functions
def add(a,b,res):
    if a in variablename:
        print("lod r1 m" + str(variablename.index(a)+1))
        arga = "r1"
    else:
        arga = str(a)

    if b in variablename:
        print("lod r2 m" + str(variablename.index(b)+1))
        argb = "r2"
    else:
        argb = str(b)
    print("add r3 " + str(arga) + " " + str(argb)) 
    print("str m" + str(variablename.index(res)+1) + " r3")

def sub(a,b,res):
    if a in variablename:
        print("lod r1 m" + str(variablename.index(a)+1))
        arga = "r1"
    else:
        arga = str(a)

    if b in variablename:
        print("lod r2 m" + str(variablename.index(b)+1))
        argb = "r2"
    else:
        argb = str(b)
    print("sub r3 " + str(arga) + " " + str(argb)) 
    print("str m" + str(variablename.index(res)+1) + " r3")

def mult(a,b,res):
    if a in variablename:
        print("lod r1 m" + str(variablename.index(a)+1))
        arga = "r1"
    else:
        arga = str(a)

    if b in variablename:
        print("lod r2 m" + str(variablename.index(b)+1))
        argb = "r2"
    else:
        argb = str(b)
    print("mlt r3 " + str(arga) + " " + str(argb)) 
    print("str m" + str(variablename.index(res)+1) + " r3")

def div(a,b,res):
    if a in variablename:
        print("lod r1 m" + str(variablename.index(a)+1))
        arga = "r1"
    else:
        arga = str(a)

    if b in variablename:
        print("lod r2 m" + str(variablename.index(b)+1))
        argb = "r2"
    else:
        argb = str(b)
    print("div r3 " + str(arga) + " " + str(argb)) 
    print("str m" + str(variablename.index(res)+1) + " r3")    
# first loop
for lineindex, line in enumerate(program):
    linenum = lineindex + 1
    instr = line.split()
    
    if instr[0] == "VAR":
        if len(instr) != 3:
            sys.exit("Error: expected 2 arguments, got: " + str(len(instr)-1) + " : at line: " + str(linenum))
        elif instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word: at line: " + str(linenum))
        elif instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name \"" + instr[1] + "\" already in use: at line: " + str(linenum))
        elif instr[1][0].isnumeric():
            sys.exit("Error: variable name cannot contain a number at the start: at line " + str(linenum))
        variablename.append(instr[1])
    
    elif instr[0] == "FUNC":
        if len(instr) != 3:
            sys.exit("Error: expected 2 arguments, got: " + str(len(instr)-1) + " :at line: " + str(linenum))
        elif instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word: at line: " + str(linenum))
        elif instr[1] in funcname or instr[1] in variablename:
            sys.exit("Error: name \"" + instr[1] + "\" already in use: at line: " + str(linenum))
        elif instr[2] in funcname or instr[2] in variablename:
            sys.exit("Error: name \"" + instr[2] + "\" already in use: at line: " + str(linenum))
        elif activefunc == True:
            sys.exit("Error: cannot define a function within a function: at line: " + str(linenum))
        activefunc = True
        endcount += 1 
        nearestend.append(endcount)
        variablename.append(instr[2])
        funcvariable.append(instr[2])

    elif instr[0] == "RET":
        if len(instr) >= 3:
            sys.exit("Error: expected 0-1 arguments, got: " + str(len(instr)-1) + " : at line: " + str(linenum))

    elif instr[0] == "END":
        if len(instr) != 1:
            sys.exit("Error: unexpected token: at line" + str(linenum))
        activefunc = False
        endcount += 1 
        nearestend.append(endcount)
    
    elif instr[0] == "WHILE":
        if len(instr) != 4:
            sys.exit("Error: expected 3 arguments, got: " + str(len(instr)-1) + " : at line: " + str(linenum))
        elif instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word: at line: " + str(linenum))
        elif instr[2] in commandwords:
            sys.exit("Error: name \"" + instr[2] + "\" cannot be a command word: at line: " + str(linenum))
        elif instr[2] not in comparisons:
            sys.exit("Error: invalid comparison \"" + instr[2] + "\": at line" + str(linenum))
        elif instr[3] in commandwords:
            sys.exit("Error: name \"" + instr[3] + "\" cannot be a command word: at line: " + str(linenum))
    
    elif instr[0] == "IF":
        if len(instr) != 4:
            sys.exit("Error: expected 3 arguments, got: " + str(len(instr)-1) + " : at line: " + str(linenum))
        elif instr[1] in commandwords:
            sys.exit("Error: name \"" + instr[1] + "\" cannot be a command word: at line: " + str(linenum))
        elif instr[2] in commandwords:
            sys.exit("Error: name \"" + instr[2] + "\" cannot be a command word: at line: " + str(linenum))
        elif instr[2] not in comparisons:
            sys.exit("Error: invalid comparison \"" + instr[2] + "\": at line" + str(linenum))
        elif instr[3] in commandwords:
            sys.exit("Error: name \"" + instr[3] + "\" cannot be a command word: at line: " + str(linenum))
                                 
# second loop
ifcount = 0
funccount = 0
endcount = 0
for lineindex, line in enumerate(program):
    linenum = lineindex + 1
    instr = line.split()

    if instr[0] == "VAR":
        print("str m"+ str(variablename.index(instr[1])+1) + " " + instr[2])
    elif instr[0] in variablename:
        if len(instr) != 4 and len(instr) != 5 and len(instr) != 3:
            sys.exit("Error: unexpected token \"" + " ".join(instr) + "\" at line " + str(linenum))
        elif instr[1] != "EQUAL":
            sys.exit("Error: unexpected token \"" + " ".join(instr) + "\" at line " + str(linenum)) 
        elif len(instr) == 5 and instr[3] == "ADD":
            add(instr[2],instr[4],instr[0])
        elif len(instr) == 5 and instr[3] == "SUB":
            sub(instr[2],instr[4],instr[0])
        elif len(instr) == 5 and instr[3] == "MULT":
            mult(instr[2],instr[4],instr[0])
        elif len(instr) == 5 and instr[3] == "DIV":
            div(instr[2],instr[4],instr[0])  
        elif len(instr) == 4 and instr[2] in funcname:
            print("lod r5 m" + str(variablename.index(instr[3])+1))
            print("str m" + str(variablename.index(funcvariable[funcname.index(instr[2])])+1) + " r5")
            print("cal ." + instr[2])
            print("str m" + str(variablename.index(instr[0])+1) + " r4")
        elif len(instr) == 3 and instr[2] in variablename:
            print("lod r3 m" + str(variablename.index(instr[2])+1))
            print("str m" + str(variablename.index(instr[0])+1) + " r3")
        elif len(instr) == 3 and instr[2].isnumeric():
            print("str m" + str(variablename.index(instr[0])+1) + str(instr[2]))
        else:
            sys.exit("Error: unexpected token \"" + " ".join(instr) + "\" at line " + str(linenum))

    elif instr[0] == "WHILE":
        if instr[1] not in variablename and not instr[1].isnumeric():
            sys.exit("Error: unexpected argument \"" + instr[1] + "\": at line: " + str(linenum))
        elif instr[3] not in variablename and not instr[3].isnumeric():
            sys.exit("Error: unexpected argument \"" + instr[3] + "\": at line: " + str(linenum))
        if instr[1] in variablename:
            print("lod r1 m" + str(variablename.index(instr[1])+1))
            arga = "r1"
        else:
            arga = str(instr[1])
        if instr[3] in variablename:
            print("lod r2 m" + str(variablename.index(instr[3])+1))
            argb = "r2"
        else:
            argb = str(instr[3])
        whilecount += 1
        print(".while" + str(whilecount))
        returnstack.append("while" + str(whilecount))
        print(comparisondict[instr[2]] + " .end" + str(nearestend[whilecount-1]) + " " +  arga + " " + argb)
    
    elif instr[0] == "END":
        if (returnstack[len(returnstack)-1] not in funcname) and (returnstack[len(returnstack)-1] not in iflist):
            endcount += 1 
            print("jmp ." + returnstack.pop())
        else: 
            endcount += 1
        print(".end" + str(endcount))
    
    elif instr[0] == "FUNC":
        funcname.append(instr[1])    
        returnstack.append(str(instr[1]))
        funccount += 1
        print("jmp .end" + str(nearestend[endcount]) )
        print("." + str(instr[1]))
    
    elif instr[0] == "RET":
        if len(instr) == 2:
            if instr[1] in variablename:
                print("lod r4 m" + str(variablename.index(instr[1])+1))
                arg = "r4"
            else:
                arg = str(instr[1])
        print("ret")
    
    elif instr[0] == "IF":
        if instr[1] not in variablename and not instr[1].isnumeric():
            sys.exit("Error: unexpected argument \"" + instr[1] + "\": at line: " + str(linenum))
        elif instr[3] not in variablename and not instr[3].isnumeric():
            sys.exit("Error: unexpected argument \"" + instr[3] + "\": at line: " + str(linenum))
        if instr[1] in variablename:
            print("lod r1 m" + str(variablename.index(instr[1])+1))
            arga = "r1"
        else:
            arga = str(instr[1])
        if instr[3] in variablename:
            print("lod r2 m" + str(variablename.index(instr[3])+1))
            argb = "r2"
        else:
            argb = str(instr[3])
        ifcount += 1
        iflist.append("if" + str(ifcount))
        returnstack.append("if" + str(ifcount))
        print(comparisondict[instr[2]] + " .end" + str(nearestend[ifcount-1]) + " " +  arga + " " + argb)

    elif instr[0] in funcname:
        if instr[1] in variablename:
            print("lod r5 m" + str(variablename.index(instr[1])+1))
        else:
            print("imm r5 " + str(instr[1]))
        print("str m" + str(variablename.index(funcvariable[funcname.index(instr[0])])+1) + " r5")
        print("cal ." + instr[0])