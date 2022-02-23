import json
import numpy as np
import pandas as pd
from datetime import timedelta, date

f = open('neighbor-districts-modified.json') 
data = json.load(f)

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


#Weekly cases
week_wise={"districtid":[],"weekid":[], "cases":[],}
districtid_val=[]
timeid_val=[]
cases_val=[]
dict12={}
for i in data:
    idx=[j for j in range(len(dist_list)) if dist_list[j]==i[3:]]
    li=cp()
    week=[]
    for k in idx:
        if date1[k] in li:
            li[date1[k]]=confirmed[k]
    p=0
    weekid=1
    prev=0
    lp=[]
    for j in li:
        lp.append(li[j])
    for k in range(len(lp)):
        if p==6:
            timeid_val.append(weekid)
            weekid+=1
            districtid_val.append(i)
            cases_val.append(abs(lp[k]-prev))
            prev=lp[k]
            p=0
        else:
            p+=1
week_wise["districtid"]=districtid_val
week_wise["weekid"]=timeid_val
week_wise["cases"]=cases_val
df1=pd.DataFrame.from_dict(week_wise)
df1.to_csv("cases-week.csv")

# Monthly Cases
month_wise={"districtid":[],"monthid":[],'cases':[]}
districtid_mval=[]
month_id=[]
cases=[]

for i in data:
    yr,mon,day1,day2=2020,'03',15,14
    start=str(yr)+'-'+mon+'-'+str(day1)
    end=str(yr)+'-'+'0'+str(int(mon)+1)+'-'+str(day2)
    idx=[j for j in range(len(dist_list)) if dist_list[j]==i[3:]]
    li=cp()
    week=[]
    for k in idx:
        if date1[k] in li:
            li[date1[k]]=confirmed[k]
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
    monthid=1
    for l in month:
        districtid_mval.append(i)
        month_id.append(monthid)
        monthid+=1
        cases.append(l)

month_wise["districtid"]=districtid_mval
month_wise["monthid"]=month_id
month_wise["cases"]=cases
df2=pd.DataFrame.from_dict(month_wise)
df2.to_csv("cases-month.csv")

##Overall Cases
##overall cases
timeid=[]
dist=[]
li1=[]
for i in data:
    d=i[3:]
    if d in dist_list:
        ind=0
        for j in range(len(dist_list)):
            if d==dist_list[j]:
                ind=j
        li1.append(i)
        dist.append(confirmed[ind])
        timeid.append(1)


overall = {'districtid': li1, 'overall': timeid, 'cases':dist }
overall = pd.DataFrame(overall)
overall.to_csv('case-overall.csv')