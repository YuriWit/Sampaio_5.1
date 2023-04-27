import argparse
import string

# parse parameters from cmd
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="this is the assembly file")
parser.add_argument("-o", "--output", help="this is the opcode file ready for the simulator")
args = parser.parse_args()

if args.output == None:
    args.output = args.filename.split(".")[0] + ".out"

infile = args.filename
outfile = args.output


# get data from file
data = ""
with open(infile, "r") as file:
    data = file.read()

# remove irrelevant spaces, tabs
data = "".join(data.split("\t"))
data = "".join(data.split(" "))
data = data.split("\n")

# remove comments
cmds = []
for i in range(len(data)):
    data[i] = data[i].split(";")[0]
    if data[i] in [None, "", '']:
        continue
    cmds.append(data[i])

# parse opcodes from individual commands
opcodes = []
for cmd in cmds:
    if cmd[0:3] == "mov":
        if cmd[3] == "R":
            if cmd[6] == "R": # MOV R, R
                opcodes.append(0 + int(cmd[4])*4 + int(cmd[7]))
            elif cmd[6] == "[": # MOV R, [R]
                opcodes.append(64 + int(cmd[4])*4 + int(cmd[8]))
            else: # MOV R, K
                opcodes.append(16 + int(cmd[4])*4)
                opcodes.append(int(cmd.split(",")[-1]))
                
        if cmd[3] == "[":
            opcodes.append(32 + 16 + int(cmd[5])*4 + int(cmd[9]))
        pass
    elif cmd[0:3] == "add":
        opcodes.append(32 + int(cmd[4])*4 + int(cmd[7]))
    elif cmd[0:2] == "jz":
        opcodes.append(64 + 16 + int(cmd[3])*4)

# generate program
program = "v3.0 hex words addressed\n"
for i in range(16):
    program += format(i*16, '02x') + ":"
    for j in range(16):
        if i*16+j < len(opcodes):
            program += " " + format(opcodes[i*16+j], '02x')
        else:
            program += " 00"
    program += "\n"

# save output file
with open(outfile, "w") as file:
    file.write(program)
