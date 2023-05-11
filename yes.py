print(('Invalid', 'Valid')[all(map(lambda f: f(input('Enter a password: ')), [(lambda s: len(s) >= 8), str.islower, str.isupper, str.isdigit]))] + ' password')
