import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

import ssl
import config
import sheet

ssl._create_default_https_context = ssl._create_unverified_context

def SendSMS(number,txt):#toNumber):
    # set api key, api secret
    api_key = config.key_init['api_key']
    api_secret = config.key_init['api_secret']

    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['to'] = number #수신번호 Number '01000000000,01000000001'
    params['from'] = config.key_init['sender'] # 발신번호 
    params['text'] = txt#'문자내용
    cool = Message(api_key, api_secret)
    print('successfully sent')

    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])

        if "error_list" in response: 
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)

