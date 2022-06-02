class Calculator:
    def __init__(self,name,age):
        self.name = name
        self.result = 0
        self.age = age

    def add(self,num):
        self.result += num
        return self.result

    def sub(self,num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        if (num == 0) :
            print("0으로 나누지 마라")
            return None
        
        self.result /= num
        return self.result

calculator1 = Calculator("김하경",24)
calculator1.mul(2)

print(calculator1.name)