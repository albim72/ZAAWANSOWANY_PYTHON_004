from homework import Homework
from exam import Exam
from grade import ExamD

print("___klasa Homework___")
gl = Homework()
gl.grade = 96
assert gl.grade == 96
print(gl.grade)

print("___klasa Exam___")
st = Exam()
st.writing_grade = 84
st.math_grade = 72

assert st.writing_grade == 84
assert st.math_grade == 72

print(f"ocena writing {st.writing_grade}")
print(f"ocena math {st.math_grade}")

# e = st._check_grade(678)
# print(e)

print("___klasa Grade___")
first_ex = ExamD()
first_ex.math_grade = 45
first_ex.writing_grade = 50
first_ex.science_grade = 32
print("Egzamin - pierwszy termin")
print(f"ocena math {first_ex.math_grade}")
print(f"ocena writing {first_ex.writing_grade}")
print(f"ocena science {first_ex.science_grade}")

sec_ex = ExamD()
sec_ex.math_grade = 55
sec_ex.writing_grade = 78
sec_ex.science_grade = 63
print("Egzamin - drugi termin")
print(f"ocena math {sec_ex.math_grade}")
print(f"ocena writing {sec_ex.writing_grade}")
print(f"ocena science {sec_ex.science_grade}")

print("Egzamin - jeszcze raz pierwszy termin")
print(f"ocena math {first_ex.math_grade}")
print(f"ocena writing {first_ex.writing_grade}")
print(f"ocena science {first_ex.science_grade}")
