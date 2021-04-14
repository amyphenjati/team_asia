i = 0
yes_count = 0
no_count = 0
with open('text/questions.txt') as questions:
    lines = [line.rstrip('\n') for line in questions]
    while i < len(lines):
        quest = lines[i]
        i+=1
        print(quest)
        x = input()
        if x == 'yes':
            yes_count +=1
        elif x == 'no':
            no_count +=1
        else:
            print('please start over')
            break

print('yes_count', yes_count)
print('no_count', no_count)