import json
import time
import logging
import os.path
from os import path
from datetime import datetime

#-----------------------------------------------------------logfile----------------------------------------------------------------------
logging.basicConfig(filename="corruptdata.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

#-----------------------------------------------function to convert text to json-----------------------------------------------------------
def toJsonFormat(currentRecord):
    jsonData={}
    i=0
    mappings = ["eventTime", "email", "sessionid"]
    while i < len(mappings):
        jsonData[mappings[i]] = currentRecord[i]
        i=i+1
    return jsonData


# ---------------------------------------------Function to format date-time from string--------------------------------------------------
def parseDate(dates):
    return datetime.strptime(dates,'%Y-%m-%dT%H:%M:%SZ')


# ---------------------------------------------Function to check date format--------------------------------------------------------------
def checkDateFormat(dateformat):
    format = "%Y-%m-%dT%H:%M:%SZ"
    try:
        checkdate = bool(datetime.strptime(dateformat, format))
    except ValueError:
        checkdate = False
    return checkdate
    

#--------------------------------------------------Driver/Main function--------------------------------------------------------------------
def textToJson(filename, fromdate, todate):
    fromDateFormat = parseDate(fromdate)
    todate_format  = parseDate(todate)
    jsonArray=[]
    with open(filename, buffering=2000000000) as fo:
        for record in fo:
            i=0 
            currentRecord = list(record.strip().split(' '))
            if len(currentRecord) != 3:
                logging.debug("\nCorrupt data found {}".format(currentRecord))
                continue
            traverseDate=parseDate(currentRecord[0])

            if(traverseDate >= fromDateFormat and traverseDate <= todate_format) :
                convertedJsonData={}
                convertedJsonData=toJsonFormat(currentRecord)
                jsonArray.append(convertedJsonData)
            elif traverseDate > todate_format:
                break
    return jsonArray

# --------------------------------------------Program start here--------------------------------------------------------------------------
if __name__ == '__main__':

    file = input("Enter file name(if in same directory) or path to file: ")

    if(path.exists(file) != True):
        print("\nERROR:: Incorrect file name or path.\n")
        exit()

    fromdate = input("Enter From date time in (%Y-%m-%dT%H:%M:%SZ) format: ")
    todate = input("Enter From to time in (%Y-%m-%dT%H:%M:%SZ) format: ")

    fromDateFlag = checkDateFormat(fromdate)
    toDateFlag = checkDateFormat(todate)

    if (fromDateFlag == False or toDateFlag == False): 
        print("\nERROR:: Error while parsing date.. Incorrect date format.\n")
        exit()

    if parseDate(fromdate) >= parseDate(todate):
        print("\nERROR:: Error while parsing date.. End date should be greater than start date\n")
        exit()

    jsondata=textToJson(file, fromdate, todate)

    outputFile = open("output.json", "w")
    json.dump(jsondata,outputFile,indent=3)
    outputFile.close()

    print("\nCheck output.json file for the desired result.")
    print("Check corruptdata.log file for any corrupt data.\n")

# 1. One pass - 6 cores. 6x threads which take data in round-robin.
# 2. Two pass - first pass = number of records in file. second pass give each thread- n number of lines to process.
