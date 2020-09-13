ParserNum=3
import GetEventSeq
import numpy as np
def GetData():
    event_seq=GetEventSeq.GetEventSeq('D:\SIT_PROJECT\LogParser_LSTM\src\BGL_2k.log','D:\SIT_PROJECT\LogParser_LSTM\pre_data')
    datax=[]
    datay=[]
    for i in range(0,len(event_seq)-ParserNum,1):
        seq_in=event_seq[i:i+ParserNum]
        seq_out=event_seq[i+ParserNum]
        datax.append(seq_in)
        datay.append(seq_out)
    return datax,datay