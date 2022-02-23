import numpy as np
import pandas as pd
import scipy.stats as stats
pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')
pop_c18 = pd.read_excel(r'DDW-C18-0000.xlsx')
pop_c19 = pd.read_excel(r'DDW-C19-0000.xlsx')
pop_c14 = pd.read_excel(r"DDW-0000C-14.xls")



state_codes=set(pop_data["State"])
state_list=list(pop_data["State"])
level=list(pop_data["Level"])
tru=list(pop_data['TRU'])
tot_pm=list(pop_data['TOT_M'])
tot_pf=list(pop_data['TOT_F'])
name=list(pop_data["Name"])
sp_dict1={}
sp_dict2={}
for i in state_codes:
    idx=[j for j in range(len(state_list)) if state_list[j]==i and (level[j]=="STATE" or level[j]=="India") and tru[j]=="Total"]
    for j in idx:
        sp_dict1[i]=tot_pm[j]
        sp_dict2[i]=tot_pf[j]



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
k=0
smale2={}
sfemale2={}
smale3={}
sfemale3={}
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j]=="Total"  and ageg[j]=="Total")]
    for j in idx:
        smale2[k]=totmp1[j]
        sfemale2[k]=totfp1[j]
        smale3[k]=totmp2[j]
        sfemale3[k]=totfp2[j]
        k+=1

state_namess=[]
for i in names:
    if i not in state_namess:
        state_namess.append(i)


fmale={}
ffemale={}
male1=[]
female1=[]
male2=[]
female2=[]
male3=[]
female3=[]
pval1=[]
stcodes=state_code1
for i in smale2:
    rat3=(smale3[i])/(sfemale3[i])
    rat2=(smale2[i]-smale3[i])/(sfemale2[i]-sfemale3[i])
    rat1=(sp_dict1[i]-smale2[i])/(sp_dict2[i]-sfemale2[i])
    pop_mean=sp_dict1[i]/sp_dict2[i]
    li1=[]
    li1.append(rat3)
    li1.append(rat2)
    li1.append(rat1)
#     print(i," ",li1)
    t, p = stats.ttest_1samp(li1, pop_mean)
    # print(state_code1[i]," ",p)
    m3=smale3[i]/sp_dict1[i]*100
    f3=sfemale3[i]/sp_dict2[i]*100
    m2=((smale2[i]-smale3[i])/sp_dict1[i])*100
    f2=((sfemale2[i]-sfemale3[i])/sp_dict2[i])*100
    m1=((sp_dict1[i]-smale2[i])/sp_dict1[i])*100
    f1=((sp_dict2[i]-sfemale2[i])/sp_dict2[i])*100
    male3.append(m3)
    female3.append(f3)
    male2.append(m2)
    female2.append(f2)
    male1.append(m1)
    female1.append(f1)
    pval1.append(p)
    



genderind = {'state-code':stcodes,'male-percentage':male1,"female-percentage":female1,"p-value":pval1}
genderind = pd.DataFrame(genderind)
genderind.to_csv('gender-india-a.csv',index=False)

genderind = {'state-code':stcodes,'male-percentage':male2,"female-percentage":female2,"p-value":pval1}
genderind = pd.DataFrame(genderind)
genderind.to_csv('gender-india-b.csv',index=False)
genderind = {'state-code':stcodes,'male-percentage':male3,"female-percentage":female3,"p-value":pval1}
genderind = pd.DataFrame(genderind)
genderind.to_csv('gender-india-c.csv',index=False)

