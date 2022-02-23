import numpy as np
import pandas as pd
import xlrd

pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')
pop_c18 = pd.read_excel(r'DDW-C18-0000.xlsx')
pop_c19 = pd.read_excel(r'DDW-C19-0000.xlsx')
pop_c8 = pd.read_excel(r"DDW-0000C-08.xlsx")

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



popc=pop_c19[5:].rename(columns={"C-19 POPULATION BY BILINGUALISM, TRILINGUALISM, EDUCATIONAL LEVEL AND SEX":"state code",
                                "Unnamed: 1":"District code",
                                "Unnamed: 2":"Area name",
                                "Unnamed: 3":"tru",
                                "Unnamed: 4":"educational level",
                                "Unnamed: 5":"Persons-L2",
                                "Unnamed: 6":"Males-L2",
                                "Unnamed: 7":"Females-L2",
                                "Unnamed: 8":"Persons-L3",
                                "Unnamed: 9":"Males-L3",
                                "Unnamed: 10":"Females-L3",}).dropna()
state_listc=list(popc["state code"])
tru=list(popc["tru"])
totp1=list(popc['Persons-L2'])
totp2=list(popc['Persons-L3'])
state_code1=popc["state code"].unique()
names=list(popc["Area name"])
litg=list(popc["educational level"])


state_namess=[]
for i in names:
    if i not in state_namess:
        state_namess.append(i)

li1=popc["educational level"].unique()
li1=li1[1:]


state_dict1={}
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j]=="Total"  and litg[j] in li1)]
    li=[]
    for j in idx:
        li.append(totp2[j])
    state_dict1[i]=li
    #print(li)
#     ele=max(li)
#     indx=li.index(ele)+1
#     print(i," ",state_namess[k]," ",li1[indx]," ",round(ele/total*100,2))
#     k+=1

popc=pop_c8[6:].rename(columns={"Unnamed: 0":"table name",
                                "Unnamed: 1":"state code",
                                "Unnamed: 2":"distict code",
                                "Unnamed: 3":"Area name",
                                "Unnamed: 4":"tru",
                                'C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011':"age-group",
                                "Unnamed: 6":"total-person",
                                "Unnamed: 7":"total-Males",
                                "Unnamed: 8":"total-Females",
                                "Unnamed: 9":"Llliterate-Persons",
                                "Unnamed: 10":"Llliterate-Males",
                                "Unnamed: 11":"Llliterate-Females",
                                "Unnamed: 12":"Literate-Persons",
                                "Unnamed: 13":"Literate-Males",
                                "Unnamed: 14":"Literate-Females",
                                "Unnamed: 15":"Literate without educational level-Persons",
                                "Unnamed: 16":"Literate without educational level-Males",
                                "Unnamed: 17":"Literate without educational level-Females",
                                "Unnamed: 18":"Literate Below Primary-Persons",
                                "Unnamed: 19":"Literate Below Primary-Males",
                                "Unnamed: 20":"Literate Below Primary-Females",
                                "Unnamed: 21":"Primary but below middle-Persons",
                                "Unnamed: 22":"Primary but below middle-Males",
                                "Unnamed: 23":"Primary but below middle-Females",
                                "Unnamed: 24":"Middle but below matric/secondary-Persons",
                                "Unnamed: 25":"Middle but below matric/secondary-Males",
                                "Unnamed: 26":"Middle but below matric/secondary-Females",
                                "Unnamed: 27":"Matric/Secondary-Persons",
                                "Unnamed: 28":"Matric/Secondary-Males",
                                "Unnamed: 29":"Matric/Secondary-Females",
                                "Unnamed: 30":"Higher secondary/Intermediate-Persons",
                                "Unnamed: 31":"Higher secondary/Intermediate-Males",
                                "Unnamed: 32":"Higher secondary/Intermediate-Females",
                                "Unnamed: 33":"Non-technical diploma-Persons",
                                "Unnamed: 34":"Non-technical diploma-Males",
                                "Unnamed: 35":"Non-technical diploma-Females",
                                "Unnamed: 36":"technical diploma-Persons",
                                "Unnamed: 37":"technical diploma-Males",
                                "Unnamed: 38":"technical diploma-Females",
                                "Unnamed: 39":"Graduate & above-Persons",
                                "Unnamed: 40":"Graduate & above-Males",
                                "Unnamed: 41":"Graduate & above-Females",
                                "Unnamed: 42":"Unclassified-Persons",
                                "Unnamed: 43":"Unclassified-Males",
                                "Unnamed: 44":"Unclassified-Females",
                                })


# 'Illiterate', 'Literate', 'Literate but below primary',
#        'Primary but below middle', 'Middle but below matric/secondary',
#        'Matric/Secondary but below graduate', 'Graduate and above'

state_list=list(popc["state code"])
tru=list(popc["tru"])
ageg=list(popc["age-group"])
illiterate=list(popc["Llliterate-Persons"])
literate=list(popc["Literate-Persons"])
libbp=list(popc["Literate Below Primary-Persons"])
pribbm=list(popc["Primary but below middle-Persons"])
midbbm=list(popc["Middle but below matric/secondary-Persons"])
matsec=list(popc["Matric/Secondary-Persons"])
m1=list(popc["Higher secondary/Intermediate-Persons"])
m2=list(popc["Non-technical diploma-Persons"])
m3=list(popc["technical diploma-Persons"])
gradabv=list(popc["Graduate & above-Persons"])
state_code1=popc["state code"].unique()

state_dict2={}
for i in state_code1:
    idx=[j for j in range(len(state_list)) if state_list[j]==i and ageg[j]=="All ages"  and tru[j]=="Total"]
    li=[]
    idx=idx[0]
    li.append(illiterate[idx])
    li.append(literate[idx])
    li.append(libbp[idx])
    li.append(pribbm[idx])
    li.append(midbbm[idx])
    li.append(matsec[idx]+m1[idx]+m2[idx]+m3[idx])
    li.append(gradabv[idx])
    #print(li)
    state_dict2[i]=li

cat_list=['Illiterate', 'Literate', 'Literate but below primary',
       'Primary but below middle', 'Middle but below matric/secondary',
       'Matric/Secondary but below graduate', 'Graduate and above']
k=0
storut=[]
lit1=[]
perct=[]
for i in state_dict1:
    li1=state_dict1[i]
    li2=state_dict2[i]
    li=[]
    for j in range(len(li1)):
        li.append(li1[j]/li2[j])
    ele=max(li)
    indx=li.index(ele)
    storut.append(i)
    lit1.append(cat_list[indx])
    perct.append(ele*100)
    #print(i," ",state_namess[k]," ",cat_list[indx]," ",round(ele*100,2))
    k+=1
litind = {'state/ut':storut,"literacy-group":lit1,"percentage":perct}
litind = pd.DataFrame(litind)
litind.to_csv('literacy-india.csv',index=False)


