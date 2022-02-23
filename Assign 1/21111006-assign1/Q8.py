import json
import numpy as np
import pandas as pd
import xlrd

f = open('neighbor-districts-modified.json') 
data = json.load(f)

vaccine_data=pd.read_csv("vaccination_data_district_wise.csv")
print(len(vaccine_data))

state_list=vaccine_data.loc[1:,'State']
col=vaccine_data.columns
col=col[6:]
dist_list=vaccine_data.loc[:,'District_Key']

from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2020,3,15)
end_dt = date(2021, 8, 14)
list1=[]
for dt in daterange(start_dt, end_dt):
    list1.append(dt.strftime("%d/%m/20%y"))


dict_district1={}
dict_district2={}
for i in range(len(dist_list)):
    dlist=list1
    drow=vaccine_data.iloc[i]
    if dist_list[i] not in data:
        continue
    dose1_list1=[]
    dose1_list2=[]
    for j in dlist:
        point1=j+".3"
        point2=j+".4"
        if point1 not in col:
            dose1_list1.append(0)
        else:
            if(type(drow[point1])==np.nan):
                dose1_list1.append(0)
            else:
                dose1_list1.append(float(drow[point1])) 
        if point2 not in col:
            dose1_list2.append(0)
        else:
            if(type(drow[point2])==np.nan):
                dose1_list2.append(0)
            else:
                dose1_list2.append(float(drow[point2]))
    dict_district1[dist_list[i]]=(max(dose1_list1))
    dict_district2[dist_list[i]]=(max(dose1_list2))    
        
        



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

di1={}
di2={}
for i in dict_district1:
    if i in dict12:
        di1[i]=dict_district1[i]
    if i in dict13:
        di2[i]=dict_district2[i]

vaccinated={"districtid":[],"vaccinateddose1ratio":[],"vaccinateddose2ratio":[]}
districtid2=[]
vacc_dose1_ratio=[]
vacc_dose2_ratio=[]

for i in di1:
    districtid2.append(i)
    v1=dict13[i]+dict12[i]
    vacc_dose1_ratio.append(di1[i]/v1)
    vacc_dose2_ratio.append(di2[i]/v1)  
    
vaccinated["districtid"]=districtid2
vaccinated["vaccinateddose1ratio"]=vacc_dose1_ratio
vaccinated["vaccinateddose2ratio"]=vacc_dose2_ratio

df1=pd.DataFrame.from_dict(vaccinated)
df1=df1.sort_values(by=['vaccinateddose1ratio'],ascending=True)
df1.to_csv("district-vaccinated-dose-ratio.csv")

dist_codes=[]
for i in df1['districtid']:
    if i[:2] not in dist_codes:
        dist_codes.append(i[:2])

state_to_name={'AN':'Andaman and Nicobar Islands','AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CH':'Chandigarh','CT':'Chhattisgarh','DN':'Dadra and Nagar Haveli and Daman and Diu','DL':'Delhi','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LA':'Ladakh','LD':'Lakshadweep','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Odisha','PY':'Puducherry','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana','TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttarakhand','WB':'West Bengal'}

state_svratio={"Stateid":[],"vaccinateddose1ratio":[],"vaccinateddose2ratio":[]}
state_id=[]
vac_r1=[]
vac_r2=[]

d1_val=0
d2_val=0
total_pop=0
for i in dist_codes:
    d1=0
    d2=0
    for j in di1:
        if j[:2]==i:
            d1+=di1[j]
    for j in di2:
        if j[:2]==i:
            d2+=di2[j]
    pm1=0
    for j in dict13:
        if j[:2]==i:
            pm1+=dict13[j]
    pm2=0
    for j in dict12:
        if j[:2]==i:
            pm2+=dict12[j]
            
    r1=pm1+pm2
    d1_val+=d1
    d2_val+=d2
    total_pop+=r1
    state_id.append(i)
    vac_r1.append(d1/r1)
    vac_r2.append(d2/r1)
    



state_svratio["Stateid"]=state_id
state_svratio["vaccinateddose1ratio"]=vac_r1
state_svratio["vaccinateddose2ratio"]=vac_r2

df2=pd.DataFrame.from_dict(state_svratio)
df2=df2.sort_values(by=['vaccinateddose1ratio'],ascending=True)
df2.to_csv("state-vaccinated-dose-ratio.csv")

print("Overall vaccinateddose1ratio ",d1_val/total_pop)
print("Overall vaccinateddose2ratio ",d2_val/total_pop)

ovratio={"Overall":[],"vaccinateddose1ratio":[],"vaccinateddose2ratio":[]}
ov=[]
ov.append("Overall")
vac_r1=[]
vac_r1.append(d1_val/total_pop)
vac_r2=[]
vac_r2.append(d2_val/total_pop)


ovratio["Overall"]=ov
ovratio["vaccinateddose1ratio"]=vac_r1
ovratio["vaccinateddose2ratio"]=vac_r2

df3=pd.DataFrame.from_dict(ovratio)
df3.to_csv("overall-vaccinated-dose-ratio.csv")







