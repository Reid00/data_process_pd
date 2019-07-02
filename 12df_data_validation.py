import pandas as pd

students = pd.read_excel('students.xlsx', sheet_name='students')


# 数据校验
def score_validation(row):
    try:
        assert 0 < row.score < 100
    except:
        print(f'student id: {row.id}\t name {row.Name}\tthe score {row.score} is invalid')


students.apply(score_validation, axis=1)

# print(students.head())
