def merge_values(f,s):
    merge_string = f +  s
    return(merge_string)
first_string = input("Enter a string of text:")
second_string = input("Enter another string of text:")

merge_string = merge_values(f=first_string, s=second_string)
print(merge_string)

#### here is my class
class Pet():
    species = "cat"
    name = "Kitty"
    age = 6
    def description(self):
        desc_str = "I have a %s named %s that is %s year(s) old." % (self.species, self.name, self.age)
        return desc_str
pet1 = Pet()
pet1.species = "cat"
pet1.name = "Kitty"
pet1.age = 6

print(pet1.description())