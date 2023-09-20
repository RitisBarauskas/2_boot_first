class Student:
    def __init__(self, name: str, second_name: str = 'Бесфамильный') -> None:
        self.name = name
        self.second_name = second_name

    def __str__(self) -> str:
        return f'Hello, {self.name}'


names = ['John', 'Jane', 'Jack']

for name in names:
    student = Student(name)
    print(student)
