#함수를 '1개만' 작성해 공백으로 구분되어 입력받은 두 정수의 합, 차, 곱, 몫, 나머지를 한 줄씩 순서대로 출력하세요
def arsenal(a,b):
    cal = []
    cal.append(a+b)
    cal.append(a-b)
    cal.append(a-b)
    cal.append(a-b)
    cal.append(a-b)
    return cal


a, b = map(int, input().split())
for i in arsenal(a,b):
    print(i)