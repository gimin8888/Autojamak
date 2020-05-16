import pyautogui as pag
import time

pag.FAILSAFE = True

print('프로그램 제작 : 블피 유튜브 / 도움주신 분 : 김코어')

right = str(input('매크로를 시작하기 전 포토샵 자막과 메모장 자막을 꼭 저장해 주시기 바랍니다. 다음으로 넘어가시려면 1을 적어주세요'))

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