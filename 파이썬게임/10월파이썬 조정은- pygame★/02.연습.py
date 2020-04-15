import pygame #pygame라이브러리 호출
import random #random 라이브러리 호출
from time import sleep

WHITE = (255,255,255) #배경색 흰색 코드
background_height = 768 #배경 세로 길이
aircraft_width = 124
aircraft_heigth = 100


devil_width = 85 #적 비행기의 가로 세로 크기 -> 총알이 명중했는지 파악하기 위해 필요



def gameOver():
    global screen
    dispMessage("Game Over")

def airplane(x,y): #비행기 함수 선언
    global screen, aircraft
    screen.blit(aircraft,(x,y)) #이미지를 스크린에 위치시킴

def back(background,x,y): #배경 함수 선언
    global screen
    screen.blit(background,(x,y))

def drawObject(obj,x,y):
    global screen
    screen.blit(obj,(x,y))


def runGame(): #게임구동함수 선언
    global screen, clock, aircraft, background1, background2
    global devil, bullet, boom

    Shot = 0 #명중한 횟수
    boom_count =0 #폭발 이미지가 화면에 표시되는 시간 변수

    devil_x = random.randrange(0,650) #적이 나타날 위치 가로 범위내에서 랜덤으로 선정
    devil_y = 0  #세로 범위

    bullet_xy = [] #총알 키를 누를때마다 총알 좌표 추가되는 리스트
    passed = 0

    x = 1024*0.45
    y = 768*0.8 #비행기 위치 선정
    x_change = 0 #비행기가 가로로 움직일거라 x_change변수 선언 -> x좌표 변화
    y_change = 0 #비행기 세로 위치 변수

    background1_y = 0 #배경이미지 왼쪽상단 모서리 좌표 0 지정
    background2_y = -background_height #두번째 배경을 원본 바로 다음에 위치 시키도록 좌표 지정

    end = 0 #while문을 위한 변수
    while end == 0: #무한반복
        for event in pygame.event.get(): #게임판에서 발생하는 이벤트 리턴
            if event.type == pygame.QUIT:
                end +=1
                #event type이 종료 -> false가 되어 while문을 빠져나옴

            if event.type == pygame.KEYDOWN: #KEYDOWN : 키를 눌렀을때
                if event.key == pygame.K_RIGHT: #오른쪽 방향키 : 오른쪽으로 5 만큼 이동
                    x_change = +5
                elif event.key == pygame.K_LEFT: #왼쪽 방향키 : 왼쪽으로 5만큼 이동
                    x_change = -5
                elif event.key == pygame.K_UP: #위 방향키 : 위로 5 만큼 이동
                    y_change = -5 #높이는 위에서부터 아래로내려오는게 (+)이므로 부호 반대
                elif event.key == pygame.K_DOWN: #아래 방향키 : 아래로 5만큼 이동
                    y_change = +5
                elif event.key == pygame.K_LCTRL: #컨트롤키 : 총알 발사
                    bullet_x = x + aircraft_width/2 #총알의 x좌표 = 현재비행기x좌표 +비행기너비/2
                    bullet_y = y  #총알의 y좌표 = 현재 비행기 y좌표
                    bullet_xy.append([bullet_x,bullet_y]) #좌표 설정후 list에 추가
                elif event.key == pygame.K_SPACE: #스페이스바 누르면 5초 정지
                    sleep(5)

            if event.type == pygame.KEYUP: #키를 안누를때
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0 #움직임 없음
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0 #움직임 없음

        x += x_change
        y += y_change
        if y < 0:
            y = 0

        screen.fill(WHITE) #스크린을 흰색으로 채움

        background1_y += 2 #내려오게 만들게 +2
        background2_y += 2

        if background1_y == background_height:
            background1_y = -background_height

        if background2_y == background_height:
            background2_y = -background_height

        back(background1,0,background1_y)
        back(background2,0,background2_y) #배경이미지 게임판에 채우기 위해 좌상단 모서리 x좌표와 y좌표 back함수에 전달


        if passed > 2:
            gameOver()


        devil_y += 4 #y좌표를 4씩 밑으로 움직임
        # devil1_y += 3
        if devil_x <= 0 or devil_y >= 768: #왼쪽 끝까지 날아가거나 가장 하단으로 내려오면
            passed += 1 #지나감 1추가
            devil_x = random.randrange(0,650)  #새로 날아올 적 위치 잡음
            devil_y = 0


        if len(bullet_xy) != 0: #총알 좌표 리스트가 비어있지 않으면
            for i, bxy in enumerate(bullet_xy): #리스트에서 하나씩 추출해서 좌표 갱신
                bxy[1] -= 15 #y좌표를 +15씩 -> 15픽셀로 날아가도록
                bullet_xy[i][1] = bxy[1]

                if bxy[1] < devil_y: #총알이 적보다 더 위에 위치하면
                    if bxy[0] > devil_x and bxy[0] < devil_x + devil_width:
                        #적의 너비안에 총알의 x좌표가 들어오는 경우 -> 명중
                        bullet_xy.remove(bxy) #총알의 좌표를 리스트에서 삭제
                        Shot += 1
                if bxy[1] <= 0:
                    try :
                        bullet_xy.remove(bxy)
                    except:
                        pass
            for bx, by in bullet_xy:
                drawObject(bullet,bx,by) #총알 호출
        if Shot <= 3: #3발이하로 맞으면
            drawObject(devil,devil_x,devil_y) #적비행기 계속해서 화면에 띄워줌
        else: #3발 이상 맞으면

            drawObject(boom,devil_x-15,devil_y-15) #폭발하는 이미지 호출
            boom_count += 1
            if boom_count > 7:
                boom_count = 0
                devil_x = random.randrange(0,650)
                devil_y = random.randrange(-900,0)
                Shot = 0


        drawObject(devil,devil_x,devil_y) #적 호출
        airplane(x,y) #비행기 호출


        pygame.display.update()#그리고 지우고 반복
        clock.tick(50) #초당프레임값을 30으로 지정하여 while문 반복

    pygame.quit() #게임 종료
    quit()

def initGame(): #게임 시작/초기화 함수 선언
    global screen, clock, aircraft, background1, background2
    global devil, bullet, boom

    pygame.init() #pygame라이브러리 초기화 (최초호출 항상 필요)
    screen = pygame.display.set_mode((1024,768)) #스크린 크기 지정
    pygame.display.set_caption("FlyingGame") #게임판 이름 지정
    aircraft = pygame.image.load("./비행기이미지.png")
    background1 = pygame.image.load("./배경.jpg")
    background2 = background1.copy() #원본 복사
    boom = pygame.image.load("./폭발.png")
    devil = pygame.image.load("./적1.png")
    bullet = pygame.image.load("./총알1.png")
    clock = pygame.time.Clock() #초당프레임(FPS)설정을 위한 변수
    runGame() #게임 러닝 함수 호출


initGame() #초기화 함수 선언 -> 시작
