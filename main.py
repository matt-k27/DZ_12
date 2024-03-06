import string

print('DZ12')

inputtedText = str(input('Enter your text pls: ')).title()
hashTag = []

for char in inputtedText:
    if not (char in string.punctuation) and char != ' ':
        hashTag.append(char)

result = "".join(hashTag)

print(f'#{result[:140]}')

print('Thank you for using')