class Calculator:

    # 선언부
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    # 실행부
    @staticmethod
    def execute():
        calc = Calculator(int(input("첫번째 수 : ")), int(input("두번째 수 : ")))
        # print(f'첫번째 수 : {calc.first}')
        # print(f'두번째 수 : {calc.second}')
        print(f'{calc.first} + {calc.second} = {calc.sum()}')
        print(f'{calc.first} - {calc.second} = {calc.sub()}')
        print(f'{calc.first} * {calc.second} = {calc.mul()}')
        print(f'{calc.first} / {calc.second} = {calc.div()}')


if __name__ == '__main__':
    Calculator.execute()

