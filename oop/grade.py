"""
클래스에 학생의 이름을 입력하고, 해당 학생이 얻은 3과목의 평균 점수에 따라 A ~ F 까지의 등급을 출력하세요.
해당 문제를 해결하기 위해서는 교제 72p의 리스트를 참조하세요.
"""


class Grade:

    def __init__(self, name):
        self.name = name
        self.marks = []     # list로 초기화

    def addMarks(self, mark):
        self.marks.append(mark)

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def main():
        student_name = Grade(input("학생 이름 입력 : "))
        for subject in ['국어', '영어', '수학']:
            student_name.addMarks(int(input(subject + " 점수 입력 : ")))
        subject_avg = student_name.avg()
        if subject_avg >= 90:
            grade = "A"
        elif subject_avg >= 80:
            grade = "B"
        elif subject_avg >= 70:
            grade = "C"
        elif subject_avg >= 60:
            grade = "D"
        elif subject_avg >= 50:
            grade = "E"
        else:
            grade = "F"
        print(f'{student_name.name}이의 세 과목의 평균 점수는 {int(subject_avg)}점, 학점은 {grade} 이다.')


if __name__ == '__main__':
    Grade.main()
