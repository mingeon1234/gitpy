arr=[1,2,3,4,"안니영",True]
num = 1


while num == 2 :
    print(1)
else:
    print(3)


for i in range(1,10,1):
    print(i)

# 빈 리스트 생성 방법

arr = []
arr2 = list()

print(arr)
print(arr2)

arr = [1,2,3,"안녕",True]
print(arr[3]) # 안녕 출력
print(arr[-3]) # 3 출력

# append() # 요소의 추가


arr.append("2")


for i in range(0, len(arr), 1) :
    print(arr[i])

arr = [[1,2,3,4],[5,6,7,8]]
print(arr) # [[1,2,3,4],[5,6,7,8]]
print(arr[0]) # [1,2,3,4]
print(arr[1]) # [5,6,7,8]

arr2 = [1,2,3,4]

print(arr[0][0])


arr = [4,2,1,-20,10,-20,-20]
arr.sort() # 오름차순
print(arr)

# reverse() 현재 리스트 뒤집기
arr.reverse()
print(arr)

# count(x) 요소 x 개수 새기

print(arr.count(-20))

# remove(x) 요소 x 없애기

arr.remove(-20)
print(arr) # -20(같은 값이) 여러개라면 가장 앞의 값 삭제

for i in range(arr.count(-20)):
    arr.remove(-20)

print(arr)

# insert(인덱스, 값) 특정 위치에 요소를 삽입

arr.insert(3,-20)
print(arr)

# index(값) 특정 값의 요소 위치

print(arr.index(-20)) # insert에서 3번째 위치에 넣어서 3이 출력