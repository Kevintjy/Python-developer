"""
This is a file to initialize the class of Course

NOTICE:
This file is used to help reader understand how the result.txt writing,
and how to calculate the current mark.
In window.py, it straightforwardly calculates the data read from result.txt,
not related to this class.
"""


class Course:
    def __init__(self, name: str):
        self.name = name
        self.result = {}
        self.current = 0

    def add_mark(self, assignment_name: str, mark: int, percent: int) ->None:
        self.result[assignment_name] = (mark, percent)
        self.update_current()

    def update_current(self):
        temp = 0
        new_temp = []
        for m, p in self.result.values():
            temp += m * p
            new_temp.append(p)
        return temp / sum(new_temp)

    def __str__(self):
        result = []
        for k,v in self.result.items():
            result.append(k+':'+str(v)+'\n'+ '        ')
        return self.name + ': ' + ''.join(result)


if __name__ == '__main__':
    MAT137 = Course('MAT137')
    MAT137.add_mark('tt1',90,10)
    MAT137.add_mark('tt2',100,20)
    print(MAT137.update_current())

