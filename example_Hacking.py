words = ['Name : mehdi', 'family : asadi' , 'birthday : 1363.2.3', 'nickname : as']

correct = "mehdi1363.as"

print(words, '\n')
user_word = input('Enter your guess: ')

for n in range(0, 3):
    if user_word == correct:
        print('Hacked Successfully')
        break
    elif n == 2:
        print(f'\nHack Blocked. {correct}')
        break

    print(f'Incorrect. You have {2-n} more times')
    user_word = input('Enter another guess: ') 