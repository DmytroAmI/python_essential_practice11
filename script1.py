"""
Single-Responsibility Principle
Кожен клас має бути відповідальним
тільки за свою частину функціоналу
"""


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, "r") as f:
            return f.read()

    def write_data(self, data):
        with open(self.filename, "w") as f:
            return f.write(data)
