class Employee:

    def __init__(self, i, n):
        self.id = i
        self.name = n


d = Employee(10, 'Pankaj')
# print(d.name)
if hasattr(d, 'name'):
    print(getattr(d, 'name'))
