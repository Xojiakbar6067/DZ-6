class Math:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def addition(self):
        c=math.a+math.b
        print(c)
    def multiplication(self):
        c=math.a*math.b
        print(c)
    def division(self):
        c=math.a/math.b
        print(c)
math=Math(a=int(input('a=')), b=int(input('b=')))
math.addition()
math.multiplication()
math.division()