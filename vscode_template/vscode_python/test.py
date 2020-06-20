num1 = 10_000_000
num2 = 100_000
total = num1 + num2
print(f'{total:,}')

names = ['Corey','Chris','Dave','Travis']

for i, name in enumerate(names,start=0):
    print(i, name)



#TODO: 匹配两个list, zip
names = ['Peter Parker','Clark Kent','Wade Wilson','Bruce Wayne']
heros = ['Spiderman','Superman','Deadpool','Batman']
universes = ['Marvel','DC','Marvel','DC']

for name, hero, universe in zip(names, heros, universes):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heros, universes):
    print(value)



# TODO: unpacking
items = (1, 2, 3, 4, 5)
a,b,*c,d = items
print(a)
print(b)
print(c)
print(d)
