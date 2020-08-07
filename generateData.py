with open("data", "r") as inputF:
    with open ("notesData.py", "w+") as outputF:
        outputF.write("notes={\n")
        num_lines = sum(1 for line in inputF)
        inputF.seek(0)
        for i, line in enumerate(inputF):
            elems=line.strip().split()
            outputF.write(elems[1])
            outputF.write(': \'')
            outputF.write(elems[0])
            if i!=num_lines-1:
                outputF.write('\',\n')
            else:
                outputF.write('\'\n')
        outputF.write("}\n")


