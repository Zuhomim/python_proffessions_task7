import json


def load_students():
    """Загружает список студентов из файла"""
    with open('students.json', 'r') as file:
        students = json.load(file)
    return students


def load_professions():
    """Загружает список профессий из файла"""
    with open('professions.json', 'r') as file:
        professions = json.load(file)
    return professions


def get_student_by_pk(pk, students_list):
    """Получает словарь с данными студента по его pk"""
    for student in students_list:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title, prof_list):
    """Получает словарь с инфо о профе по названию"""
    for prof_name in prof_list:
        if prof_name["title"].lower() == title.lower():
            return prof_name


def check_fitness(student, profession):
    """Сравнивает skills студента и skills професии, выводит пересечения и процент вхождения подмножества"""
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])
    available_skills = list(student_skills.intersection(profession_skills))
    missing_skills = list(profession_skills.difference(student_skills))
    fit_percent_skills = round((len(available_skills) / len(profession_skills)) * 100)

    return {
        "has": available_skills,
        "lacks": missing_skills,
        "fit_percent": fit_percent_skills
    }
