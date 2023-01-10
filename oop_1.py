class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

   



cat_1 = Cat('tommy',1)
cat_2 = Cat('brownie',2)
cat_3 = Cat('kin',3)


def oldest_cat(*args):
    return max(*args)

print(f"the oldest cat is {oldest_cat(cat_1.age,cat_2.age,cat_3.age)} years old")