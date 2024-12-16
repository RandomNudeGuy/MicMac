class H:
    def __str__(self):
        return "H"

class e:
    def __str__(self):
        return "e"

class l:
    def __str__(self):
        return "l"

class o:
    def __str__(self):
        return "o"

class space:
    def __str__(self):
        return " "

class W:
    def __str__(self):
        return "W"

class r:
    def __str__(self):
        return "r"

class d:
    def __str__(self):
        return "d"

class exclamation:
    def __str__(self):
        return "!"

def create_objects():
    return [H(), e(), l(), l(), o(), space(), W(), o(), r(), l(), d(), exclamation()]

def memory_hog():
    for obj in create_objects():
        for _ in range(10**7):
            pass
        yield str(obj)

result = "".join([char for char in memory_hog()])

if __name__ == '__main__':
    print(result)
