# 빈 튜플 선언
t1 = ()

print(t1) # () 튜플 / {} set [] / 리스트 / {:} 딕셔너리

# 생성, 수정, 추가, 삭제 불가

t2 = {1,2,3,4}

t2 = {1, '2', '3'}

num1, str1, str2 = t2
print(num1, str1, str2)

# set = 집합
s1 = set([1,2,3]) # == s1 = {1,2,3}
s2= set([2,3,4,5])

# set 관련 함수
# .add(n) - 값 n을 추가 (아마 하난듯)

print(s1)
s1.add(9)
print(s1)

# .update() - 값 여러개 추가
print(s1)
s1.update([1,2,3,4,5])
print(s1)

# .remove() - 해당 값 삭제 (해당 값이 없을 시 오류)
s1.remove(3)
print(s1)

# .discard() - 해당 값 삭제 (해당 값이 없어도 실행. 오류x)
s1.discard(3)
print(s1)

# 합집합
print(s1 | s2)
print(s1.union(s2)) # .union()

# 교집합
print(s1 & s2)
print(s1.intersection(s2)) # .intersection()

# 차집합
print(s1 - s2)
print(s1.difference(s2)) # .difference()

# 대칭차집합
pirnt(s1 ^ s2)

# 함수 
arr = [2,3,4,-2,10]
total = sum(arr)

# arr은 기능을 실행하기 위한 인자 값으로 매개변수에 할당
# sum() 함수의 반환 값은 변수 total 할당

# sum() = (리스트나 튜플)에 사용하며 숫자로 이루어진 자료형에 한해 총 합을 구함

arr = [2,3,4,5,6]
print(sum(arr)) # 20

# min() - 최솟값 함수
print(min(arr))

# max() - 최댓값 함수
print(max(arr))

# pow(a, b) - 거듭제곱
print(pow(6,3))

def test():
    print("x")

def print_hello(to1, to2):
    print("hello", to1, to2)

print_hello('data','data3')