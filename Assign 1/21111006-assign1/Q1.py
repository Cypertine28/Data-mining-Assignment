import json
import numpy as np
import pandas as pd


f=open("neighbor-districts.json")
data=json.load(f)
f.close()
new_dict={}
for i in data:
    key=i.replace("_"," ")
    key=key.replace(" district","")
    key=key[:key.find("/")]
    new_dict[key]=data[i]
    n=[]
    for j in new_dict[key]:
        temp=j.replace("_"," ")
        temp=temp.replace(" district","")
        temp=temp[:temp.find("/")]
        n.append(temp)
    new_dict[key]=n

vaccine_data=pd.read_csv("vaccination_data_district_wise.csv")

districts=vaccine_data['District_Key']
vaccinelist=districts.dropna()
new_dist=[]
for i in vaccinelist:
    search=i[3:]
    new_dist.append(search.lower())

final={}
for i in new_dict:
    if(i not in new_dist):
        continue
    t1=vaccinelist[new_dist.index(i)+1]
    if t1[3:]=="Aurangabad":
        t1="MH_Aurangabad"
        
    final[t1]=new_dict[i]
    n=[]
    for j in final[t1]:
        if(j not in new_dist):
            continue
        t=vaccinelist[new_dist.index(j)+1]
        if t[3:]=="Aurangabad":
            t="MH_Aurangabad"
        n.append(t)
    final[t1]=sorted(n)
    
with open("neighbor-districts-modified.json", "w") as outfile:
    json.dump(final, outfile, indent = 2, sort_keys=True)
    outfile.close()