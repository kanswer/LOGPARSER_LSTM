import numpy
import LoadData
import GetTemplate

Contents=LoadData.LoadDataSet('D:\SIT_PROJECT\LogParser_LSTM\src\BGL_2k.log')
numpy.savetxt('pre_data',Contents,fmt='%s') #preprocess log data
numpy.savetxt('template',GetTemplate.GetTemplate('D:\SIT_PROJECT\LogParser_LSTM\pre_data'),fmt='%s') #get template