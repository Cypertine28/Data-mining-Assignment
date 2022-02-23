import json
import numpy as np
import pandas as pd
from datetime import timedelta, date

f = open('neighbor-districts-modified.json') 
data = json.load(f)
vaccine_data=pd.read_csv("vaccination_data_district_wise.csv")

state_list=vaccine_data.loc[1:,'State']
dist_codes=[]
for i in data:
    if i[:2] not in dist_codes:
        dist_codes.append(i[:2])

state_to_name={'AN':'Andaman and Nicobar Islands','AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CH':'Chandigarh','CT':'Chhattisgarh','DN':'Dadra and Nagar Haveli and Daman and Diu','DL':'Delhi','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LA':'Ladakh','LD':'Lakshadweep','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Odisha','PY':'Puducherry','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana','TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttarakhand','WB':'West Bengal'}
col=vaccine_data.columns
col=col[6:]
dist_list=vaccine_data.loc[:,'District_Key']
dist_list1=[]
for i in range(len(dist_list)):
    if dist_list[i] in data:
        dist_list1.append(dist_list[i])

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2020,3,15)
end_dt = date(2021, 8, 14)
list1=[]
for dt in daterange(start_dt, end_dt):
    list1.append(dt.strftime("%d/%m/20%y"))

##Weekly -district
week_wise_vaccine_dist={"districtid":[],"weekid":[],'dose1':[],'dose2':[]}
districtid=[]
week_ids=[]
dose_1=[]
dose_2=[]
dict_for_overall1={}
dict_for_overall2={}
for i in range(len(dist_list)):
    dlist=list1
    drow=vaccine_data.iloc[i]
    if dist_list[i] not in data:
        continue
    week_list1=[]
    week_list2=[]
    for j in dlist:
        dose1=j+".3"
        dose2=j+".4"
        if dose1 not in col:
            week_list1.append(0)
            week_list2.append(0)
        elif (dose1 in col) and (dose2 not in col):
            if(type(drow[dose1])==np.nan):
                week_list1.append(0)
            else:
                week_list1.append(float(drow[dose1]))
            week_list2.append(0)
        else:
            if(type(drow[dose1])==np.nan):
                week_list1.append(0)
            else:
                week_list1.append(float(drow[dose1]))   
            if(type(drow[dose2])==np.nan):
                week_list2.append(0)
            else:
                week_list2.append(float(drow[dose2]))
    
    dict_for_overall1[dist_list[i]]=week_list1
    dict_for_overall2[dist_list[i]]=week_list2
    weekid=1
    p=0
    prev1=0
    prev2=0
    for k in range(len(week_list1)):
        if p==6:
            districtid.append(dist_list[i])
            week_ids.append(weekid)
            weekid+=1
            dose_1.append(week_list1[k]-prev1)
            dose_2.append(week_list2[k]-prev2)
            prev1=week_list1[k]
            prev2=week_list2[k]
            p=0
        else:
            p=p+1

week_wise_vaccine_dist["districtid"]=districtid
week_wise_vaccine_dist["weekid"]=week_ids
week_wise_vaccine_dist["dose1"]=dose_1
week_wise_vaccine_dist["dose2"]=dose_2
df1=pd.DataFrame.from_dict(week_wise_vaccine_dist)
df1.to_csv("district-vaccinated-count-week.csv")

##District overall
overall_wise_vaccine_dist={"districtid":[],"Overall":[],'dose1':[],'dose2':[]}
districtid=[]
Overall =[]
dose_1=[]
dose_2=[]

for i in dict_for_overall1:
    li=dict_for_overall1[i]
    dose_1.append(li[len(li)-1])
    Overall.append(1)
    districtid.append(i)

for i in dict_for_overall2:
    li=dict_for_overall2[i]
    dose_2.append(li[len(li)-1])
    overall_wise_vaccine_dist["districtid"]=districtid
overall_wise_vaccine_dist["Overall"]=Overall
overall_wise_vaccine_dist["dose1"]=dose_1
overall_wise_vaccine_dist["dose2"]=dose_2      
df12=pd.DataFrame.from_dict(overall_wise_vaccine_dist)
df12.to_csv("district-vaccinated-count-Overall.csv")

##state Overall
overall_wise_vaccine_dist={"Stateid":[],"Overall":[],'dose1':[],'dose2':[]}
state=[]
Overall =[]
dose_1=[]
dose_2=[]
for i in dist_codes:
    s=0
    for j in dict_for_overall1:
        if j[:2]==i:
            li=dict_for_overall1[j]
            val=li[len(li)-1]
            s+=val
    
    s1=0
    for j in dict_for_overall2:
        if j[:2]==i:
            li=dict_for_overall2[j]
            val=li[len(li)-1]
            s1+=val
    
    dose_1.append(s)
    dose_2.append(s1)
    state.append(i)
    Overall.append(1)

overall_wise_vaccine_dist["Stateid"]=state
overall_wise_vaccine_dist["Overall"]=Overall
overall_wise_vaccine_dist["dose1"]=dose_1
overall_wise_vaccine_dist["dose2"]=dose_2      
df123=pd.DataFrame.from_dict(overall_wise_vaccine_dist)
df123.to_csv("state-vaccinated-count-Overall.csv")

##week state
districts=df1['districtid']
weekid=df1['weekid']
dose1=df1['dose1']
dose2=df1['dose2']
week_wise_state={"Stateid":[],"weekid":[],'dose1':[],'dose2':[]}
state_id_week=[]
week_id=[]
dose_1=[]
dose_2=[]
dist_dict1={}
dist_dict2={}
for i in dist_codes:
    dict_week1=[]
    dict_week2=[]
    idx=[j for j in range(len(districts)) if districts[j][:2]==i]
    for j in range(1,75):
        s1=0
        s2=0
        for k in idx:
            if j==weekid[k]:
                s1+=dose1[k]
                s2+=dose2[k]
        dict_week1.append(s1)
        dict_week2.append(s2)
    weekid1=1
    for l in range(len(dict_week1)):
        state_id_week.append(i)
        week_id.append(weekid1)
        weekid1+=1
        dose_1.append(dict_week1[l])
        dose_2.append(dict_week2[l])
    dist_dict1[i]=dict_week1 
    dist_dict2[i]=dict_week2

week_wise_state["Stateid"]=state_id_week
week_wise_state["weekid"]=week_id
week_wise_state["dose1"]=dose_1
week_wise_state["dose2"]=dose_2      
df2=pd.DataFrame.from_dict(week_wise_state)
df2.to_csv("state-vaccinated-count-week.csv")


##count monthly

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2020,3,15)
end_dt = date(2021, 8, 14)
list1={}
list2={}
for dt in daterange(start_dt, end_dt):
    list1[dt.strftime("%d/%m/20%y")]=0
for dt in daterange(start_dt, end_dt):
    list2[dt.strftime("%d/%m/20%y")]=0

month_wise_district={"districtid":[],"monthid":[],'dose1':[],'dose2':[]}
district_id_month=[]
month_id=[]
dose_mon1=[]
dose_mon2=[]
for i in range(len(dist_list)):
    dlist1=list1
    dlist22=list2
    yr,mon,day1,day2=2020,'03',15,14
    start=str(day1)+'/'+mon+'/'+str(yr)
    end=str(day2)+'/'+'0'+str(int(mon)+1)+'/'+str(yr)
    drow=vaccine_data.iloc[i]
    if dist_list[i] not in data:
        continue
        
    for j in dlist1:
        dose1=j+".3"
        if dose1 not in col:
            dlist1[j]=0
        else:
            if(type(drow[dose1])==np.nan):
                dlist1[j]=0
            else:
                val=float(drow[dose1])
                dlist1[j]=val
                
    for t in dlist22:
        dose2=t+".4"
        if dose2 not in col:
            dlist22[t]=0
        else:
            if(type(drow[dose2])==np.nan):
                dlist22[t]=0
            else:
                val=float(drow[dose2])
                dlist22[t]=val
    
    dose_1=[]
    prev=0
    for p in dlist1:
        if start==p:
            prev=dlist1[p]
            if(int(mon)==12):
                yr=2021
                mon='01'
            else:
                if int(mon)>=9:
                    mon=str(int(mon)+1)
                else:
                    mon='0'+str(int(mon)+1)
            start=str(day1)+'/'+mon+'/'+str(yr)
        if p==end:
            dose_1.append(dlist1[p]-prev)
            if(int(mon)==12):
                yr=2021
                end=str(day2)+'/'+'01'+'/'+str(yr)
            else:
                if int(mon)>=9:
                    end=str(day2)+'/'+str(int(mon)+1)+'/'+str(yr)
                else:
                    end=str(day2)+'/'+'0'+str(int(mon)+1)+'/'+str(yr)
    dose_2=[]
    prev=0
    yr,mon,day1,day2=2020,'03',15,14
    start=str(day1)+'/'+mon+'/'+str(yr)
    end=str(day2)+'/'+'0'+str(int(mon)+1)+'/'+str(yr)
    for p in dlist22:
        if start==p:
            prev=dlist22[p]
            if(int(mon)==12):
                yr=2021
                mon='01'
            else:
                if int(mon)>=9:
                    mon=str(int(mon)+1)
                else:
                    mon='0'+str(int(mon)+1)
            start=str(day1)+'/'+mon+'/'+str(yr)
        if p==end:
            dose_2.append(dlist22[p]-prev)
            if(int(mon)==12):
                yr=2021
                end=str(day2)+'/'+'01'+'/'+str(yr)
            else:
                if int(mon)>=9:
                    end=str(day2)+'/'+str(int(mon)+1)+'/'+str(yr)
                else:
                    end=str(day2)+'/'+'0'+str(int(mon)+1)+'/'+str(yr)
    monthid1=1
    for k in range(len(dose_1)):
        district_id_month.append(dist_list[i])
        dose_mon1.append(dose_1[k])
        dose_mon2.append(dose_2[k])
        month_id.append(monthid1)
        monthid1+=1
        
month_wise_district["districtid"]=district_id_month
month_wise_district["monthid"]=month_id
month_wise_district["dose1"]=dose_mon1
month_wise_district["dose2"]=dose_mon2      
df4=pd.DataFrame.from_dict(month_wise_district)
df4.to_csv("district-vaccinated-count-month.csv")



districts=df4['districtid']
monthid=df4['monthid']
dose1=df4['dose1']
dose2=df4['dose2']
month_wise_state={"Stateid":[],"monthid":[],'dose1':[],'dose2':[]}
state_id_month=[]
month_id=[]
dose_1=[]
dose_2=[]
dist_dict1={}
dist_dict2={}
for i in dist_codes:
    dict_month1=[]
    dict_month2=[]
    idx=[j for j in range(len(districts)) if districts[j][:2]==i]
    for j in range(1,18):
        s1=0
        s2=0
        for k in idx:
            if j==monthid[k]:
                s1+=dose1[k]
                s2+=dose2[k]
        dict_month1.append(s1)
        dict_month2.append(s2)
    id1=1
    for l in range(len(dict_month1)):
        state_id_month.append(i)
        month_id.append(id1)
        id1+=1
        dose_1.append(dict_month1[l])
        dose_2.append(dict_month2[l])
    dist_dict1[i]=dict_month1 
    dist_dict2[i]=dict_month2
month_wise_state["Stateid"]=state_id_month
month_wise_state["monthid"]=month_id
month_wise_state["dose1"]=dose_1
month_wise_state["dose2"]=dose_2      
df5=pd.DataFrame.from_dict(month_wise_state)
df5.to_csv("state-vaccinated-count-month.csv")