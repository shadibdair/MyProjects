
class SchoolMember:
    def tell(self):
        print('hello SchoolMember', end=" ")


class Teacher(SchoolMember):
    def tell(self):
        SchoolMember.tell(self)
        print('and Teacher', end=" ")


class Book(SchoolMember):
    def tell(self):
        Teacher.tell(self)
        print('open your Book please...')





m = SchoolMember()
t = Teacher()
d= Book()

#t.tell()
#m.tell()
d.tell()
"""
OUTPUT:
____________________________________
hello SchoolMember and Teacher
hello SchoolMember
"""