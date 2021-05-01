"""
이름, 전화번호, 이메일, 주소를 입력 받아 연락처를 입출, 출력, 삭제하는 프로그램을 작성하세요.
"""


class Contacts:

    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print(f'이름 : {self.name}')
        print(f'전화번호 : {self.phone}')
        print(f'이메일 : {self.email}')
        print(f'주소 : {self.addr}')

    @staticmethod
    def set_contact():
        name = input("이름을 입력하세요. : ")
        phone = input("전화번호를 입력하세요. : ")
        email = input("이메일을 입력하세요. : ")
        addr = input("주소를 입력하세요. : ")
        return Contacts(name, phone, email, addr)

    @staticmethod
    def get_contacts(contact_list):
        for i in contact_list:
            i.print_info()

    @staticmethod
    def del_contact(contact_list, name):
        for i, t in enumerate(contact_list):  # i = index, j = element ( 리스트 내부의 주소 )
            if t.name == name:
                del contact_list[i]

    @staticmethod
    def print_menu():
        print('1. 연락처 입력')
        print('2. 연락처 출력')
        print('3. 연락처 삭제')
        print('4. 연락처 종료')
        menu = input("메뉴를 선택하세요. : ")
        return int(menu)

    @staticmethod
    def main():
        contact_list = []
        while 1:
            menu = Contacts.print_menu()
            if menu == 1:
                t = Contacts.set_contact()
                contact_list.append(t)
            elif menu == 2:
                Contacts.get_contacts(contact_list)
            elif menu == 3:
                name = input("삭제할 이름을 입력하세요. : ")
                Contacts.del_contact(contact_list, name)
            elif menu == 4:
                print("연락처를 종료합니다.")
                break


if __name__ == '__main__':
    Contacts.main()
