# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보세요. (단 입력으로 들어오는 수의 개수는 정해져 있지 않으며,
# 입력값으로 -1이 들어오면 더 이상 값을 받지 않는다.)

"""
[힌트]
1. 입력값을 받는 함수는 input함수입니다.
예시) core = input("양의 정수를 입력해주세요: ")

2. 입력으로 숫자가 몇 개가 들어올 지 모르는 상황입니다. 이 경우에는 일단 계속 반복을 하다가, 특정 조건인 경우에 반복문을 탈출해야 겠죠?

3. 입력된 숫자는 리스트에 저장을 해놨다가, 이후 평균을 계산할 때 이용해보세요!

어려우시면 운영진에게 언제든 물어보세요~
"""

###########################################################


Arsenal = []
count = 0



while True:
    Highbury = int(input("원하는 숫자를 입력하세요, -1을 입력하면 종료됩니다: "))
    if Highbury > -1:
        Arsenal.append(Highbury)
        
        print("지금까지 평균은 %f 입니다. 계속 입력해보세요" % (sum(Arsenal)/len(Arsenal)))

    elif Highbury < -1:
        Arsenal.append(Highbury)
        
        print("지금까지 평균은 %f 입니다. 계속 입력해보세요" % (sum(Arsenal)/len(Arsenal)))
    else:
        print("종료되었습니다.")
        break;
        


if count > 0:
    print("지금까지 평균은 %f 입니다." %(Sum/count))