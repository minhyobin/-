player = 0

try:
    print("모든 답은 숫자로 입력하시오. Q1. 당신은 어순이 같은 언어를 좋아하는가?\
             \n 1.그렇다\n 2.아니다\n")
    choice = int(input("나는?"))
    if choice == 1:
        player =+ player+1
    elif choice == 2:
        player =+ player+2
    else:
        raise ValueError

    print("Q2. 흔히 접할 수 있는 언어를 사용하고 싶은가?\
             \n 1.그렇다\n 2.아니다\n")
    choice = int(input("나는?"))
    if choice == 1:
        player =+ player+1
    elif choice == 2:
        player =+ player+2
    else:
        raise ValueError
        
    print("Q3. 특정 상황을 제외하고 발음이 같은 언어가 좋다.\
             \n 1.그렇다\n 2.아니다\n")
    choice = int(input("나는?"))
    if choice == 1:
        player =+ player+1
    elif choice == 2:
        player =+ player+2
    else:
        raise ValueError

    if player <= 3:
        print("당신의 점수는 {0}점이며, 일본어를 추천합니다.".format(player))
    elif player >= 4 and player < 5:
        print("당신의 점수는 {0}점이며, 스페인어를 추천합니다.".format(player))
    else:
        print("당신의 점수는 {0}점이며, 영어를 추천합니다.".format(player))

except ValueError:
    print("잘못된 값을 입력하였습니다.")

    
