# 로또 당첨 번호 확인
from tkinter import * # tkinter 라이브러리 호출

win = Tk() # 창 실행

win.title('로또 당첨 번호 확인') # 창 제목
win.geometry('300x200') # 창 크기
win.option_add('*Font', '맑은고딕 10') # 창 내용 폰트

# 확인 회차 입력
lab1 = Label()
lab1.config(text = '확인하고 싶은 회차를 입력하세요')
lab1.pack(side = TOP, pady = 5)


# 회차 입력
ent = Entry(win)
ent.config(justify = CENTER)
ent.pack(side = TOP, pady = 5)

# 로또 번호 크롤러 함수
def lotto_p():
    import requests
    from bs4 import BeautifulSoup
    n = ent.get()
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={0}'.format(n)
    # div class='win_result'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    txt = soup.find('div', attrs={'class','win_result'}).get_text()

    num_list = txt.split('\n')[7:13]
    bonus = txt.split('\n')[-4]

    if bonus == '':
        num_list = '아직 진행되지 않은 회차입니다'
        bonus = '다른 회차를 검색하세요'
    
    if n == '':
        num_list = '회차를 입력해주세요.'
        bonus = ''

    lab3.config(text = num_list)
    lab5.config(text = bonus)

btn = Button(win)
btn.config(text='로또 당첨 번호 확인')
btn.config(command = lotto_p)
btn.pack(side = TOP, pady = 5)

# 로또 당첨번호 라벨
lab2 = Label()
lab2.config(text = '당첨번호')
lab2.pack(side = TOP, pady = 5)

# # 로또 당첨번호 출력 라벨
lab3 = Label()
lab3.pack()

# 로또 보너스번호 라벨
lab4 = Label()
lab4.config(text = '보너스번호')
lab4.pack(side = TOP, pady = 5)

# # 로또 보너스번호 출력 라벨
lab5 = Label()
lab5.pack()

win.mainloop()