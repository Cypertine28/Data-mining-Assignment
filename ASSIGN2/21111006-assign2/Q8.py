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
totmp1=list(popc['Males-L2'])
totfp1=list(popc['Females-L2'])
totmp2=list(popc['Males-L3'])
totfp2=list(popc['Females-L3'])
state_code1=popc["state"].unique()
names=list(popc["Area name"])
ageg=list(popc["Age-group"])
sm2={}
sf2={}
sm3={}
sf3={}
sm1={}
sf1={}
k=0
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j]=="Total"  and ageg[j]!="Total" and ageg[j]!='Age not stated')]
    li1=[]
    li2=[]
    li3=[]
    li4=[]
    for j in idx:
        li1.append(totmp1[j])
        li2.append(totfp1[j])
        li3.append(totmp2[j])
        li4.append(totfp2[j])
    sm2[k]=li1
    sf2[k]=li2
    sm3[k]=li3
    sf3[k]=li4
    k+=1

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
totmp=list(popc['Males-t'])
totfp=list(popc['Females-t'])
state_code1=popc["state code"].unique()
names=list(popc["Area name"])
ageg=list(popc["age-group"])
li1=['5-9',
 '10-14',
 '15-19',
 '20-24',
 '25-29',
 '30-49',
 '50-69',
 '70+']

li1=popc["age-group"].unique()
li1=li1[2:len(li1)-1]
k=0
tot_age_mp={}
tot_age_fp={}
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i  and ageg[j] in li1 ]
    
    valm1,valf1=0,0
    valm2,valf2=0,0
    valm3,valf3=0,0
    for j in idx:
        if ageg[j] in ['30-34', '35-39','40-44', '45-49']:
            valm1+=totmp[j]
            valf1+=totfp[j]
        if ageg[j] in ['50-54', '55-59', '60-64', '65-69']:
            valm2+=totmp[j]
            valf2+=totfp[j]
        if ageg[j] in [ '70-74','75-79', '80+']:
            valm3+=totmp[j]
            valf3+=totfp[j]
    lival1=[]
    lival2=[]
    for  p in idx[:5]:
        lival1.append(totmp[p])
        lival2.append(totfp[p])
    lival1.append(valm1)
    lival2.append(valf1)
    lival1.append(valm2)
    lival2.append(valf2)
    lival1.append(valm3)
    lival2.append(valf3)
    tot_age_mp[i]=lival1
    tot_age_fp[i]=lival2


li1=['5-9',
 '10-14',
 '15-19',
 '20-24',
 '25-29',
 '30-49',
 '50-69',
 '70+']

j=0
li_codes=list(tot_age_mp.keys())
liagmale3,permale3=[],[]
liagmale2,permale2=[],[]
liagmale1,permale1=[],[]
liagfemale3,perfemale3=[],[]
liagfemale2,perfemale2=[],[]
liagfemale1,perfemale1=[],[]
for i in tot_age_mp:
    tli1=tot_age_mp[i]
    tli2=sm2[j]
    tli3=sm3[j]
    #for male
    #for ratio 3
    ansli=[]
    for k in range(len(tli1)):
        ansli.append((tli3[k])/tli1[k])
    ele=max(ansli)
    indx=ansli.index(ele)
    permale3.append(ele)
    liagmale3.append(li1[indx])
    #for ratio 2
    ansli=[]
    for k in range(len(tli1)):
        ansli.append((tli2[k]-tli3[k])/tli1[k])
    ele=max(ansli)
    indx=ansli.index(ele)
    permale2.append(ele)
    liagmale2.append(li1[indx])
    #for ratio 1
    ansli=[]
    for k in range(len(tli1)):
        ansli.append((tli1[k]-tli2[k])/tli1[k])
    ele=max(ansli)
    indx=ansli.index(ele)
    permale1.append(ele)
    liagmale1.append(li1[indx])
    #for female
    tli1=tot_age_fp[i]
    tli2=sf2[j]
    tli3=sf3[j]
    j+=1
    #for ratio 3
    ansli=[]
    for k in range(len(tli1)):
        ansli.append((tli3[k])/tli1[k])
    ele=max(ansli)
    indx=ansli.index(ele)
    perfemale3.append(ele)
    liagfemale3.append(li1[indx])
    #for ratio 2
    ansli=[]
    for k in range(len(tli1)):
        ansli.append((tli2[k]-tli3[k])/tli1[k])
    ele=max(ansli)
    indx=ansli.index(ele)
    perfemale2.append(ele)
    liagfemale2.append(li1[indx])
    #for ratio 1
    ansli=[]
    for k in range(len(tli1)):
        ansli.append((tli1[k]-tli2[k])/tli1[k])
    ele=max(ansli)
    indx=ansli.index(ele)
    perfemale1.append(ele)
    liagfemale1.append(li1[indx])
    
    
ind = {'state/ut':li_codes,"age-group-males":liagmale3,"ratio-males":permale3,"age-group-females":liagfemale3,"ratio-females":perfemale3}
ind = pd.DataFrame(ind)
ind.to_csv('age-gender-a.csv',index=False)

ind = {'state/ut':li_codes,"age-group-males":liagmale2,"ratio-males":permale2,"age-group-females":liagfemale2,"ratio-females":perfemale2}
ind = pd.DataFrame(ind)
ind.to_csv('age-gender-b.csv',index=False)

ind = {'state/ut':li_codes,"age-group-males":liagmale1,"ratio-males":permale1,"age-group-females":liagfemale1,"ratio-females":perfemale1}
ind = pd.DataFrame(ind)
ind.to_csv('age-gender-c.csv',index=False)


















