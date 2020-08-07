import notesData 
import freqData

def findClosestNote(f):
    noteFreq=-1
    previousDistance=-1
    for curNote in freqData.freq:
        curDistance=abs(curNote-f)
        if previousDistance==-1 or curDistance<previousDistance:
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
            note=notesData.notes[notesfreq]
            print("Note: %s"%note)
            outputFile.write(cells[0]+';'+str(avrg)+';'+'\"'+note+'\"'+';'+str(notesfreq)+'\n')
        

