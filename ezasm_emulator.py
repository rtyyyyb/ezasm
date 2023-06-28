import sys
running = True
activefunc = False
variablename = []
variablevalue = []
funcname = []
funcvariable = []
iflist = []
commandwords = ["VAR","RET","FUNC","EQUAL","ADD","SUB","MULT","DIV","WHILE"]
comparisons = ["=","!=",">=","<=",">","<"]
returnstack = []
nearestend = []
whilecount = 0
endcount = 0

with open(input("program file path: ")) as programfile:
    program = programfile.readlines()

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
        variablevalue.append(instr[2])
    
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

programcount = 0
while running == True:
    instr = program[programcount]
    print(instr)
    
    programcount += 1















    
