from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance,0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Ocena musi zawierać się w przedziale 0-100')
        self._values[instance] = value

class ExamC:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

#     def __init__(self,math,writ,sci):
#         self.math_grade = math
#         self.writing_grade = writ
#         self.science_grade = sci
#
# ec = ExamC(Grade(),Grade(),Grade())

#     def __init__(self):
#         self.math_grade = Grade()
#         self.writing_grade = Grade()
#         self.science_grade = Grade()
#
# ec = ExamC()
# ec.science_grade(56)

