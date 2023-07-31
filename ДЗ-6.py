class Student:
    def __init__(self, name, grup_num, age):
        self.name=name
        self.grup_num=grup_num
        self.age=age
    def get_name(self):
        student_num=int(input('имя которого номера студента хотите увидеть? '))
        if student_num==1:
            print(studenty1.name)
        elif student_num==2:
            print(studenty2.name)
        elif student_num==3:
            print(studenty3.name)
        elif student_num==4:
            print(studenty4.name)
        elif student_num==5:
            print(studenty5.name)
        else:
            print('унас имеется информация всего 5ти студентов')
    def get_grup_num(self):
        name_stu = input('группа какого студента хотите увидет? ')
        if name_stu == studenty1.name:
            print(studenty1.grup_num)
        elif name_stu == studenty2.name:
                print(studenty2.grup_num)
        elif name_stu == studenty3.name:
            print(studenty3.grup_num)
        elif name_stu == studenty4.name:
                print(studenty4.grup_num)
        elif name_stu == studenty5.name:
                print(studenty5.grup_num)
        else:
            print('к сожелению у нас нет студента под таким именем')
    def get_age(self):
        name_stu = input('возраст какого студента хотите увидет? ')
        if name_stu==studenty1.name:
            print(studenty1.age)
        elif name_stu==studenty2.name:
            print(studenty2.age)
        elif name_stu==studenty3.name:
            print(studenty3.age)
        elif name_stu==studenty4.name:
            print(studenty4.age)
        elif name_stu==studenty5.name:
            print(studenty5.age)
        else:
            print('к сожелению у нас нет студента под таким именем')
    def set_grup_num(self, new_num):
        self.grup_num=new_num
    def set_age(self, new_age):
        self.age=new_age

studenty1=Student(name='Pavel', grup_num='9a', age=16)
studenty2=Student(name='Jordan', grup_num='10b', age=17)
studenty3=Student(name='Bill', grup_num='8d', age=15)
studenty4=Student(name='Smith', grup_num='9d', age=16)
studenty5=Student(name='Aleks', grup_num='8a', age=15)

while True:
    print('---------------------------------','\n''1-покозат имя студента','\n''2-показат группу студента',
          '\n''3-покозат возраст студента','\n''4-изменит группу студента','\n''5-изменит возраст студента')
    operator=int(input('виберайте: '))
    if operator==1:
        studenty1.get_name()
    elif operator==2:
        studenty1.get_grup_num()
    elif operator==3:
        studenty1.get_age()
    elif operator==4:
        name_stu = input('группа какого студента хотите изменит? ')
        change_num=input('на какую группу изменит? ')
        if name_stu==studenty1.name:
            studenty1.set_grup_num(change_num)
        elif name_stu==studenty2.name:
            studenty2.set_grup_num(change_num)
        elif name_stu==studenty3.name:
            studenty3.set_grup_num(change_num)
        elif name_stu==studenty4.name:
            studenty4.set_grup_num(change_num)
        elif name_stu==studenty5.name:
            studenty5.set_grup_num(change_num)
        else:
            print('к сожелению у нас нет студента под таким именем')
    elif operator==5:
        name_stu = input('возраст какого студента хотите изменит? ')
        change_num=input('на какой возраст изменит? ')
        if name_stu==studenty1.name:
            studenty1.set_age(change_num)
        elif name_stu==studenty2.name:
            studenty2.set_age(change_num)
        elif name_stu==studenty3.name:
            studenty3.set_age(change_num)
        elif name_stu==studenty4.name:
            studenty4.set_age(change_num)
        elif name_stu==studenty5.name:
            studenty5.set_age(change_num)
        else:
            print('к сожелению у нас нет студента под таким именем')
