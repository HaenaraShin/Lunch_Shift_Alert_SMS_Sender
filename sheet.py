import gspread
import time
import datetime
from oauth2client.service_account import ServiceAccountCredentials

def contactinfo():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
    client = gspread.authorize(creds)
    
    contacts=[]
    name=[]
    contacts_return=[]
    first_contact = []
    second_contact = []
    
    #시간 
    time=datetime.datetime.now()
    secondtime=time.date()
    third = secondtime.strftime('%Y-%m-%d')

    
    today = datetime.datetime.today()
    month=today.strftime('%Y-%m')

    #당직 명단 
    sheet1=client.open('당직명단').worksheet(month)
    firstpage=sheet1.get_all_values()

    #연락처 명단
    sheet2=client.open('당직연락처').worksheet("Contact").get_all_records()

    #날짜/현재 날짜 & 이름 연락처 일치
    
    for firstpage_row in firstpage:
        if firstpage_row[0] == third:
            for sheet2_row in sheet2:
                if sheet2_row['이름']== firstpage_row[1]:
                    first_contact.append(sheet2_row['이름'])
                    temp = sheet2_row['연락처']
                    a = temp.replace("-","")
                    first_contact.append(a)
                if sheet2_row['이름']==firstpage_row[4]:
                    second_contact.append(sheet2_row['이름'])
                    temp = sheet2_row['연락처']
                    a = temp.replace("-", "")
                    second_contact.append(a)
    return first_contact, second_contact


