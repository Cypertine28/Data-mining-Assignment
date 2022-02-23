import numpy as np
import pandas as pd
import xlrd

pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')
#central
CG_data =  pd.read_excel(r'All regions datasets/CENTRAL/CG.XLSX')
MP_data =  pd.read_excel(r'All regions datasets/CENTRAL/MP.XLSX')
UP_data =  pd.read_excel(r'All regions datasets/CENTRAL/UP.XLSX')
#east
BH_data =  pd.read_excel(r'All regions datasets/EAST/BH.XLSX')
JH_data =  pd.read_excel(r'All regions datasets/EAST/JH.XLSX')
OR_data =  pd.read_excel(r'All regions datasets/EAST/OR.XLSX')
WB_data =  pd.read_excel(r'All regions datasets/EAST/WB.XLSX')
#north
chandigarh_data =  pd.read_excel(r'All regions datasets/NORTH/CHANDIGARH.XLSX')
DELHI_data =  pd.read_excel(r'All regions datasets/NORTH/DELHI.XLSX')
HP_data =  pd.read_excel(r'All regions datasets/NORTH/HP.XLSX')
HR_data =  pd.read_excel(r'All regions datasets/NORTH/HR.XLSX')
JK_data =  pd.read_excel(r'All regions datasets/NORTH/JK.XLSX')
PN_data =  pd.read_excel(r'All regions datasets/NORTH/PN.XLSX')
UK_data =  pd.read_excel(r'All regions datasets/NORTH/UK.XLSX')
#north-east
ANDM_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/Andaman & Nicobar Islands.XLSX')
AR_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/AR.XLSX')
AS_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/AS.XLSX')
MG_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/MG.XLSX')
MN_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/MN.XLSX')
MZ_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/MZ.XLSX')
NG_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/NG.XLSX')
SK_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/SK.XLSX')
TR_data =  pd.read_excel(r'All regions datasets/NORTH-EAST/TR.XLSX')
#south
AP_data =  pd.read_excel(r'All regions datasets/SOUTH/AP.XLSX')
KL_data =  pd.read_excel(r'All regions datasets/SOUTH/KL.XLSX')
KT_data =  pd.read_excel(r'All regions datasets/SOUTH/KT.XLSX')
LAKSHYD_data =  pd.read_excel(r'All regions datasets/SOUTH/Lakshadweep.XLSX')
PUDUCH_data =  pd.read_excel(r'All regions datasets/SOUTH/Puducherry.XLSX')
TN_data =  pd.read_excel(r'All regions datasets/SOUTH/TN.XLSX')
#west
DNH_data =  pd.read_excel(r'All regions datasets/WEST/Dadra & Nagar Haveli.XLSX')
DND_data =  pd.read_excel(r'All regions datasets/WEST/Daman & Diu.XLSX')
GJ_data =  pd.read_excel(r'All regions datasets/WEST/GJ.XLSX')
GOA_data =  pd.read_excel(r'All regions datasets/WEST/GOA.XLSX')
MH_data =  pd.read_excel(r'All regions datasets/WEST/MH.XLSX')
RJ_data =  pd.read_excel(r'All regions datasets/WEST/RJ.XLSX')


Final_dict1={}
Final_dict2={}

# North region

Final_lang_dict={}
final={}
popc1=chandigarh_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc1["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc1["name-L1"])
lang_pop=list(popc1["person-L1"])

for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]

lang_name=[item for item in list(popc1["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc1["name-L2"])
lang_pop1=list(popc1["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc1["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc1["name-L3"])
lang_pop2=list(popc1["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

#Delhi
popc2=DELHI_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc2["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc2["name-L1"])
lang_pop=list(popc2["person-L1"])

for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]   


lang_name=[item for item in list(popc2["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc2["name-L2"])
lang_pop1=list(popc2["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc2["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc2["name-L3"])
lang_pop2=list(popc2["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

#HP
popc3=HP_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc3["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc3["name-L1"])
lang_pop=list(popc3["person-L1"])

for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]  


lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]            
#HR            
popc4=HR_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc4["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc4["name-L1"])
lang_pop=list(popc4["person-L1"])  


for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]   


lang_name=[item for item in list(popc4["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc4["name-L2"])
lang_pop1=list(popc4["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc4["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc4["name-L3"])
lang_pop2=list(popc4["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]          

#JK
popc5=JK_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc5["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc5["name-L1"])
lang_pop=list(popc5["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]   


lang_name=[item for item in list(popc5["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc5["name-L2"])
lang_pop1=list(popc5["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc5["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc5["name-L3"])
lang_pop2=list(popc5["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]                    

#PN
popc6=PN_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc6["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc6["name-L1"])
lang_pop=list(popc6["person-L1"])


for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]   


lang_name=[item for item in list(popc6["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc6["name-L2"])
lang_pop1=list(popc6["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc6["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc6["name-L3"])
lang_pop2=list(popc6["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]                    


            
#UK
popc7=UK_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc7["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc7["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc7["name-L1"])
lang_pop=list(popc7["person-L1"])


for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]   


lang_name=[item for item in list(popc7["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc7["name-L2"])
lang_pop1=list(popc7["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc7["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc7["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc7["name-L3"])
lang_pop2=list(popc7["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]                    

            
dict1=dict(sorted(Final_lang_dict.items(), key=lambda item: item[1],reverse=True))
j=0
list1=[]
for i in dict1:
    if j==3:
        break
    list1.append(i)
    j+=1
dict1=dict(sorted(final.items(), key=lambda item: item[1],reverse=True))
j=0
list2=[]
for i in dict1:
    if j==3:
        break
    list2.append(i)
    j+=1           
# print(list1)
# print(list2)
Final_dict1["North"]=list1
Final_dict2["North"]=list2

# West region

#west
# DNH_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/WEST/Dadra & Nagar Haveli.XLSX')
# DND_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/WEST/Daman & Diu.XLSX')
# GJ_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/WEST/GJ.XLSX')
# GOA_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/WEST/GOA.XLSX')
# MH_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/WEST/MH.XLSX')
# RJ_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/WEST/RJ.XLSX')
final={}
Final_lang_dict={}
popc1=DNH_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc1["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc1["name-L1"])
lang_pop=list(popc1["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc1["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc1["name-L2"])
lang_pop1=list(popc1["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc1["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc1["name-L3"])
lang_pop2=list(popc1["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]


#DND
popc2=DND_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc2["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc2["name-L1"])
lang_pop=list(popc2["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc2["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc2["name-L2"])
lang_pop1=list(popc2["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc2["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc2["name-L3"])
lang_pop2=list(popc2["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

#GJ
popc3=GJ_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc3["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc3["name-L1"])
lang_pop=list(popc3["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
            
#GOA
popc4=GOA_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc4["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc4["name-L1"])
lang_pop=list(popc4["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc4["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc4["name-L2"])
lang_pop1=list(popc4["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc4["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc4["name-L3"])
lang_pop2=list(popc4["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
#MH   
popc5=MH_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc5["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc5["name-L1"])
lang_pop=list(popc5["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc5["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc5["name-L2"])
lang_pop1=list(popc5["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc5["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc5["name-L3"])
lang_pop2=list(popc5["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
#RJ
popc6=RJ_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc6["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc6["name-L1"])
lang_pop=list(popc6["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc6["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc6["name-L2"])
lang_pop1=list(popc6["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc6["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc6["name-L3"])
lang_pop2=list(popc6["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
dict1=dict(sorted(Final_lang_dict.items(), key=lambda item: item[1],reverse=True))
j=0
list1=[]
for i in dict1:
    if j==3:
        break
    list1.append(i)
    j+=1
dict1=dict(sorted(final.items(), key=lambda item: item[1],reverse=True))
j=0
list2=[]
for i in dict1:
    if j==3:
        break
    list2.append(i)
    j+=1           
# print(list1)
# print(list2)
Final_dict1["West"]=list1
Final_dict2["West"]=list2

# Central Region

Final_lang_dict={}
final={}
popc1=CG_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})


lang_codes=[item for item in list(popc1["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc1["name-L1"])
lang_pop=list(popc1["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc1["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc1["name-L2"])
lang_pop1=list(popc1["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc1["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc1["name-L3"])
lang_pop2=list(popc1["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
            
# MP
popc2=MP_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc2["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc2["name-L1"])
lang_pop=list(popc2["person-L1"])


for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc2["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc2["name-L2"])
lang_pop1=list(popc2["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc2["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc2["name-L3"])
lang_pop2=list(popc2["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
            
#UP
popc3=UP_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc3["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc3["name-L1"])
lang_pop=list(popc3["person-L1"])

for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

dict1=dict(sorted(Final_lang_dict.items(), key=lambda item: item[1],reverse=True))
j=0
list1=[]
for i in dict1:
    if j==3:
        break
    list1.append(i)
    j+=1
dict1=dict(sorted(final.items(), key=lambda item: item[1],reverse=True))
j=0
list2=[]
for i in dict1:
    if j==3:
        break
    list2.append(i)
    j+=1           
# print(list1)
# print(list2)
Final_dict1["Central"]=list1
Final_dict2["Central"]=list2

# EAST Region

# BH_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/EAST/BH.XLSX')
# JH_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/EAST/JH.XLSX')
# OR_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/EAST/OR.XLSX')
# WB_data =  pd.read_excel(r'C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM/EAST/WB.XLSX')
popc1=BH_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})


lang_codes=[item for item in list(popc1["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc1["name-L1"])
lang_pop=list(popc1["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc1["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc1["name-L2"])
lang_pop1=list(popc1["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc1["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc1["name-L3"])
lang_pop2=list(popc1["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

#JH            
popc2=JH_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc2["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc2["name-L1"])
lang_pop=list(popc2["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc2["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc2["name-L2"])
lang_pop1=list(popc2["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc2["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc2["name-L3"])
lang_pop2=list(popc2["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
#OR
popc3=OR_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc3["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc3["name-L1"])
lang_pop=list(popc3["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

popc4=WB_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc4["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc4["name-L1"])
lang_pop=list(popc4["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc4["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc4["name-L2"])
lang_pop1=list(popc4["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc4["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc4["name-L3"])
lang_pop2=list(popc4["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
dict1=dict(sorted(Final_lang_dict.items(), key=lambda item: item[1],reverse=True))
j=0
list1=[]
for i in dict1:
    if j==3:
        break
    list1.append(i)
    j+=1
dict1=dict(sorted(final.items(), key=lambda item: item[1],reverse=True))
j=0
list2=[]
for i in dict1:
    if j==3:
        break
    list2.append(i)
    j+=1           
# print(list1)
# print(list2)
Final_dict1["East"]=list1
Final_dict2["East"]=list2

# South Region

final={}
Final_lang_dict={}
popc1=AP_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})


lang_codes=[item for item in list(popc1["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc1["name-L1"])
lang_pop=list(popc1["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc1["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc1["name-L2"])
lang_pop1=list(popc1["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc1["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc1["name-L3"])
lang_pop2=list(popc1["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]


popc2=KL_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc2["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc2["name-L1"])
lang_pop=list(popc2["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc2["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc2["name-L2"])
lang_pop1=list(popc2["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc2["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc2["name-L3"])
lang_pop2=list(popc2["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

popc3=KT_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc3["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc3["name-L1"])
lang_pop=list(popc3["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
#LAK
popc4=LAKSHYD_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc4["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc4["name-L1"])
lang_pop=list(popc4["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

popc5=PUDUCH_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc5["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc5["name-L1"])
lang_pop=list(popc5["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc5["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc5["name-L2"])
lang_pop1=list(popc5["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc5["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc5["name-L3"])
lang_pop2=list(popc5["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
popc6=TN_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc6["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc6["name-L1"])
lang_pop=list(popc6["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc6["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc6["name-L2"])
lang_pop1=list(popc6["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc6["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc6["name-L3"])
lang_pop2=list(popc6["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
dict1=dict(sorted(Final_lang_dict.items(), key=lambda item: item[1],reverse=True))
j=0
list1=[]
for i in dict1:
    if j==3:
        break
    list1.append(i)
    j+=1
dict1=dict(sorted(final.items(), key=lambda item: item[1],reverse=True))
j=0
list2=[]
for i in dict1:
    if j==3:
        break
    list2.append(i)
    j+=1           
# print(list1)
# print(list2)
Final_dict1["South"]=list1
Final_dict2["South"]=list2

# North east

final={}
Final_lang_dict={}
popc1=ANDM_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})


lang_codes=[item for item in list(popc1["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc1["name-L1"])
lang_pop=list(popc1["person-L1"])

for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc1["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc1["name-L2"])
lang_pop1=list(popc1["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc1["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc1["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc1["name-L3"])
lang_pop2=list(popc1["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]


popc2=AR_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc2["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc2["name-L1"])
lang_pop=list(popc2["person-L1"])

for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc2["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc2["name-L2"])
lang_pop1=list(popc2["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc2["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc2["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc2["name-L3"])
lang_pop2=list(popc2["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

popc3=AS_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc3["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc3["name-L1"])
lang_pop=list(popc3["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
popc4=MG_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc4["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc4["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc4["name-L1"])
lang_pop=list(popc4["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc3["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc3["name-L2"])
lang_pop1=list(popc3["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc3["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc3["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc3["name-L3"])
lang_pop2=list(popc3["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

popc5=MN_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc5["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc5["name-L1"])
lang_pop=list(popc5["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc5["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc5["name-L2"])
lang_pop1=list(popc5["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc5["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc5["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc5["name-L3"])
lang_pop2=list(popc5["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
popc6=MZ_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc6["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc6["name-L1"])
lang_pop=list(popc6["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc6["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc6["name-L2"])
lang_pop1=list(popc6["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc6["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc6["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc6["name-L3"])
lang_pop2=list(popc6["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
#NG
popc7=NG_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc7["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc7["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc7["name-L1"])
lang_pop=list(popc7["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc7["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc7["name-L2"])
lang_pop1=list(popc7["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc7["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc7["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc7["name-L3"])
lang_pop2=list(popc7["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]

popc8=SK_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc8["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc8["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc8["name-L1"])
lang_pop=list(popc8["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc8["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc8["name-L2"])
lang_pop1=list(popc8["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc8["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc8["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc8["name-L3"])
lang_pop2=list(popc8["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
            
            
popc9=TR_data[5:].rename(columns={"C-17 POPULATION BY BILINGUALISM AND TRILINGUALISM":"state code",
                                "Unnamed: 1":"State name",
                                "Unnamed: 2":"code-L1",
                                "Unnamed: 3":"name-L1",
                                "Unnamed: 4":"person-L1",
                                "Unnamed: 5":"male-L1",
                                "Unnamed: 6":"female-L1",
                                "Unnamed: 7":"code-L2",
                                "Unnamed: 8":"name-L2",
                                "Unnamed: 9":"person-L2",
                                "Unnamed: 10":"male-L2",
                                "Unnamed: 11":"female-L2",
                                "Unnamed: 12":"code-L3",
                                "Unnamed: 13":"name-L3",
                                "Unnamed: 14":"person-L3",
                                "Unnamed: 15":"male-L3",
                                "Unnamed: 16":"female-L3"})
lang_codes=[item for item in list(popc9["code-L1"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc9["name-L1"].unique()) if type(item) !=float]
lang_list=list(popc9["name-L1"])
lang_pop=list(popc9["person-L1"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list)) if i==lang_list[j]]
    if i in Final_lang_dict:
        Final_lang_dict[i]+=lang_pop[idx[0]]
    else:
        Final_lang_dict[i]=lang_pop[idx[0]]
    if i in final:
        final[i]+=lang_pop[idx[0]]
    else:
        final[i]=lang_pop[idx[0]]
lang_name=[item for item in list(popc9["name-L2"].unique()) if type(item) !=float]
lang_list1=list(popc9["name-L2"])
lang_pop1=list(popc9["person-L2"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list1)) if i==lang_list1[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop1[j]
        else:
            Final_lang_dict[i]=lang_pop1[j]
                
lang_codes=[item for item in list(popc9["code-L3"].unique()) if type(item) !=float]
lang_name=[item for item in list(popc9["name-L3"].unique()) if type(item) !=float]
lang_list2=list(popc9["name-L3"])
lang_pop2=list(popc9["person-L3"])
for i in lang_name:
    idx=[j  for j in range(len(lang_list2)) if i==lang_list2[j]]
    for j in idx:
        if i in Final_lang_dict:
            Final_lang_dict[i]+=lang_pop2[j]
        else:
            Final_lang_dict[i]=lang_pop2[j]
dict1=dict(sorted(Final_lang_dict.items(), key=lambda item: item[1],reverse=True))
j=0
list1=[]
for i in dict1:
    if j==3:
        break
    list1.append(i)
    j+=1
dict1=dict(sorted(final.items(), key=lambda item: item[1],reverse=True))
j=0
list2=[]
for i in dict1:
    if j==3:
        break
    list2.append(i)
    j+=1           
# print(list1)
# print(list2)
Final_dict1["North-East"]=list1
Final_dict2["North-East"]=list2

regl=[]
l1=[]
l2=[]
l3=[]
Final_dict1=dict(sorted(Final_dict1.items(),key=lambda item: item[0]))
for i in Final_dict1:
    li=Final_dict1[i]
    regl.append(i)
    l1.append(li[0])
    l2.append(li[1])
    l3.append(li[2])
regind= {'region':regl,"language-1":l1,"language-2":l2,"language-3":l3}
regind = pd.DataFrame(regind)
regind.to_csv('region-india-b.csv',index=False)


regl=[]
l1=[]
l2=[]
l3=[]
Final_dict2=dict(sorted(Final_dict2.items(),key=lambda item: item[0]))
for i in Final_dict2:
    li=Final_dict2[i]
    regl.append(i)
    l1.append(li[0])
    l2.append(li[1])
    l3.append(li[2])
regind= {'region':regl,"language-1":l1,"language-2":l2,"language-3":l3}
regind = pd.DataFrame(regind)
regind.to_csv('region-india-a.csv',index=False)





























