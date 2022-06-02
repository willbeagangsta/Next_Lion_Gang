



#3. 입력받은 줄 수 만큼 별을 오른쪽 정렬로 표시하는 프로그램을 작성해주세요
# 예:
#     *
#    **
#   ***
#  ****
count = 1

while count <5:
    print(" " * (5-count) + "*" * count)
    count += 1