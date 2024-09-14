lass EMP:
    def_init_(self):
    self.roll = roll
    self.dept = dept
    self.sal = sal

    def showDetail(self):
        print("roll is =", self.roll)
        print("dept is =", self.dept)
        print("salary is =", self.sal)


e1 = EMP("staf", "gr-b", "50000")
e1.showDetail()
