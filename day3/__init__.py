from day3.views.controller import Controller
from day3.templates.plot import Plot

if __name__ == '__main__':
    def print_menu():
        print('0. EXIT')
        print('1. 시각화')
        print('2. 모델링')
        print('3. 머신러닝')
        print('4. 머신생성')
        return input('메뉴를 입력하세요. : ')

    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            print('---------- 시각화 실행 ----------')
            plot = Plot('train.csv')
            menu = input('차트내용 선택 \n'
                         '1. 생존자 vs 사망자 \n'
                         '2. 생존자 성별 대비 \n')
            if menu == '1':
                plot.plot_survived_dead()
            if menu == '2':
                plot.plot_sex()
        if menu == '2':
            print('---------- 모델링 실행 ----------')
            app.modeling('train.csv', 'test.csv')
        if menu == '3':
            print('---------- 머신러닝 실행 ----------')
            app.learning('train.csv', 'test.csv')
        if menu == '4':
            print('---------- 머신생성 실행 ----------')
            app.submit('train.csv', 'test.csv')
        elif menu == '0':
            break
