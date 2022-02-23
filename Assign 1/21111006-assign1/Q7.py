import json
import numpy as np
import pandas as pd
import xlrd

f = open('neighbor-districts-modified.json') 
data = json.load(f)

vaccine_data=pd.read_csv("vaccination_data_district_wise.csv")
print(len(vaccine_data))

from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2020,3,15)
end_dt = date(2021, 8, 14)
list1=[]
for dt in daterange(start_dt, end_dt):
    list1.append(dt.strftime("%d/%m/20%y"))


state_list=vaccine_data.loc[1:,'State']

col=vaccine_data.columns
col=col[6:]

dist_list=vaccine_data.loc[:,'District_Key']



dict_district1={}
dict_district2={}
for i in range(len(dist_list)):
    dlist=list1
    drow=vaccine_data.iloc[i]
    if dist_list[i] not in data:
        continue
    cowaxin_list1=[]
    covisheid_list1=[]
    for j in dlist:
        point1=j+".8"
        point2=j+".9"
        if point1 not in col:
            cowaxin_list1.append(0)
        else:
            if(type(drow[point1])==np.nan):
                cowaxin_list1.append(0)
            else:
                cowaxin_list1.append(float(drow[point1])) 
        if point2 not in col:
            covisheid_list1.append(0)
        else:
            if(type(drow[point2])==np.nan):
                covisheid_list1.append(0)
            else:
                covisheid_list1.append(float(drow[point2]))
    dict_district1[dist_list[i]]=(max(covisheid_list1))
    dict_district2[dist_list[i]]=(max(cowaxin_list1))    
        
        

ratio_district={}
for i in dict_district1:
    if dict_district2[i]==0:
        ratio_district[i]=float('inf')
    else:
        ratio_district[i]=dict_district1[i]/dict_district2[i]

district_wise_ratio={"districtid":[],"vaccineratio":[]}
districtid=[]
vacc_ratio=[]

for i in ratio_district:
    districtid.append(i)
    vacc_ratio.append(ratio_district[i])

district_wise_ratio["districtid"]=districtid
district_wise_ratio["vaccineratio"]=vacc_ratio

df1=pd.DataFrame.from_dict(district_wise_ratio)
df1=df1.sort_values(by=['vaccineratio'],ascending=True)
df1.to_csv("district-vaccination-type-ratio.csv")

state_to_name={'AN':'Andaman and Nicobar Islands','AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CH':'Chandigarh','CT':'Chhattisgarh','DN':'Dadra and Nagar Haveli and Daman and Diu','DL':'Delhi','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LA':'Ladakh','LD':'Lakshadweep','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Odisha','PY':'Puducherry','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana','TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttarakhand','WB':'West Bengal'}

dist_codes=[]
for i in df1['districtid']:
    if i[:2] not in dist_codes:
        dist_codes.append(i[:2])

state_svratio={"Stateid":[],"vaccineratio":[]}
state_id=[]
vacr=[]

cv_val=0
cs_val=0
for i in dist_codes:
    cv=0
    cs=0
    for j in dict_district1:
        if j[:2]==i:
            cs+=dict_district1[j]
    for j in dict_district2:
        if j[:2]==i:
            cv+=dict_district2[j]
    r1=cs/cv
    cv_val+=cv
    cs_val+=cs
    state_id.append(i)
    vacr.append(round(r1, 2))

state_svratio["Stateid"]=state_id
state_svratio["vaccineratio"]=vacr

df2=pd.DataFrame.from_dict(state_svratio)
df2=df2.sort_values(by=['vaccineratio'],ascending=True)
df2.to_csv("state-vaccination-type-ratio.csv")

ovratio={"Overall":[],"vaccineratio":[]}
l1=[]
l1.append("Overall")
l2=[]
l2.append(round(cs_val/cv_val,3))
ovratio["Overall"]=l1
ovratio["vaccineratio"]=l2

df3=pd.DataFrame.from_dict(ovratio)
df3.to_csv("overall-vaccination-type-ratio.csv")









































