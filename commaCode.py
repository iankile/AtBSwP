list = []
info = None
while info != '':
    info = str(input('What do you want to add to your list? '))
    list.append(str(info))
for i in range(int(len(list)-2)):
    print(list[i] + ', ', end='')
print('and ' + list[-2])
