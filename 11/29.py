import random


def up_down_game():

    answer = random.randint(1, 100)
    attempts = 0  # 시도 횟수

    print("UP DOWN 게임을 시작합니다!")
    print("1부터 100 사이의 숫자를 맞춰보세요.")

    while attempts < 10000:
        try:

            user_input = int(input(f"시도 {attempts + 1}번째: 숫자를 입력하세요: "))


            if user_input == answer:
                print(f"정답! {answer}를 맞추셨습니다!")
                break
            elif user_input < answer:
                print("UP! 더 큰 숫자를 입력해 보세요.")
            else:
                print("DOWN! 더 작은 숫자를 입력해 보세요.")

            attempts += 1
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")


    if user_input != answer:
        print(f"실패! 정답은 {answer}였습니다.")


up_down_game()


import random


word_dict = {
    "Apple": "사과",
    "Banana": "바나나",
    "Grapes": "포도",
    "Orange": "오렌지",
    "Melon": "멜론",
    "Pear": "배",
    "Peach": "복숭아",
    "Watermelon": "수박",
    "Strawberry": "딸기",
    "Pineapple": "파인애플"
}

# 객관식 문제를 위한 선택지 준비
def generate_choices(correct_answer, word_dict):
    choices = [correct_answer]
    while len(choices) < 4:
        random_word = random.choice(list(word_dict.values()))
        if random_word not in choices:
            choices.append(random_word)
    random.shuffle(choices)
    return choice
