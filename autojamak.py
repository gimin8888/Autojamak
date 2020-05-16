import pyautogui as pag
import time

pag.FAILSAFE = True

print('프로그램 제작 : 블피 유튜브 / 도움주신 분 : 김코어')

right = str(input('매크로를 시작하기 전 포토샵 자막과 메모장 자막을 꼭 저장해 주시기 바랍니다. 다음으로 넘어가시려면 1을 적어주세요'))

time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 메모장 두번째 줄 자막 글자 맨 왼쪽에 마우스를 대고 있으세요.')
    time_cnt -= 1
    time.sleep(1)

print(pag.position())

japyoX = int(input('화면에 나온 x좌표를 숫자만 적어주세요 japyoX : '))
japyoY = int(input('화면에 나온 y좌표를 숫자만 적어주세요 japyoY : '))

time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 자막이 쓰여질 포토샵 T 부분에 마우스를 대고 있으세요.')
    time_cnt -= 1
    time.sleep(1)

print(pag.position())

japyo2X = int(input('화면에 나온 x좌표를 숫자만 적어주세요 japyo2X : '))
japyo2Y = int(input('화면에 나온 y좌표를 숫자만 적어주세요 japyo2Y : '))

time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 메모장 첫번째 줄 숫자 부분 맨 왼쪽에 마우스를 대고 있으세요.')
    time_cnt -= 1
    time.sleep(1)

print(pag.position())

japyo3X = int(input('화면에 나온 x좌표를 숫자만 적어주세요 japyo3X : '))
japyo3Y = int(input('화면에 나온 y좌표를 숫자만 적어주세요 japyo3Y : '))

time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 메모장 자막 세번째 줄 맨 왼쪽 부분에 마우스를 대고 있으세요.')
    time_cnt -= 1
    time.sleep(1)

print(pag.position())

japyo4X = int(input('화면에 나온 x좌표를 숫자만 적어주세요 japyo4X : '))
japyo4Y = int(input('화면에 나온 y좌표를 숫자만 적어주세요 japyo4Y : '))

# while True: 
#     Choice = input("먼저 좌표를 설정해야 합니다 준비가 되셨으면 1을 입력해주세요") 
#     print(Choice) 
#     Choice_arr.append(Choice)#입력한 동작을 저장 
#     if Choice == '1': 
#         Mouse_in()
#     else : 
#         print("1을 입력하지 않아서 시스템을 종료 합니다") 
#         start() 
#         break

num = 0
num1 = int(input('마지막으로 자막 갯수를 써주세요!(써주신 수만큼 매크로가 반복 실행됩니다!)'))


time_cnt = 5

while time_cnt:
    print(str(time_cnt) + '초 후에 매크로가 시작됩니다. 절대 키보드와 마우스를 움직이지 마세요!')
    time_cnt -= 1
    time.sleep(1)

print('매크로를 종료하시려면 마우스를 맨 왼쪽으로 옮기시면 됩니다')

# print(pyautogui.position())
while num < num1:
    num += 1

    pag.dragTo(japyoX, japyoY)
    pag.drag(900, 0, 1, button='left')

    pag.keyDown('ctrl')
    pag.press('X')
    pag.keyUp('ctrl')

    pag.click(japyo2X, japyo2Y)
    pag.doubleClick(japyo2X, japyo2Y)

    time.sleep(0.5)

    pag.keyDown('ctrl')
    pag.press('v')
    pag.keyUp('ctrl')

    time.sleep(0.5)

    pag.dragTo(japyo3X, japyo3Y)
    pag.drag(100, 0, 0.5, button='left')

    pag.keyDown('ctrl')
    pag.press('X')
    pag.keyUp('ctrl')

    pag.click(japyo2X, japyo2Y)

    pag.keyDown('ctrl')
    pag.keyDown('shift')
    pag.press('S')
    pag.keyUp('ctrl')
    pag.keyUp('shift')

    pag.keyDown('ctrl')
    pag.press('V')
    pag.keyUp('ctrl')

    pag.press('enter')

    pag.click(japyo4X, japyo4Y)
    pag.press('backspace')
    pag.press('backspace')
else :
    # Ctrl+C 입력시 예외 발생
    print('자막이 모두 완성 되었습니다!')

# num7 = pyautogui.locateCenterOnScreen('1.png')
# pyautogui.click(num7)


# pyautogui.scroll(-100)
# scroll up 10 "clicks"

# pyautogui.moveTo(500, None, 2)

# pyautogui.dragTo(100, 200, button='left')

# pyautogui.moveTo(x=23, y=106)
# pyautogui.click(x=23, y=106)

# i = pyautogui.locateOnScreen('7.jpg')

# pyautogui.click(i)

# print(pyautogui.position())

# pyautogui.screenshot('1.jpg', region=(1243, 797, 30, 30))

# num1 = pyautogui.locateCenterOnScreen('1.jpg')
# pyautogui.click(num1)
