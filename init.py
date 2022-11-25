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

print('Imagine a ' + alien_rat.color + ' rat\n'"with a weight of", alien_rat.size, "kg")


# print the value: object and class attributes


class Bird:
    def __int__(self, height, age, weight):
        self.urefu = height
        self.miaka = age
        self.uzito = weight


chicken = Bird()

chicken.urefu = 20
chicken.uzito = 2
chicken.miaka = 2

print("\nOur veteran hen is about", chicken.miaka, "years old")


class Lady:
    def __init__(self, color, name, country, status):
        self.rangi = color
        self.jina = name
        self.nchi = country
        self.hali = status


girl_friend = Lady("Brown", "Rachel", "Kenya", "single but we are married")


print("\nMy girlfriend is", girl_friend.hali)
