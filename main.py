import coolsms
import sheet
import config
import schedule
import time

def tracer(func):
    def wrapper():
        try:
            return func()
        except Exception as ex:
            string = '{} 함수에서 에러 발생\n에러코드 : {}'.format(func.__name__, ex)
            print(string)
            return coolsms.SendSMS(config.key_init['sys_admin_phone'], string)
    return wrapper

@tracer
def getSheet():
    first_one, second_one = sheet.contactinfo()

    # 받아온 리스트가 완전하지않으면 참조오류를 삽입합니다
    if len(first_one) == 0:
        first_one.append('참조오류')
    if len(second_one) == 0:
        second_one.append('참조오류')

    content =[first_one[0]+'님 12시 1차 당직입니다!\n'+ config.key_init['URL'],second_one[0]+'님 12시 30분 2차 당직입니다!\n'+ config.key_init['URL']]

    fixedtext = ('오늘 당직자는 '+first_one[0]+', '+second_one[0]+'입니다')

    return [first_one, second_one, content, fixedtext]


#메시지 발송
@tracer
def firstmessage():
    data = getSheet()
    person = data[0]
    text = data[2]
    #1차 문자
    if len(person) != 2:  # 참조오류라면 아래 문구를 출력합니다
        return print('1차 당직자 참조에러')
    coolsms.SendSMS(person[1], text[0])
    print(person[0],person[1],'발송완료!')

@tracer
def secondmessage():
    data = getSheet()
    person = data[1]
    text = data[2]
    #2차 문자
    if len(person) != 2:
        return print('2차 당직자 참조에러')
    coolsms.SendSMS(person[1],text[1])
    print(person[0],person[1],'발송완료!')

@tracer
def fixedmessage():
    text = getSheet()
    #담당자 확인 문자
    coolsms.SendSMS(config.key_init['supervisor'], text[3])
    print('담당자 확인 문자 전송 완료')

@tracer
def adminmessage():
    coolsms.SendSMS(config.key_init['sys_admin_phone'], '당직담당알림 프로그램 정상 운영중')

@tracer
def message():
    schedule.every().day.at("09:00").do(adminmessage)
    schedule.every().day.at("11:30").do(firstmessage)
    schedule.every().day.at("11:32").do(secondmessage)
    schedule.every().day.at("11:34").do(fixedmessage)
    schedule.every().day.at("12:25").do(secondmessage)

#메인
def main():
    message()
    while True:
        print('running')
        schedule.run_pending()
        time.sleep(60)


if __name__=="__main__":
    try:
        main()
    except  Exception as e:
        print(str(e))
        close = ''
        while close != 'close':
            close = input('에러가 발생하여 관리자를 호출했습니다.'
                          '종료를 위해 "close" 를 입력해주세요 : ')



