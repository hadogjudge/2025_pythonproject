#repeat_function()
arr = ['AA' , 'BB' , 'CC' , 'DD']

for i in  arr:
    print(i)

test = [{'answer': [1,3,2,4,5,1,2,3,4]},
{'answer': [1,1,1,1,1,1,1,1,1]},
{'answer': [1,4,2,3,5,2,4,3,2]},
{'answer': [1,3,2,4,5,1,2,3,4]},
{'answer': [1,4,2,4,4,2,1,3,4]},
{'answer': [3,4,2,2,1,4,3,5,4]},]
a =  [1,3,2,4,5,1,2,3,4]
correct_answer = [1,3,2,4,5,1,2,3,4]
for (student, correct) in zip(a, correct_answer):
    print(student , '/' , correct)



test = [
    {
        'name': 'aaa',
        'number': 10101,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'bbb',
        'number': 10102,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'ccc',
        'number': 10103,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'ddd',
        'number': 10104,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'eee',
        'number': 10105,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    }
]
correct_answer = {
    'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
}
for student in test:
    math_score = get_score(student['math'], correct_answer['math'])
    korean_score = get_score(student['korean'], correct_answer['korean'])
    english_score = get_score(student['english'], correct_answer['english'])
    science_score = get_score(student['science'], correct_answer['science'])

    print("수학점수:", math_score)
    print("국어점수:", korean_score)
    print("영어점수:", english_score)
    print("과학점수:", science_score)

print("학생", student['name'], "==================")

# for 중첩
# student.keys(), (이름이거나, 학번인 경우) or (배열이 아닌경우) continue

math_score = get_score(student['math'], correct_answer['math'])
korean_score = get_score(student['korean'], correct_answer['korean'])
english_score = get_score(student['english'], correct_answer['english'])
science_score = get_score(student['science'], correct_answer['science'])

print("수학점수:", math_score)
print("국어점수:", korean_score)
print("영어점수:", english_score)
print("과학점수:", science_score)
