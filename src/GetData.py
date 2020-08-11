ParserNum=3
import numpy as np
def GetData(filename):
    x_data=[]
    y_data=[]
    fr=open(filename)
    c=0
    x=[]
    for line in fr.readlines():
        if c>=ParserNum:
            y_data.append(float(line))
            x_data.append(x)
            x.pop(0)
        x.append(float(line))
        c=c+1
    return np.array(x_data),np.array(y_data)
