import os
import re
import pickle

file=r'./FJS'
files=os.listdir(file)
for f in files:
    file_path=os.path.join(file,f)
    Instance=[]
    with open(file_path,'r') as data:
        List=data.readlines()
        for line in List:
            pat = r'\d+'
            result = re.findall(pat, line)
            li = [int(ri) for ri in result]
            Instance.append(li)
    # print(Instance)
    n,m,means_m=Instance[0][0],Instance[0][1],Instance[0][2]
    del Instance[0]
    PT=[]
    MT=[]
    ni=[]
    for Ii in Instance:
        if Ii!=[]:
            JPTi=[]
            JMTi=[]
            Oi=Ii
            O_num=Oi[0]
            ni.append(O_num)
            del Oi[0]
            for i in range(O_num):
                OPTi=[]
                OMTi=[]
                Mi=Oi[0]
                del Oi[0]
                for j in range(Mi):
                    OMTi.append(Oi[2*j])
                    OPTi.append(Oi[2*j+1])
                JPTi.append(OPTi)
                JMTi.append(OMTi)
                del Oi[:2*Mi]
            PT.append(JPTi)
            MT.append(JMTi)
    new_f = f.split('.')[0]
    FJSP_Instance={'n':n,'m':m,'processing_time':PT,'Processing machine':MT,'Jobs_Onum':ni}
    if not os.path.exists(r'./FJSP_Instance'):
        os.makedirs(r'./FJSP_Instance')
    with open(os.path.join(r'./FJSP_Instance',new_f+".pkl"),"wb") as f1:
        pickle.dump(FJSP_Instance, f1, pickle.HIGHEST_PROTOCOL)