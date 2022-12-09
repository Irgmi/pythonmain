##Василенко Вадим ИПЗ-19/9

import re

class NameConverter():

    def __init__(self, name):
        self.name = name

    def to_snake_case(self):
        self.name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', self.name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', self.name).lower()

    def to_camel_case(self):
        self.name = re.sub(r"(_|-)+", " ", self.name).title().replace(" ", "")
        return ''.join([self.name[0].lower(), self.name[1:]])


if __name__ == "__main__":
    name = input()
    NameConverterObject = NameConverter(name)
    print(NameConverterObject.to_snake_case())
    print(NameConverterObject.to_camel_case())