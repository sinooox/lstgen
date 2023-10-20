students = [
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'},
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 3, 'full_name': 'Винговатов Александр Олегович'}
]

lst = [student['full_name'] for student in students
       if len(student['full_name'][student['full_name'].index(' ')+1:student['full_name'].rindex(' ')]) > 6]

print(lst)
