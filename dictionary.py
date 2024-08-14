# 사전 (dictionary)
# key-value pair(키 - 값 쌍)
# key, value는 정수가 아니여도 된다.

my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(my_dictionary[3])
# 값 9 받아온다

my_dictionary[9] = 81
# 9라는 key에 81이라는 값을 추가한다.


# 이런식으로 문자열이 될 수 있다.
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

print(my_family.values())
for value in my_family.values():
    print(value)

print(my_family.keys())
for key in my_family.keys():
    print(key)

for key, value in my_family.items():
    print(key, value)