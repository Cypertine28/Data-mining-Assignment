import numpy as np
import pandas as pd
import xlrd

pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')
pop_c18 = pd.read_excel(r'DDW-C18-0000.xlsx')
pop_c19 = pd.read_excel(r'DDW-C19-0000.xlsx')
pop_c8 = pd.read_excel(r"DDW-0000C-08.xlsx")

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
totmp1=list(popc['Males-L2'])
totmp2=list(popc['Males-L3'])
totfp1=list(popc['Females-L2'])
totfp2=list(popc['Females-L3'])
state_code1=popc["state code"].unique()
names=list(popc["Area name"])
litg=list(popc["educational level"])




li1=popc["educational level"].unique()
li1=li1[1:]
li1

tot_m2={}
tot_f2={}
tot_m3={}
tot_f3={}
for i in state_code1:
    idx=[j for j in range(len(state_listc)) if state_listc[j]==i and (tru[j]=="Total"  and litg[j] in li1)]
    tli1=[]
    tli2=[]
    tli3=[]
    tli4=[]
    for k in idx:
        tli1.append(totmp1[k])
        tli2.append(totfp1[k])
        tli3.append(totmp2[k])
        tli4.append(totfp2[k])
    tot_m2[i]=tli1
    tot_f2[i]=tli2
    tot_m3[i]=tli3
    tot_f3[i]=tli4
    

tot_m3

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



state_list=list(popc["state code"])
tru=list(popc["tru"])
ageg=list(popc["age-group"])
illiterate_male=list(popc["Llliterate-Males"])
illiterate_female=list(popc["Llliterate-Females"])
literate_male=list(popc["Literate-Males"])
literate_female=list(popc["Literate-Females"])
libbp_male=list(popc["Literate Below Primary-Males"])
libbp_female=list(popc["Literate Below Primary-Females"])
pribbm_male=list(popc["Primary but below middle-Males"])
pribbm_female=list(popc["Primary but below middle-Females"])
midbbm_male=list(popc["Middle but below matric/secondary-Males"])
midbbm_female=list(popc["Middle but below matric/secondary-Females"])
matsec_male=list(popc["Matric/Secondary-Males"])
matsec_female=list(popc["Matric/Secondary-Females"])
m1_male=list(popc["Higher secondary/Intermediate-Males"])
m1_female=list(popc["Higher secondary/Intermediate-Females"])
m2_male=list(popc["Non-technical diploma-Males"])
m2_female=list(popc["Non-technical diploma-Females"])
m3_male=list(popc["technical diploma-Males"])
m3_female=list(popc["technical diploma-Females"])
gradabv_male=list(popc["Graduate & above-Males"])
gradabv_female=list(popc["Graduate & above-Females"])
state_code1=popc["state code"].unique()

state_dict_male={}
state_dict_female={}
for i in state_code1:
    idx=[j for j in range(len(state_list)) if state_list[j]==i and ageg[j]=="All ages"  and tru[j]=="Total"]

    li=[]
    idx=idx[0]
    li.append(illiterate_male[idx])
    li.append(literate_male[idx])
    li.append(libbp_male[idx])
    li.append(pribbm_male[idx])
    li.append(midbbm_male[idx])
    li.append(matsec_male[idx]+m1_male[idx]+m2_male[idx]+m3_male[idx])
    li.append(gradabv_male[idx])
    
    state_dict_male[i]=li
    li=[]
    li.append(illiterate_female[idx])
    li.append(literate_female[idx])
    li.append(libbp_female[idx])
    li.append(pribbm_female[idx])
    li.append(midbbm_female[idx])
    li.append(matsec_female[idx]+m1_female[idx]+m2_female[idx]+m3_female[idx])
    li.append(gradabv_female[idx])
    
    state_dict_female[i]=li

cat_list=['Illiterate', 'Literate', 'Literate but below primary',
       'Primary but below middle', 'Middle but below matric/secondary',
       'Matric/Secondary but below graduate', 'Graduate and above']


j=0
li_codes=list(state_dict_male.keys())
lgmale3,permale3=[],[]
lgmale2,permale2=[],[]
lgmale1,permale1=[],[]
lgfemale3,perfemale3=[],[]
lgfemale2,perfemale2=[],[]
lgfemale1,perfemale1=[],[]
for i in state_dict_male:
    #for male
    li1=state_dict_male[i]
    li2=tot_m2[i]
    li3=tot_m3[i]
    #for ratio 3
    li=[]
    for k in range(len(li1)):
        li.append((li3[k])/li1[k])
    ele=max(li)
    idx=li.index(ele)
    lgmale3.append(cat_list[idx])
    permale3.append(ele)
    
    #for ratio 2
    li=[]
    for k in range(len(li1)):
        li.append((li2[k]-li3[k])/li1[k])
    ele=max(li)
    idx=li.index(ele)
    lgmale2.append(cat_list[idx])
    permale2.append(ele)
    
    #for ratio 1
    li=[]
    for k in range(len(li1)):
        li.append((li1[k]-li2[k])/li1[k])
    ele=max(li)
    idx=li.index(ele)
    lgmale1.append(cat_list[idx])
    permale1.append(ele)
    
    #for female
    li1=state_dict_female[i]
    li2=tot_f2[i]
    li3=tot_f3[i]
    #for ratio 3
    li=[]
    for k in range(len(li1)):
        li.append((li3[k])/li1[k])
    ele=max(li)
    idx=li.index(ele)
    lgfemale3.append(cat_list[idx])
    perfemale3.append(ele)
    #for ratio 2
    li=[]
    for k in range(len(li1)):
        li.append((li2[k]-li3[k])/li1[k])
    ele=max(li)
    idx=li.index(ele)
    lgfemale2.append(cat_list[idx])
    perfemale2.append(ele)
    #for ratio 1
    li=[]
    for k in range(len(li1)):
        li.append((li1[k]-li2[k])/li1[k])
    ele=max(li)
    idx=li.index(ele)
    lgfemale1.append(cat_list[idx])
    perfemale1.append(ele)
    
    
ind = {'state/ut':li_codes,"literacy-group-males":lgmale3,"ratio-males":permale3,"literacy-group-females":lgfemale3,"ratio-females":perfemale3}
ind = pd.DataFrame(ind)
ind.to_csv('literacy-gender-a.csv',index=False)

ind = {'state/ut':li_codes,"literacy-group-males":lgmale2,"ratio-males":permale2,"literacy-group-females":lgfemale2,"ratio-females":perfemale2}
ind = pd.DataFrame(ind)
ind.to_csv('literacy-gender-b.csv',index=False)

ind = {'state/ut':li_codes,"literacy-group-males":lgmale1,"ratio-males":permale1,"literacy-group-females":lgfemale1,"ratio-females":perfemale1}
ind = pd.DataFrame(ind)
ind.to_csv('literacy-gender-c.csv',index=False)




