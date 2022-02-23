import numpy as np
import pandas as pd
import xlrd

pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')
pop_c18 = pd.read_excel(r'DDW-C18-0000.xlsx')
pop_c19 = pd.read_excel(r'DDW-C19-0000.xlsx')
pop_c14 = pd.read_excel(r"DDW-0000C-14.xls")

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
s2={}
s3={}
k=0
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j]=="Total"  and ageg[j]=="Total")]
    for j in idx:
        s2[k]=totp1[j]
        s3[k]=totp2[j]
        k+=1

state_namess=[]
for i in names:
    if i not in state_namess:
        state_namess.append(i)


li1=['5-9',
 '10-14',
 '15-19',
 '20-24',
 '25-29',
 '30-49',
 '50-69',
 '70+']

k=0
age_wise_val={}
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and tru[j]=="Total" and (ageg[j] in li1) ]
    li=[]
    for j in idx:
        li.append(totp2[j])
    age_wise_val[i]=li



popc=pop_c14[6:].rename(columns={"Unnamed: 0":"table name",
                                "Unnamed: 1":"state code",
                                "Unnamed: 2":"distict code",
                                "Unnamed: 3":"Area name",
                                'C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ':"age-group",
                                "Unnamed: 5":"Persons-t",
                                "Unnamed: 6":"Males-t",
                                "Unnamed: 7":"Females-t",
                                "Unnamed: 8":"Persons-r",
                                "Unnamed: 9":"Males-r",
                                "Unnamed: 10":"Females-r",
                                "Unnamed: 11":"Persons-u",
                                "Unnamed: 12":"Males-u",
                                "Unnamed: 13":"Females-u"})
state_listc=list(popc["state code"])
totp=list(popc['Persons-t'])
state_code1=popc["state code"].unique()
names=list(popc["Area name"])
ageg=list(popc["age-group"])

li1=popc["age-group"].unique()
li1=li1[2:len(li1)-1]


k=0
age_wise_tval={}
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i  and ageg[j] in li1 ]
    val1=0
    val2=0
    val3=0
    for j in idx:
#         print(state_namess[k]," ", ageg[j]," ",totp[j])
        if ageg[j] in ['30-34', '35-39','40-44', '45-49']:
            val1+=totp[j]
        if ageg[j] in ['50-54', '55-59', '60-64', '65-69']:
            val2+=totp[j]
        if ageg[j] in [ '70-74','75-79', '80+']:
            val3+=totp[j]
    lival=[]
    for  p in idx[:5]:
        lival.append(totp[p])
    lival.append(val1)
    lival.append(val2)
    lival.append(val3)
    age_wise_tval[i]=lival


li1=['5-9',
 '10-14',
 '15-19',
 '20-24',
 '25-29',
 '30-49',
 '50-69',
 '70+']
k=0
storut=[]
agegrp=[]
perct=[]
for i in age_wise_tval:
    tli1=age_wise_tval[i]
    tli2=age_wise_val[i]
    ansli=[]
    for j in range(len(tli1)):
        ansli.append(tli2[j]/tli1[j])
    ele=max(ansli)
    indx=ansli.index(ele)
    storut.append(str(i))
    agegrp.append(li1[indx])
    perct.append(ele*100)
#     print(i," ",state_namess[k]," ",round(ele*100,2)," ",li1[indx])
    k+=1
ageind = {'state/ut':storut,"age-group":agegrp,"percentage":perct}
ageind = pd.DataFrame(ageind)
ageind.to_csv('age-india.csv',index=False)




