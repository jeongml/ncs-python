class Person:

    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def greeting(self):
        print(f'안녕하세요. 제 이름은 {self.name}이고,'
              f' 나이는 {self.age}살이고,'
              f' {self.addr}에서 거주합니다.')

    @staticmethod
    def main():
        maria = Person('마리아', 20, '서울')
        maria.greeting()
        tom = Person('톰', 17, '대전')
        tom.greeting()


if __name__ == '__main__':
    Person.main()

