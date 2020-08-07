ParserDepth=12

def hasNumbers(inputString):
    for char in inputString:
        if char.isdigit():
            return True
    return False

def LoadDataSet(filename):
    Contents=[]
    fr=open(filename)
    for line in fr.readlines():
        line_pre=line.strip().split(' ')
        content=line_pre[9:]
        for i in range(len(content)):
            if hasNumbers(content[i]):
                content[i]='<*>'
        s=''
        for word in content:
            s=s+word+' '
        s=s.strip(' ')
        Contents.append(s)
    return Contents
