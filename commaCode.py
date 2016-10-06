list = []
info = None
while info != '':
    info = str(input('What do you want to add to your list? '))
    list.append(str(info))
for i in range(int(len(list)-1)):
    print(list[i] + ', ' )
print(list[:-1])