import random
students = {
    10101: "오해원",
    10102: "조준상",
    10103: "서아인",
    10104: "이동균",
    10105: "정준혁",
    10106: "이정현",
    10107: "장희상",
    10108: "김세훈",
    10109: "임태안",
    10110: "심지환",
    10111: "이도현",
    10112: "박하늘별님구름햇님보다사랑스러우리",
    10113: "최강록",
    10114: "젠슨 황",
    10115: "리사 수",
    10116: "일론 머스크",
    10117: "블루 브림",
    10118: "무토 유우기",
    10119: "벨로리빗샤",
    10120: "이승만",
    10121: "오벨리스크의 거신병",
    10122: "안노히데아키",
    10123: "피카츄",
    10124: "요리괴물",
}
pool = list(students.keys())

seat = [[None,None,None,None,None,None],
        [None,None,None,None,None,None],
        [None,None,None,None,None,None],
        [None,None,None,None,None,None],]
ranIndex = random.randrange(0,len(pool))

randRow = random.randint(0,len(seat)-1)
randcol = random.randint(0,len(seat[0])-1)

print(pool[ranIndex])
print(randRow)
print(randcol)

seat[randRow][randcol] = pool[ranIndex]

for i in range(len(seat)):
    print(seat[i])

pool.remove(pool[ranIndex])
print(randRow)
print(randcol)

seat[randRow][randcol] = pool[ranIndex]

for i in range(len(seat)):
    print(seat[i])

pool.remove(pool[ranIndex])
print(randRow)
print("-----------------------")
