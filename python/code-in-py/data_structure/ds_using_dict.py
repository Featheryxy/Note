ab = {# address book
    'Swaroop':'swaropp@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']

print('\nThere are {} contacts in the address-book\n' .format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}' .format(name,address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])