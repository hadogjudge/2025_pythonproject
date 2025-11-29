import random


def up_down_game():

    answer = random.randint(1, 100)
    attempts = 0  # 시도 횟수

    print("UP DOWN 게임을 시작합니다!")
    print("1부터 100 사이의 숫자를 맞춰보세요.")

    while attempts < 5:
        try:

            user_input = int(input(f"시도 {attempts + 1}번째: 숫자를 입력하세요: "))


            if user_input == answer:
                print(f"정답! {answer}를 맞추셨습니다!")
                break
            elif user_input < answer:
                print("업")
            else:
                print("다운")

            attempts += 1
        except ValueError:
            print("잘못된 입력입니다.")


    if user_input != answer:
        print(f"실패! 정답은 {answer}였습니다.")



up_down_game()
