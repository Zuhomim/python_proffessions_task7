import functions

# JSON-структуры студентов и профессий из файлов students, proffessions
students = functions.load_students()
professions = functions.load_professions()


def main():
    """Основная функция программы"""

    student_num = int(input("Введите номер студента\n"))
    # Словарь студента
    student_dict = functions.get_student_by_pk(student_num, students)
    # Проверка наличия студента по введенному номеру студента
    if not student_dict:
        print('У нас нет такого студента')
        return

    student_name = student_dict["full_name"]
    student_skills = student_dict["skills"]

    print(f'''Студент {student_name}
Знает {', '.join(student_skills)}''')

    student_speciality = input(f'Выберите специальность для оценки студента {student_name}\n')

    # Словарь профессии из файла professions
    profession_dict = functions.get_profession_by_title(student_speciality, professions)

    # Проверка наличия введенной профессии в файле professions
    if not profession_dict:
        print('У нас нет такой специальности')
        return

    # Словарь со скиллами студента, имеющимися в скиллах профессии,
    # недостающими скиллами и процентом скиллов студента от необходимых скиллов для профессии
    skills_dict = functions.check_fitness(student_dict, profession_dict)

    print(f'''Пригодность {skills_dict["fit_percent"]}%
{student_name} знает {', '.join(skills_dict["has"])}
{student_name} не знает {', '.join(skills_dict["lacks"])}''')

    return


main()
