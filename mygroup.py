groupmates = [
    {
        "name": "Юрий",
        "surname": "Титов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Анна",
        "surname": "Поваркова",
        "exams": ["МСиС", "АиГ", "КТП"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Гнездилов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Валерия",
        "surname": "Маркелова",
        "exams": ["УиАБД", "ИТиП", "СИИ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Евгений",
        "surname": "Самолыго",
        "exams": ["История", "Право", "БЖ"],
        "marks": [3, 3, 4]
    }
]
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def print_students(students):
    error = -1
    while error == -1:
        print(u"Введите среднее значение")
        averageMark = input()
        if is_number(averageMark) and 1 <= float(averageMark) and float(averageMark) <= 5:
            error = 1
        else:
            print(u"Значение введено неверно")
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        average = 0
        for number in student["marks"]:
            average += number
        average = average/len(student["marks"])
        if average > float(averageMark):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_students(groupmates)
