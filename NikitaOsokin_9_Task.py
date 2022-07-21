class Student:
    Name = "Ivan"
    Age = "18"
    GroupNumber = "10A"

    def __init__(self, Name, Age, GroupNumber):
        self.Name = Name
        self.Age = Age
        self.GroupNumber = GroupNumber

    def getName(self):
        print("Name: {}".format(self.Name))
        return

    def getAge(self):
        print("Age: {}".format(self.Age))
        return

    def getGroupNumber(self):
        print("Group: {}".format(self.GroupNumber))
        return

    def setNameAge(self, Name, Age):
        self.Name = Name
        self.Age = Age
        return Name, Age

    def setGroupNumber(self, GroupNumber):
        self.GroupNumber = GroupNumber
        return GroupNumber


StudentOne = Student(Name='Igor', Age='18', GroupNumber='10G')
StudentTwo = Student(Name='Nikita', Age='23', GroupNumber='10A')
StudentThree = Student(Name='Jon', Age='19', GroupNumber='11B')
StudentFour = Student(Name='Oleg', Age='17', GroupNumber='10A')
StudentFive = Student(Name='Roma', Age='18', GroupNumber='10G')
Student.setNameAge(self=Student, Name="Igor", Age="25")
Student.setGroupNumber(self=Student, GroupNumber="12А")



