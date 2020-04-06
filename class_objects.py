#Python is an object oriented language
#It is a type of programming that allows properties and behaviors to be bundled into individual objects
#Classes are used to create new user defined data structures that contain arbitrary information about something.
#An object(is an instance of a Class) consists of states (properties), behaviors(response), identity(it gives a unique name to an objects)


#First let's make a very simple Class, remember its like a blueprint

class firstClass:
  variable = "hello"

  def function(self):
    print("My first message in a class")

first_object = firstClass()
#this allows you to have a variable that holds an object from the class

#Sometimes we want to access a variable in an object, to do this , we do the following
first_object.variable

#Let's se what this prints
print(first_object.variable)

#One of the cool things about classes is that you can create mulitple objects with different copies of the variables

#Now I will create my own class and create two objects inside it

class Harvard_student:
    name = ""
    kind = "student"
    house = ""
    concentration = ""

    #now I will create a function that defines a description of the harvard Harvard_student
    #By using the self keyword we can access the atrributes and methods of the class in python
    def description(self):
        print("My name is", self.name, "I am a", self.kind, "I live in", self.house, "I study" , self.concentration)

#First instantiate the objects
student1 = Harvard_student()
student2 = Harvard_student()

student1.name = "Miela"
student2.name = "Unique"
student1.house = "Mather"
student2.house = "Eliot"
student1.concentration = "Statistics"
student2.concentration = "Biology"

print(student1.description())
print(student2.description())
