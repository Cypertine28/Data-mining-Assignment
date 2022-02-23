import json
import numpy as np
import pandas as pd
import xlrd

f = open('neighbor-districts-modified.json') 
data = json.load(f)
pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')

districts=pop_data["Name"]
tru=list(pop_data['TRU'])
tot_m=list(pop_data['TOT_M'])
tot_f=list(pop_data['TOT_F'])

dict1={}
dict12={}
dict13={}
for i in data:
    idx=[j for j in range(len(districts)) if districts[j]==i[3:] and tru[j]=='Total']
    for j in idx:
        if tru[j]=='Total':
            dict12[i]=tot_m[j]
            dict13[i]=tot_f[j]
            li=tot_f[j]/tot_m[j]
            dict1[i]=li

vaccine_data=pd.read_csv("vaccination_data_district_wise.csv")
state_to_name={'AN':'Andaman and Nicobar Islands','AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CH':'Chandigarh','CT':'Chhattisgarh','DN':'Dadra and Nagar Haveli and Daman and Diu','DL':'Delhi','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LA':'Ladakh','LD':'Lakshadweep','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Odisha','PY':'Puducherry','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana','TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttarakhand','WB':'West Bengal'}


dist_list=vaccine_data.loc[:,'District_Key']
dist_list1=[]
for i in range(len(dist_list)):
    if dist_list[i] in data:
        dist_list1.append(dist_list[i])
        
        
col=vaccine_data.columns
col=col[6:]
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2020,3,15)
end_dt = date(2021, 8, 14)
list1=[]
for dt in daterange(start_dt, end_dt):
    list1.append(dt.strftime("%d/%m/20%y"))

dict2={}
dict21={}
dict22={}
for i in range(len(dist_list)):
    dlist=list1
    drow=vaccine_data.iloc[i]
    if dist_list[i] not in data:
        continue
    s1=0
    s2=0
    for j in dlist:
        ml=j+".5"
        fl=j+".6"
        if ml not in col:
            s1=0
        else:
            val1=drow[ml]
            if type(val1)==np.nan:
                val1=0
            s1=float(val1)
        if fl not in col:
            s2=0
        else:
            val2=drow[fl]
            if type(val2)==np.nan:
                val2=0
            s2=float(val2)
    dict21[dist_list[i]]=s1
    dict22[dist_list[i]]=s2
    dict2[dist_list[i]]=s2/s1

dist12={}
dist13={}
dist14={}
for i in dict2:
    if i in dict1:
        dist12[i]=dict2[i]
        dist13[i]=dict21[i]
        dist14[i]=dict22[i]

dict2=dist12
dict21=dist13
dict22=dist14        


district_wise_ratio={"districtid":[],"vaccinationratio":[],'populationratio':[],'ratioofratio':[]}
districtid=[]
vacc_ratio=[]
pop_ratio=[]
rofr=[]

for i in dict2:
    if i in dict1:
        districtid.append(i)
        vacc_ratio.append(dict2[i])
        pop_ratio.append(dict1[i])
        rofr.append(dict2[i]/dict1[i])

district_wise_ratio["districtid"]=districtid
district_wise_ratio["vaccinationratio"]=vacc_ratio
district_wise_ratio["populationratio"]=pop_ratio
district_wise_ratio["ratioofratio"]=rofr      
df1=pd.DataFrame.from_dict(district_wise_ratio)
df1=df1.sort_values(by=['ratioofratio'],ascending=True)
df1.to_csv("district-vaccination-population-ratio.csv")

dist_codes=[]
for i in df1['districtid']:
    if i[:2] not in dist_codes:
        dist_codes.append(i[:2])

districts=df1['districtid']
vacc_rat=df1['vaccinationratio']
po_rat=df1['populationratio']
rat=df1['ratioofratio']

week_wise_state={"Stateid":[],"vaccinationratio":[],'populationratio':[],'ratioofratio':[]}
state_id=[]
vacr=[]
prat=[]
rrat=[]

dist_dict1={}
dist_dict2={}
male_op=0
female_op=0
male_ov=0
female_ov=0
for i in dist_codes:
    male_pop=0
    female_pop=0
    for j in dict12:
        if j[:2]==i:
            male_pop+=dict12[j]
    for j in dict13:
        if j[:2]==i:
            female_pop+=dict13[j]
    r1=female_pop/male_pop
    prat.append(female_pop/male_pop)
    male_vacc=0
    female_vacc=0
    for j in dict21:
        if j[:2]==i:
            male_vacc+=dict21[j]
    for j in dict22:
        if j[:2]==i:
            female_vacc+=dict22[j]
    r2=female_vacc/male_vacc
    vacr.append(female_vacc/male_vacc)
    state_id.append(state_to_name[i])
    rrat.append(r2/r1)
    male_op+=male_pop
    female_op+=female_pop
    male_ov+=male_vacc
    female_ov+=female_vacc

week_wise_state["Stateid"]=state_id
week_wise_state["vaccinationratio"]=vacr
week_wise_state["populationratio"]=prat
week_wise_state["ratioofratio"]=rrat 

df2=pd.DataFrame.from_dict(week_wise_state)
df2=df2.sort_values(by=['ratioofratio'],ascending=True)
df2.to_csv("state-vaccination-population-ratio.csv")

overall_rt={"Overall":[],"vaccinationratio":[],'populationratio':[],'ratioofratio':[]}
ov=[]
ov.append(1)
vacr=[]
vacr.append((female_ov/male_ov))
prat=[]
prat.append((female_op/male_op))
rrat=[]
rrat.append(((female_ov/male_ov)/(female_op/male_op)))

# print("vaccination Ratio ",female_ov/male_ov)
# print("Population Ratio ",female_op/male_op)
# print("Ratio of Ratio ",(female_ov/male_ov)/(female_op/male_op))
overall_rt["Overall"]=ov
overall_rt["vaccinationratio"]=vacr
overall_rt["populationratio"]=prat
overall_rt["ratioofratio"]=rrat

df3=pd.DataFrame.from_dict(overall_rt)
df3.to_csv("Overall-vaccination-population-ratio.csv")

