import sys
programfilepath = input("program file path: ")
variablename = []
with open(programfilepath) as programfile:
    program = programfile.readlines()

for line in program: 
    instr = line.split()
    if instr[0] == "VAR":
        if len(instr) == 1:
            sys.exit("Error: missing argument at line "+ str(program.index(line)+1))
        variablename.append(instr[1])
print(variablename)
