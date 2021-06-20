import json
from datetime import datetime

file = 'sampletest.txt'
# fromdate = '2000-01-01T17:25:49Z'
fromdate = input("Enter From date time in (%Y-%m-%dT%H:%M:%SZ) format: ")
todate = input("Enter From to time in (%Y-%m-%dT%H:%M:%SZ) format: ")

# todate = '2000-01-26T02:22:19Z'
fromdateformat=datetime.strptime(fromdate,'%Y-%m-%dT%H:%M:%SZ')
todateformat=datetime.strptime(todate,'%Y-%m-%dT%H:%M:%SZ')
# print(datetime01)
a=[]
mappings = ["eventTime", "email", "sessionid"]

with open(file) as fo:
    for data in fo:
        i=0 
        desc = list(data.strip().split(' '))
        traversedate=datetime.strptime(desc[0], '%Y-%m-%dT%H:%M:%SZ')
        # print("i value"+desc[i])
        # print("0 value"+ desc[0])
        # print(traversedate)
        if len(desc) < 3 or len(desc) > 3:
            continue

        if(traversedate >= fromdateformat and traversedate <= todateformat) :
            dict2 = {}
            while i < len(mappings):
                dict2[mappings[i]] = desc[i]
                i=i+1
            a.append(dict2)
        else :
            continue 

otfile = open("output.json", "w")
json.dump(a,otfile,indent=3)
otfile.close()
