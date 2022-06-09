# no = input('insert any no. : ')
# no = int(no)
# total = 0
# for i in range(1,(no + 1)):
#     total += i
# print(total)

no = input('insert any num. : ')
total = 0
for i in range(len(no)):
    total = total + int(no[i])
print(total) 