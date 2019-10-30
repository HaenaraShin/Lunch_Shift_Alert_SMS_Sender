# Lunch_Shift_Alert_SMS_Sender
**🥪 점심당직알림 문자발송 서비스**

## Purpose
점심 당직자가 까먹지 않도록 점심시간 이전에 미리 SMS 문자를 발송하여 까먹지 않게 한다. 또한 당직명단 관리자는 당직 명단을 구글 시트를 통해 간단하게 관리한다.

## How it works
### 당직자 미리 알림
-	💁 누구에게 : 당일 당직자 2명 (12:00~12:30, 12:30~13:00)
-	⏰ 언제     : 당일 당직 전 (11:30, 12:25)
-	✉️ 어떻게   : SMS 발송 1회 ([CoolSMS API](https://www.coolsms.co.kr/) 서비스)

### 당직자 명단 관리 
-	📅 매월 당직자 명단을 업로드 및 수정
-	☎️ 당직자의 연락망을 업로드 및 수정
-	📄 Google Docs를 이용하여 당직자 명단 문서 공유 및 관리


## Google Sheet Sample Format
TBD


# Basic Usage
```
$ python main.py
```


License
--------
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.