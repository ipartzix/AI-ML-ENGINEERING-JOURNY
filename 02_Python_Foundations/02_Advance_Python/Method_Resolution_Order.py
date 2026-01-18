class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):  # whic is come 1st that will work or print it call MRO
    pass


d = D()
d.show()
