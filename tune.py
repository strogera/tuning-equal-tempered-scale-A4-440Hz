notesData={} #notesData = { freq: note }

#Read data form file "data" in the current directory
with open("data", "r") as inputF:
    for line in inputF:
        elems=line.strip().split()
        notesData[float(elems[1])]=elems[0]

def findClosestNote(f):
    #finds the closest note to frequency f
    noteFreq=None
    previousDistance=None
    for curNote in notesData.keys():
        curDistance=abs(curNote-f)
        if (not previousDistance) or curDistance<previousDistance:
            noteFreq=curNote
        previousDistance=curDistance
    return noteFreq
        
with open("sample.csv", "r") as inputFile:
    with open("output.csv", "w+") as outputFile:
        outputFile.write("\"Range\";\"Average\";\"Note\";\"Note's Frequency\"\n")
        for line in inputFile:
            cells=line.strip().split(';')
            nums=cells[0].split('-')
            avrg=(int(nums[0])+int(nums[1]))/2
            print()
            print("Average of (%s,%s): %s"%(nums[0], nums[1], avrg))
            notesfreq=findClosestNote(avrg)
            print("Note Freq: %s"%notesfreq)
            note=notesData[notesfreq]
            print("Note: %s"%note)
            outputFile.write(cells[0]+';'+str(avrg)+';'+'\"'+note+'\"'+';'+str(notesfreq)+'\n')
        

