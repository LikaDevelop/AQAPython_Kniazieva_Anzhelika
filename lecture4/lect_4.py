class A:
    value = 1

class B(A):
    def __init__(self):
        value = 2

class C(B):
    def __init__(self):
        self.value = 3

class D(C):
    value = 4

print(A.value)
print(B.value)
print(C.value)
print(D.value)
print(A().value)
print(B().value)
print(C().value)
print(D().value)