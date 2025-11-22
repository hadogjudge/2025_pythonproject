from timeit import repeat

score = int(input("점수를 입력하세요."))

if score >=  80:
    print("합격입니다.")
elif score >=60:
    print("재시험 응시가 필요합니다.")
else:
    print("불합격입니다.")

if score < 100 or score > 0:
    print("정상적인 점수 범위가 아닙니다.")

   # while True:
    #    user_input = input("값을 입력하세요 : ")

#        if user_input.lower() == "z"
#            break
input_number = int(input("숫자를 입력하세요. "))
index = 1

while index <= input_number:
    print(index)
    if index % 2 == 0:
      print(index)
    index = index + 2

    print("피보나치 수열")
    list = [1,1]

    while list[len(list)-1] < input_number:
       print(list_item)
    list.append(list_item + list[len(list)-2])
    list_item = list[len(list)-1]

print("피보나치 수열 without list")
a = 1
b = 1
c = 1

while c <= input_number:
    print(c)
    c = a + b
    a = b
    b = c
def print_even():


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

