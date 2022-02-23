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
s2={}
s3={}
k=0
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j]=="Total"  and ageg[j]=="Total")]
    for j in idx:
        s2[k]=totp1[j]
        s3[k]=totp2[j]
        k+=1

statencodes={}
state_names=names=list(popc["Area name"].unique())
for i in range(len(state_code1)):
    statencodes[state_code1[i]]=state_names[i]
codesncodes={}
for i in range(len(state_code1)):
    codesncodes[i]=state_code1[i]


s5={}
codes=[]
snames=[]
ratios=[]
for i in sp_dict:
    s5[i]=(s2[i]-s3[i])/(sp_dict[i]-s2[i]) 
li1=sorted(s5.items(), key=lambda item: item[1],reverse=True)[:3]
# print(li1)
li2=sorted(s5.items(), key=lambda item: item[1])[:3]
# print(li2)
for i in li1:
    codes.append(codesncodes[i[0]])
    snames.append(statencodes[codesncodes[i[0]]])
    ratios.append(i[1])
for i in li2:
    codes.append(codesncodes[i[0]])
    snames.append(statencodes[codesncodes[i[0]]])
    ratios.append(i[1])

# print(codes)
# print(snames)
# print(ratios)
ttone = {'state-codes': codes}
ttone = pd.DataFrame(ttone)
ttone.to_csv('2-to-1-ratio.csv',index=False)
