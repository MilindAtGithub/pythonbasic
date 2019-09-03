# This is will connect to the MonogoDB fire a Query and print the results

import csv
from pymongo import MongoClient
import configparser
config = configparser.RawConfigParser()
config.read('produtil.properties')

from finxencryption.pyfinxencryption import  finXEncryption

# Connecting to MongoDb Using the URL String
dbUsr =config.get('UploadReport','database.user')
dbPWD = str(finXEncryption().decryptData(config.get('UploadReport','database.password')),'utf-8').lstrip()
host=config.get('UploadReport','database.host')
port = config.get('UploadReport','database.port')
mongoClient = MongoClient(f'mongodb://{dbUsr}:{dbPWD}@{host}:{port}/prequal')
mydb = mongoClient["prequal"]
mycol = mydb["quoteinfo"]

import datetime

start = datetime.datetime(int(config.get('UploadReport','startdate.year')),
                          int(config.get('UploadReport','startdate.month')),
                          int(config.get('UploadReport','startdate.day')))
end = datetime.datetime(int(config.get('UploadReport','enddate.year')),
                        int(config.get('UploadReport','enddate.month')),
                        int(config.get('UploadReport','enddate.day')), 23, 59, 59)

queryStr = [{ "$match":{'$and' :[ {"createdDate" :{'$gte':start,'$lte':end}},{"applicantIndex" : 0},{"status" : "SUBMITTED"}] } },
                         { "$lookup": {"localField": "referenceId","from": "documentUpload","foreignField": "referenceId","as": "document_Upload"} },
                         { "$unwind": "$document_Upload" },
                         {"$lookup": { "localField": "referenceId", "from": "external_conditions", "foreignField": "referenceId","as": "externalconditions"} },
                         { "$unwind": "$externalconditions"},
                         { "$project": {
                                            "externalconditions.categoryList.items.conditionStatus": 1,
                                             "externalconditions.categoryList.category": 1,
                                             "externalconditions.categoryList.items.date": 1,
                                             "externalconditions.categoryList.items.name": 1,
                                              "externalconditions.categoryList.items.extStatus": 1,
                                             "document_Upload.conditions.documents.uploadedStatus": 1,
                                             "document_Upload.conditions.documents.uploadedDate": 1,
                                             "document_Upload.conditions.documents.retryCount": 1,
                                             "document_Upload.conditions.conditionInfo.externalFlag": 1,
                                             "document_Upload.conditions.conditionInfo.conditionName": 1,
                                             "document_Upload.conditions.conditionInfo.documentCategory": 1,
                                              "document_Upload.conditions.documents.fileName":1,
                                             "loanNumber": 1,
                                             "fullApplication.personalDetails.email": 1,
                                             "createdDate":1,
                                             "fullApplication.personalDetails.mobilePhone":1,
                                              "heloc.personalDetails.mobilePhone":1,
                                              "heloc.personalDetails.email": 1,
                                             "applicantIndex":1,
                                              "referenceId" : 1,
                                              "applicationType": 1

                        } }
            ]

print("Fetching the Data From DB")
cursor = mycol.aggregate(queryStr)
print("Data Fetched Now Printing ....")

fieldnames = ('Loan Number', 'Loan Creation Date', 'Borrower Email', 'Condition Name', 'Condition Added Date',
                  'Document Upload Count', 'Doc Upload Date', 'Status')
timeNow = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S-%f")
with open(config.get('UploadReport','filename')+'_{}.csv'.format(timeNow), 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

def writeRowsToCSV(dicVal):
    with open(config.get('UploadReport','filename')+'_{}.csv'.format(timeNow), 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(dicVal)

for x in cursor:
    # print(x)
    loanNumber = x['loanNumber']
    createDate =x ['createdDate']
    email = x['heloc']['personalDetails']['email'] if 'heloc' in x.keys() else x['fullApplication']['personalDetails']['email']
    # First Get The Conditions
    catList = x['externalconditions']['categoryList']
    if len(catList) > 0:
        for cat in catList:
            items = cat['items']
            for eachItems in items:
                catConditionName = eachItems['name']
                conditionAddedDate = eachItems['date']
                if 'document_Upload' in x.keys():
                    conditions = x['document_Upload']['conditions']
                    if len(conditions) > 0:
                        conditionMatch=False
                        for y in conditions:
                            conditionName = y['conditionInfo']['conditionName']
                            if catConditionName == conditionName:
                                conditionMatch=True
                                documents = y['documents']
                                if len(documents) > 0:
                                    for z in documents:
                                        uploadedDate = z['uploadedDate']
                                        retryCount = z['retryCount']
                                        uploadStatus = z['uploadedStatus']
                                        writeRowsToCSV({'Loan Number': loanNumber,
                                                        'Loan Creation Date': createDate.strftime(
                                                            "%m-%d-%Y %H:%M:%S.%f"),
                                                        'Borrower Email': email,
                                                        'Condition Name': catConditionName,
                                                        'Condition Added Date': conditionAddedDate,
                                                        'Document Upload Count': retryCount,
                                                        'Doc Upload Date': uploadedDate,
                                                        'Status': uploadStatus
                                                        })
                        if not conditionMatch:
                            uploadedDate= "No Document Uploaded"
                            retryCount=0
                            uploadStatus=""
                            writeRowsToCSV({'Loan Number': loanNumber,
                                                 'Loan Creation Date': createDate.strftime("%m-%d-%Y %H:%M:%S.%f"),
                                                 'Borrower Email': email,
                                                 'Condition Name': catConditionName,
                                                 'Condition Added Date': conditionAddedDate,
                                                 'Document Upload Count': retryCount,
                                                 'Doc Upload Date': uploadedDate,
                                                 'Status': uploadStatus
                                                 })

