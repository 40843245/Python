#class_super.py
#show that the func - super()

class A:
    def __init__(self):
        self.n = 2
    def add(self, m):
        #step 4
        # self == d, self.n == d.n == 5
        print('self is {0} @A.add'.format(self))
        self.n += m
        # d.n == 7
class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        # step 2
        # self == d, self.n == d.n == 5
        print('self is {0} @B.add'.format(self))
        # same as suepr(B, self).add(m)
        # MRO of B is [D, B, C, A, object]
        # find 'add' member from the list [C, A, object]  under B
        super().add(m)

        # step 6
        # d.n = 11
        self.n += 3
        # d.n = 14
class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        # step 3:
        # self == d, self.n == d.n == 5
        print('self is {0} @C.add'.format(self))
        # same as suepr(C, self).add(m)
        # MRO of self is [D, B, C, A, object]
        #find 'add' member from the list [A, object] under C
        super().add(m)

        # step 5
        # d.n = 7
        self.n += 4
        # d.n = 11
#class D inherits class B then inherits class C
class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        #step 1:
        print('self is {0} @D.add'.format(self))
        # same super(D, self).add(m)
        # MRO  of self is [D, B, C, A, object]
        #  find 'add' member from the list [B, C, A, object] under D
        super().add(m)

        #step 7:
        # d.n = 14
        self.n += 5
        # self.n = 19
#driver code
#create a D() object named d
#d.n=5
d = D()
#d.n=5+2+4+3+5
d.add(2)
print(d.n)