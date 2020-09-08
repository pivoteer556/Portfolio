import twilio
import csv
import requests
import re
from twilio.rest import Client

def Main(currentMonth):
    with open('Interview Dataset.csv', newline='') as csvfile:
        myReader = csv.reader(csvfile)
        columns = next(myReader)
        mobilePhones = []
        mobilePhoneColumnIndex = GetMobilePhoneIndex(columns)
        birthDateColumnIndex = GetBirthDateIndex(columns)
        for row in myReader:
            birthDate = row[birthDateColumnIndex]
            if birthDate[0] == currentMonth:
                mobilePhones.append(row[mobilePhoneColumnIndex])
        ProcessRequest(mobilePhones)
        

#Gets the index of the column with mobile phones in it
#Takes in a list of columns, spits out said index.
def GetMobilePhoneIndex(columns):
    mobilePhoneColumnIndex = -1
    lcv = 0 #I'm aware that enumerate is more "Pythonic", but I'm valuing portability over language-specific standards
    for column in columns:
        if column == 'Mobile Phone':
            mobilePhoneColumnIndex = lcv
            return mobilePhoneColumnIndex
        lcv += 1

#Gets the index of the column with DOB's in it
#Takes in a list of columns, spits out said index.
def GetBirthDateIndex(columns):
    print (columns)
    birthDateColumnIndex = -1
    lcv = 0 #I'm aware that enumerate is more "Pythonic", but I'm valuing portability over language-specific standards
    for column in columns:
        if column == 'Date of Birth':
            mobilePhoneColumnIndex = lcv
            return mobilePhoneColumnIndex
        lcv += 1

#Processes the requests via twilio
def ProcessRequest(mobilePhones):
    auth_token= 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    account_sid = 'xxxxxxxxxxxxxxxxxxxxxx'
    uri = 'https://api.twilio.com/2010-04-01/Accounts/accountSID/Messages.json'
    client = Client(account_sid, auth_token)
    for phoneNumber in mobilePhones:
        phoneNumber = '+1'+phoneNumber
        if re.search("^\+[1-9]\d{1,14}$", phoneNumber):
            client.messages.create(
                to=phoneNumber,
                from_= "+11234567890",
                body = "Hello world",
            )
    
    
Main(currentMonth)
