import numpy as np
import pandas as pd
import xlrd

pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')
pop_c18 = pd.read_excel(r'DDW-C18-0000.xlsx')
pop_c19 = pd.read_excel(r'DDW-C19-0000.xlsx')

state_codes=set(pop_data["State"])
state_list=list(pop_data["State"])
level=list(pop_data["Level"])
tru=list(pop_data['TRU'])
tot_p=list(pop_data['TOT_P'])

name=list(pop_data["Name"])
sp_dict={}

for i in state_codes:
    idx=[j for j in range(len(state_list)) if state_list[j]==i and (level[j]=="STATE" or level[j]=="India") and tru[j]=="Total"]
    for j in idx:
        sp_dict[i]=tot_p[j]
#         print(i," ",j," ",name[j]," ",tot_p[j])
        


col=["State code","District code","Area Name","Tru","Age-group","Number speaking second language","Number speaking third language"
]

popc=pop_c18[5:].rename(columns={"C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX":"state",
                                "Unnamed: 1":"District",
                                "Unnamed: 2":"Area name",
                                "Unnamed: 3":"tru",
                                "Unnamed: 4":"Age-group",
                                "Unnamed: 5":"Persons-L2",
                                "Unnamed: 6":"Males-L2",
                                "Unnamed: 7":"Females-L2",
                                "Unnamed: 8":"Persons-L3",
                                "Unnamed: 9":"Males-L3",
                                "Unnamed: 10":"Females-L3",})

state_listc=list(popc["state"])
tru=list(popc["tru"])
totp1=list(popc['Persons-L2'])
totp2=list(popc['Persons-L3'])
state_code1=popc["state"].unique()
names=list(popc["Area name"])
ageg=list(popc["Age-group"])

state_names=list(popc["Area name"].unique())
state_codes=list(popc["state"].unique())


s2={}
s3={}
k=0
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j]=="Total"  and ageg[j]=="Total")]
    for j in idx:
        s2[k]=totp1[j]
        s3[k]=totp2[j]
        k+=1

L1=[]
L2=[]
L3=[]
li=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35']
k=0
codes=[]
snames=[]
for i in sp_dict:
    l1= ((sp_dict[i]-s2[i])/sp_dict[i])*100
    l2= ((s2[i]-s3[i])/sp_dict[i])*100
    l3= (s3[i]/sp_dict[i])*100
    L1.append(l1)
    L2.append(l2)
    L3.append(l3)
    codes.append(str(li[k]))
    snames.append(state_names[k])
    k+=1


percentind = {'State-code': codes,'percent-one':L1,'percent-two':L2,'percent-three':L3}
percentind = pd.DataFrame(percentind)
percentind.to_csv('percent-india.csv',index=False)









