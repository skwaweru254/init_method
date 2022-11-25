#   Class Rat with two methods:init and self defined
#   Init method is called automatically inside a class
#   parameter self inside user defined method makes the difference from function

class Rat:
    def __init__(self):
        self.size = 10
        self.color = "brown"
        print("Just for imagination!\n")


alien_rat = Rat()

# class and object

print('Imagine a '+alien_rat.color+' rat\n'"with a weight of",alien_rat.size,"kg")

# print the value: object and class attributes