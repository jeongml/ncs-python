from selenium import webdriver
from bs4 import BeautifulSoup


class NaverMovie(object):
    chromdriver = 'C:\Program Files\Google\Chrome\chromedriver'
    url = ''

    def scrap(self):
        driver = webdriver.Chrome(self.chromdriver)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {"class", "tit3"})
        cnt = 0
        print("===== 영화 순위 =====")
        for i in [div.a.string for div in all_div]:
            cnt += 1
            print(str(cnt) + "위 : " + i)
        driver.close()

    @staticmethod
    def main():
        naver = NaverMovie()
        naver.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        naver.scrap()


if __name__ == '__main__':
    NaverMovie.main()
