"""
Single-Responsibility Principle
Кожен клас має бути відповідальним
тільки за свою частину функціоналу
"""


class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        with open(self.file_name, "r") as f:
            return f.read()


class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_data(self, data):
        with open(self.file_name, "w") as f:
            return f.write(data)
