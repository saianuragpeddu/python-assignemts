x = 1
if x == 1:
    print('Equals 1')
if x > 1:
    print('x is grater than 1')
if x < 1:
    print('x is less than 1')


def greet(lang):
    if lang == 'es':
        print('Hola')
    if lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

print(greet('en'))
print(greet('es'))
print(greet('fr'))
