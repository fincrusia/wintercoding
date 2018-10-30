
# 윈터 코딩 과제 : 웹

## 1. 설치/빌드 방법

requirements : python 3.6, Django 2.1

    $ git clone https://github.com/fincrusia/wintercoding.git
    $ cd wintercoding
    $ python3 manage.py runserver

브라우저를 열고 "127.0.0.1:8000/todolist"를 주소창에 입력하여 과제물을 확인하실 수 있습니다.

## 2. 사용법

1. 상단의 "Last Update"에는 현재 시각이 표시됩니다.

2. "TODO List"에는 현재의 모든 TODO들의 정보가 목록으로 주어집니다.

3. "Alarm"에는 완료되지 않은 채로 마감기한을 지난 TODO들이 목록으로 주어집니다.

4. TODO를 추가하고 싶다면 "TODO List"의 최하단에 모든 항목을 입력하고 "Add" 버튼을 누릅니다.

5. 이미 등록된 TODO를 수정하고 싶다면 해당하는 TODO 우측의 "Modify"를 누르고, 수정하고 싶은 항목들만 정보를 입력한 후 다시 한번 "Modify"를 누릅니다.

6. 몇몇 TODO들이 완료되었다면, 각 항목 좌측의 "Select"열에 해당하는 체크박스를 누르고, "TODO List" 하단의 "All selected tasks done"을 클릭하여 "Done" 정보를 "X"에서 "O"로 바꿀 수 있습니다.

7. 몇몇 TODO들을 삭제하기 위해서는, 각 항목 좌측의 "Select"열에 해당하는 체크박스를 누르고, "TODO List" 하단의 "Remove all selected tasks"버튼을 눌러 항목들을 삭제합니다.


## 뷰 테스트 방법 (가산점)

"wintercoding" 디렉토리에서 다음을 수행합니다:

    $ python manage.py test todolist.tests.Testing.test


## 배포 (가산점)

다음 주소에서 배포된 사이트를 확인하실 수 있습니다:
    http://fincrusia.pythonanywhere.com/todolist/