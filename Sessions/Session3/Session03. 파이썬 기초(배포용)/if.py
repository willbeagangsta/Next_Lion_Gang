asia = ["한국", "중국", "일본"]
europe = ["영국", "프랑스", "독일"]
america = ["미국", "캐나다", "멕시코"]

inp = input("나라를 입력해주세요: ")

if inp in asia:
    print("아시아 입니다")

elif inp in europe:
    print("유럽입니다")

elif inp in america:
    print("아메리카입니다")

else:
    print("니 똥이다")