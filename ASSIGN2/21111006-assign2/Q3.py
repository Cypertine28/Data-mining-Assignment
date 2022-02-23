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
tot_p=list(pop_data['TOT_P'])
name=list(pop_data["Name"])
sp_dict1={}
sp_dict2={}
for i in state_codes:
    idx=[j for j in range(len(state_list)) if state_list[j]==i and (level[j]=="STATE" or level[j]=="India") and tru[j] in ["Rural","Urban"]]
    sp_dict1[i]=tot_p[idx[0]]
    sp_dict2[i]=tot_p[idx[1]]
    




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
k=0
tot_rural2={}
tot_urban2={}
tot_rural3={}
tot_urban3={}
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j] in ["Rural","Urban"]  and ageg[j]=="Total")]
    tot_rural2[k]=totp1[idx[0]]
    tot_urban2[k]=totp1[idx[1]]
    tot_rural3[k]=totp2[idx[0]]
    tot_urban3[k]=totp2[idx[1]]
    k+=1



urban={}
rural={}
urbl1=[]
rurl1=[]
urbl2=[]
rurl2=[]
urbl3=[]
rurl3=[]
pvall=[]
for i in tot_rural2:
    rat3=tot_urban3[i]/tot_rural3[i]
    rat2=(tot_urban2[i]-tot_urban3[i])/(tot_rural2[i]-tot_rural3[i])
    rat1=(sp_dict2[i]-tot_urban2[i])/(sp_dict1[i]-tot_rural2[i])
    pop_mean=sp_dict2[i]/sp_dict1[i]
    li1=[]
    li1.append(rat1)
    li1.append(rat2)
    li1.append(rat3)
    t, p = stats.ttest_1samp(li1, pop_mean)
    # print(state_code1[i]," ",p)
    pvall.append(p)
    urbl1.append((tot_urban3[i]/sp_dict2[i])*100)
    rurl1.append((tot_rural3[i]/sp_dict1[i])*100)
    urbl2.append(((tot_urban2[i]-tot_urban3[i])/sp_dict2[i])*100)
    rurl2.append(((tot_rural2[i]-tot_rural3[i])/sp_dict1[i])*100)
    urbl3.append(((sp_dict2[i]-tot_urban2[i])/sp_dict2[i])*100)
    rurl3.append(((sp_dict1[i]-tot_rural2[i])/sp_dict1[i])*100)

geograind = {'state-code':state_code1,'urban-percentage':urbl1,"rural-percentage":rurl1,"p-value":pvall}
geograind = pd.DataFrame(geograind)
geograind.to_csv('geography-india-c.csv',index=False)

geograind = {'state-code':state_code1,'urban-percentage':urbl2,"rural-percentage":rurl2,"p-value":pvall}
geograind = pd.DataFrame(geograind)
geograind.to_csv('geography-india-b.csv',index=False)

geograind = {'state-code':state_code1,'urban-percentage':urbl3,"rural-percentage":rurl3,"p-value":pvall}
geograind = pd.DataFrame(geograind)
geograind.to_csv('geography-india-a.csv',index=False)


