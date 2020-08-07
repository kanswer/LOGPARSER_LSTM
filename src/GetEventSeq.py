import GetTemplate
import LoadData
import numpy

def GetEventSeq(log_file,template_file): #only response source lof-file and template
    EventSeq=[]
    fr=open(log_file)
    Template=GetTemplate.GetTemplate(template_file)
    for line in fr.readlines():
        line_pre=line.strip().split(' ')
        content=line_pre[9:]
        for i in range(len(content)):
            if LoadData.hasNumbers(content[i]):
                content[i]="<*>"
        s=''
        for word in content:
            s=s+word+' '
        s=s.strip(' ')
        mindiff=20
        e=''
        for event in Template:
            event=event.strip(' ')
            if event.find(s)!=-1:
                e_line=event.split(' ')
                diff=len(e_line)-len(content)
                if diff<mindiff:
                    mindiff=diff
                    e=e_line[0]
        event_no=0
        power=1
        event_num=[]
        for char in e:
            if char.isdigit():
                event_num.append(int(char))
        while len(event_num)!=0:
            event_no=event_no+event_num.pop()*power
            power=power*10
        EventSeq.append(event_no)
    return EventSeq

numpy.savetxt('EventSequence',GetEventSeq('D:\SIT_PROJECT\LogParser_LSTM\src\BGL_2k.log','D:\SIT_PROJECT\LogParser_LSTM\pre_data'),fmt='%s')