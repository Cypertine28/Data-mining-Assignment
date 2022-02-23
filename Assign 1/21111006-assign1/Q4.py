import json
import numpy as np
import pandas as pd
from datetime import timedelta, date

f = open('neighbor-districts-modified.json') 
data = json.load(f)
# len(data)

districts_data=pd.read_csv("districts.csv")
# print(len(districts_data))
dist_list=list(districts_data["District"])
confirmed=list(districts_data["Confirmed"])
date1=list(districts_data["Date"])

def cp():
    def daterange(date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + timedelta(n)

    start_dt = date(2020,3,15)
    end_dt = date(2021, 8, 14)
    list1={}
    for dt in daterange(start_dt, end_dt):
        list1[dt.strftime("%Y-%m-%d")]=0
    return list1


district_wise={"districtid":[],"wave1-weekid":[],'wave2-weekid':[],'wave1-monthid':[],'wave2-monthid':[]}
districtid_val=[]
wave1_week=[]
wave2_week=[]
month_wave1=[]
month_wave2=[]
week_wise1={"districtid":[],"weekid":[],'case':[]}
districtid_val1=[]
week=[]
weekly_cases=[]
month_wise12={"Districtid":[],"monthid":[],'cases':[]}
districtid_val_month=[]
month_id=[]
month_cases=[]
#weekly
dit12={}
dit13={}
for i in data:
    if i[3:] not in dist_list:
        continue
    idx=[j for j in range(len(dist_list)) if dist_list[j]==i[3:]]
    li=cp()
    for k in idx:
        if date1[k] in li:
            li[date1[k]]=confirmed[k]
    p=0
    weekid=1
    prev=0
    lp=[]
    for j in li:
        lp.append(li[j])
    weeks=[]
    prev2=0
    flag=False
    for k in range(len(lp)):
        if p==4:
            prev2=lp[k]
            flag=True
        if p==3 and flag:
            weekly_cases.append(lp[k]-prev2)
            districtid_val1.append(i)
            week.append(weekid)
            weekid+=1
            weeks.append(lp[k]-prev2)
            flag=False
        if p==6:
            weekly_cases.append(lp[k]-prev)
            districtid_val1.append(i)
            week.append(weekid)
            weekid+=1
            weeks.append(lp[k]-prev)
            prev=lp[k]
            p=0
        else:
            p+=1
    dit12[i]=weeks
    li12=weeks
    peak1=max(li12[:91])
    wave1_week.append(li12.index(peak1)+1)
    peak2=max(li12[91:])
    wave2_week.append(li12.index(peak2)+1)
    
    #monthly
    yr,mon,day1,day2=2020,'03',15,14
    start=str(yr)+'-'+mon+'-'+str(day1)
    end=str(yr)+'-'+'0'+str(int(mon)+1)+'-'+str(day2)
    month=[]
    prev=0
    for p in li:
        if start==p:
            prev=li[p]
            if(int(mon)==12):
                yr=2021
                mon='01'
            else:
                if int(mon)>=9:
                    mon=str(int(mon)+1)
                else:
                    mon='0'+str(int(mon)+1)
            start=str(yr)+'-'+mon+'-'+str(day1)
        if p==end:
            month.append(li[p]-prev)
            if(int(mon)==12):
                yr=2021
                end=str(yr)+'-'+'01'+'-'+str(day2)
            else:
                if int(mon)>=9:
                    end=str(yr)+'-'+str(int(mon)+1)+'-'+str(day2)
                else:
                    end=str(yr)+'-'+'0'+str(int(mon)+1)+'-'+str(day2)
    dit13[i]=month
    peak1=max(month[:11])
    districtid_val.append(i)
    month_wave1.append(month.index(peak1)+1)
    peak2=max(month[11:])
    month_wave2.append(month.index(peak2)+1)
    monthid=1
    for l in month:
        districtid_val_month.append(i)
        month_id.append(monthid)
        monthid+=1
        month_cases.append(l)
district_wise["districtid"]=districtid_val
district_wise["wave1-weekid"]=wave1_week
district_wise["wave2-weekid"]=wave2_week
district_wise["wave1-monthid"]=month_wave1
district_wise["wave2-monthid"]=month_wave2

q4=pd.DataFrame.from_dict(district_wise)
q4.to_csv("district-peaks.csv")


###
week_wise1["districtid"]=districtid_val1
week_wise1["weekid"]=week
week_wise1["case"]=weekly_cases 
demo=pd.DataFrame.from_dict(week_wise1)
demo.to_csv("q4_week.csv")
districts1=demo['districtid']
weekid=demo['weekid']
cases1=demo['case']
month_wise12["Districtid"]=districtid_val_month
month_wise12["monthid"]=month_id
month_wise12["cases"]=month_cases 
demo1=pd.DataFrame.from_dict(month_wise12)
demo1.to_csv("Q4_monthly.csv")
districts2=demo1['Districtid']
monthid1=demo1['monthid']
cases2=demo1['cases']

###


state_peak={"stateid":[],"wave1-weekid":[],'wave2-weekid':[],'wave1-monthid':[],'wave2-monthid':[]}
stateid=[]
wave1_week=[]
wave2_week=[]
wave1_month=[]
wave2_month=[]
dist_codes=[]
for i in districts1:
    if i[:2] not in dist_codes:
        dist_codes.append(i[:2])
dist_dict={}
for i in dist_codes:
    dict_week=[]
    idx=[j for j in range(len(districts1)) if districts1[j][:2]==i]
    for j in range(1,148):
        s=0
        for k in idx:
            if j==weekid[k]:
                s+=cases1[k]
        dict_week.append(s)
    dist_dict[i]=dict_week   
for i in dist_dict:
    li12=dist_dict[i]
    peak1=max(li12[:91])
    wave1_week.append(li12.index(peak1)+1)
    peak2=max(li12[91:])
    wave2_week.append(li12.index(peak2)+1)

dist_dict1={}
for i in dist_codes:
    dict_week=[]
    idx=[j for j in range(len(districts2)) if districts2[j][:2]==i]
    for j in range(1,18):
        s=0
        for k in idx:
            if j==monthid1[k]:
                s+=cases2[k]
        dict_week.append(s)
    dist_dict1[i]=dict_week   

for i in dist_dict1:
    li12=dist_dict1[i]
    peak1=max(li12[:11])
    stateid.append(i)
    wave1_month.append(li12.index(peak1)+1)
    peak2=max(li12[11:])
    wave2_month.append(li12.index(peak2)+1)


state_peak["stateid"]=stateid
state_peak["wave1-weekid"]=wave1_week
state_peak["wave2-weekid"]=wave2_week 
state_peak["wave1-monthid"]=wave1_month
state_peak["wave2-monthid"]=wave2_month    
df4=pd.DataFrame.from_dict(state_peak)
df4.to_csv("state-peaks.csv")


###

overall_peak={"Overall":[],"wave1-weekid":[],'wave2-weekid':[],'wave1-monthid':[],'wave2-monthid':[]}
ovid=[]
wave1_week=[]
wave2_week=[]
wave1_month=[]
wave2_month=[]

li1=[]
for i in range(0,91):
    s=0
    for j in dist_dict:
        li=dist_dict[j]
        s+=li[i]
    li1.append(s)
val1=li1.index(max(li1))+1
li1=[]
for i in range(91,147):
    s=0
    for j in dist_dict:
        li=dist_dict[j]
        s+=li[i]
    li1.append(s)
val2=li1.index(max(li1))+1
ovid.append("Overall")
wave1_week.append(val1)
wave2_week.append(val2+91)
li1=[]
for i in range(0,10):
    s=0
    for j in dist_dict1:
        li=dist_dict1[j]
        s+=li[i]
    li1.append(s)
val1=li1.index(max(li1))+1
li1=[]
for i in range(10,17):
    s=0
    for j in dist_dict1:
        li=dist_dict1[j]
        s+=li[i]
    li1.append(s)
val2=li1.index(max(li1))+1
wave1_month.append(val1)
wave2_month.append(val2+10)

overall_peak["Overall"]=ovid
overall_peak["wave1-weekid"]=wave1_week
overall_peak["wave2-weekid"]=wave2_week
overall_peak["wave1-monthid"]=wave1_month
overall_peak["wave2-monthid"]=wave2_month
df21=pd.DataFrame.from_dict(overall_peak)
df21.to_csv("overall-peaks.csv")