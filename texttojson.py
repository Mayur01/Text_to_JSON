import json

file = 'sample1.txt'

dict = {}

mappings = ["eventTime", "email", "sessionid"]

with open(file) as fo:
    id = 1
    for data in fo:
        desc = list(data.strip().split(' '))
        # print("line length is : "+ str(len(desc)))
        print(type(desc[0]))
        if len(desc) < 3 :
            continue
        eventime = desc[0]
        i=0

        dict2 = {}
        while i < len(mappings):
            dict2[mappings[i]] = desc[i]
            i=i+1

        dict[eventime] = dict2
        id=id+1

otfile = open("output.json", "w")
json.dump(dict,otfile,indent=3)
otfile.close()
