from re import A


number = 10

day = 'three'

a = "I ate %d apples. So I was sick for %s days." % (number, day)
print(a)
a = "I ate {} apples" .format ("three")
print(a)
a = "I ate {number} apples. So I was sick for {day} days." .format(number= 3, day = "three")
print(a)