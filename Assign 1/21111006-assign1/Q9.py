import json
import numpy as np
import pandas as pd
import xlrd
from datetime import timedelta, date

f = open('neighbor-districts-modified.json') 
data = json.load(f)

vaccine_data=pd.read_csv("state-vaccinated-count-week.csv")
state_to_name={'AN':'Andaman and Nicobar Islands','AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CH':'Chandigarh','CT':'Chhattisgarh','DN':'Dadra and Nagar Haveli and Daman and Diu','DL':'Delhi','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LA':'Ladakh','LD':'Lakshadweep','MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Odisha','PY':'Puducherry','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim','TN':'Tamil Nadu','TG':'Telangana','TR':'Tripura','UP':'Uttar Pradesh','UT':'Uttarakhand','WB':'West Bengal'}
state=vaccine_data['Stateid']
weekids=vaccine_data['weekid']
dose1=vaccine_data['dose1']

statewise={}
for i in state:
    idx=[j for j in range(len(state)) if state[j]==i]
    statewise[state_to_name[i]]=dose1[idx[73]]/7

    
pop_data = pd.read_excel(r'DDW_PCA0000_2011_Indiastatedist.xlsx')

states=list(pop_data["Name"])
tru=list(pop_data['TRU'])
tot_p=list(pop_data['TOT_P'])
LEVEL=list(pop_data['Level'])

state_pop={}

dict1={}
for i in statewise:
    if i.upper() not in states:
        continue
    idx=[j for j in range(len(states)) if states[j].upper()==i.upper() and tru[j]=='Total' and LEVEL[j]=='STATE']
    for j in idx:
        if tru[j]=='Total':
            state_pop[i]=tot_p[j]
            
            
vaccinedata=pd.read_csv("vaccination_data_district_wise.csv")

state_vacc=list(vaccinedata['State_Code'])
state_vacc_data=list(vaccinedata['14/08/2021.3'])


state_tv={}
for i in range(len(state_vacc)):
    if type(state_vacc[i])==float:
        continue
    idx=[j for j in range(len(state_vacc)) if state_vacc[j]==state_vacc[i]]
    s=0
    for j in idx:
        s+=int(state_vacc_data[j])
    state_tv[state_to_name[state_vacc[i]]]=s
    
remaning={}
for i in state_tv:
    if i in state_pop:
        remaning[i]=state_pop[i]-state_tv[i]
    
for i in remaning:
    val1=remaning[i]
    val2=statewise[i]
    
dict_dt={}
for i in remaning:
    val1=remaning[i]
    val2=statewise[i]
    k=int(val1/val2)
    dict_dt[i]=k
    
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
start_dt = date(2021,8,15)
end_dt = date(2024, 12, 31)
list1=[]
for dt in daterange(start_dt, end_dt):
    list1.append(dt.strftime("%d/%m/20%y"))

    
state_date={"stateid":[],"populationleft":[],'rateofvaccination':[],'date':[]}
state_id=[]
pop_left=[]
rofvac=[]
dt=[]

for i in remaning:
    state_id.append(i)
    pop_left.append(remaning[i])
    rofvac.append(statewise[i])
    dt.append(list1[dict_dt[i]])

state_date["stateid"]=state_id
state_date["populationleft"]=pop_left
state_date["rateofvaccination"]=rofvac
state_date["date"]=dt      

df1=pd.DataFrame.from_dict(state_date)
df1.to_csv("complete-vaccination.csv")