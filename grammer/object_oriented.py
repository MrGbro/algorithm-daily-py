class Student(object):

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value:int):
        if value > 0:
            self.__height = value
        else:
            raise ValueError("height must be greater than 0")

    def __str__(self):
        return f"Student(height={self.height})"

def hello(self):
    print("hello")
Hello = type("Hello",(object,),{"hello":hello})
obj = Hello()
obj.hello()
if __name__ == '__main__':
    student = Student()
    student.height = 12
    print(student)
