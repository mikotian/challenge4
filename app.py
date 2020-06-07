import sys

def main():
    file=str(sys.argv[1])
    messages=get_messages(file)
    print(messages)
    tests=int(messages[0])
    j=1
    for i in range(tests):
        while(j<(len(messages)-2)):
             patients=int(messages[j].rstrip().split()[0])
             print(patients)
             queries=int(messages[j].rstrip().split()[1])
             print(queries)
             j=j+1
             pstring=messages[j]
             print(pstring)
             j=j+1
             for k in range(queries):
                 print(k, messages[j+k])
                 sortpatients(pstring, int(messages[j+k]))

def get_messages(inp_file):
    with open(inp_file) as fp: 
        Lines = fp.readlines() 
    return Lines
      
def sortpatients(pstring, numCentres):
    centres = {}
    for a in range(numCentres):
        centres[a]=set()
    pending=[]
    if numCentres==0:
        pending=pstring.chararray()
        print(len(pending))
        return
    else:
        for index in range(len(pstring)-1):
            added=False
            for x in centres:
                if(pstring[index] in centres[x]):
                    continue
                else:
                    temp=centres[x]
                    temp.add(pstring[index])
                    centres[x]=temp
                    added=True
                    break
            if(not added):
                pending.append(pstring[index])
#            if pstring[index] in centres:
#                temp=centres.get(pstring[index])
#                centres[pstring[index]]=temp+1
#            elif pstring[index] not in centres and len(centres)<numCentres :
#                centres[pstring[index]]=1
#            elif pstring[index] not in centres and len(centres)==numCentres :
#                pending.append(pstring[index])
    print(len(pending))

if __name__=="__main__":
    main()
