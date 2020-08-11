def GetTemplate(filename):
    Cluster=[]
    no=0
    fr=open(filename)
    for line in fr.readlines():
        line=line.strip()
        if line not in Cluster:
            Cluster.append(line)
    Cluster.sort()
    for i in range(len(Cluster)):
        Cluster[i]='E'+str(no)+' '+Cluster[i]
        no=no+1
    return Cluster