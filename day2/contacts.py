"""
방법 2 _ 간소화 ( 리팩토링 )
이름, 전화번호, 이메일, 주소를 입력 받아 연락처를 입출, 출력, 삭제하는 프로그램을 작성하세요.
"""


class Contacts:
    name = ''
    phone = ''
    email = ''
    addr = ''

    def __str__(self):
        return f'이름 : {self.name} \n' \
               f'전화번호 : {self.phone} \n' \
               f'이메일 : {self.email} \n' \
               f'주소 : {self.addr}'


class ContactsService:

    def set_contact(self):
        obj = Contacts()
        obj.name = input("이름을 입력하세요. : ")
        obj.phone = input("전화번호를 입력하세요. : ")
        obj.email = input("이메일을 입력하세요. : ")
        obj.addr = input("주소를 입력하세요. : ")
        return obj

    def get_contacts(self, contact_list):
        for i in contact_list:
            print(i)

    def del_contact(self, contact_list, name):
        for i, t in enumerate(contact_list):  # i = index, j = element ( 리스트 내부의 주소 )
            if t.name == name:
                del contact_list[i]

    def print_menu(self):
        print('1. 연락처 입력\n'
              '2. 연락처 출력\n'
              '3. 연락처 삭제\n'
              '4. 연락처 종료')
        menu = input("메뉴를 선택하세요. : ")
        return int(menu)

    @staticmethod
    def main():
        contact_list = []
        service = ContactsService()
        while 1:
            menu = service.print_menu()
            if menu == 1:
                t = service.set_contact()
                contact_list.append(t)
            elif menu == 2:
                service.get_contacts(contact_list)
            elif menu == 3:
                name = input("삭제할 이름을 입력하세요. : ")
                service.del_contact(contact_list, name)
            elif menu == 4:
                print("연락처를 종료합니다.")
                break


if __name__ == '__main__':
    ContactsService.main()
