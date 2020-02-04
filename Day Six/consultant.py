class consultant:
    def __init__(self, name="", skill="", exp=0):
        self.name = name;
        self.skill = skill;
        self.exp = exp;

    def __str__(self):
        return self.name + " " + self.skill + " " + str(self.exp)
    def salary(self):
        if (self.exp>=5 and self.exp<=10) and (self.skill=="java" or self.skill=="python"):
            print("Your salary is 12000/- ")
        elif (self.exp>=3 and self.exp<=8) and (self.skill=="AI" or self.skill=="python"):
            print("Your salary is 7000/- ")
        elif (self.exp>=4 and self.exp<=10) and (self.skill=="java" or self.skill=="python" or self.skill=="c" or self.skill=="cpp"):
            print("Your salary is 5000/- ")
        else:
            print("You are not eligible")
one=consultant("sumanth","java",5);one.salary()
two=consultant("Ram","c",6);two.salary()
three=consultant("Sham","AI",6);three.salary()
four=consultant("Raj","python",8);four.salary()
