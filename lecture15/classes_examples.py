class A:
    value = 1

class B(A):
    value = 2


class C(B):
    def __init__(self, driver):
        self.value = 3
        self.drv = driver

    def print_driver_name(self):
        print(self.drv)
class D(C):
    pass


d = D(driver="ncjdeowd")
d.print_driver_name()