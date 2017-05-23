def make_student(name, age, gender):
    return {
            'name': name,
            'age': age,
            'gender': gender,
    }

def print_student(student):
    for key, value in student.items():
        print(key, value)

s1 = make_student('yongyeon.kim','31','male')
print_student(s1)

s2 = make_student(age='31', name='yongyeon.kim2', gender='male')
print_student(s2)


