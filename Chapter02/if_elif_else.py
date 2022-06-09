# if elif else statement.
# show ticket prizing of coco.
# 1 to 3(free)
# 4 to 10(150)
# 11 to 60(250)
# above 60(200)

age = input('insert your age :')
age = int(age)
if age == 0 or age < 0:
    print('you cannot watch the movie.')
elif 0 < age <= 3 :
    print("ticket = free")
elif 3 < age <= 10 :
    print('ticket = 150')
elif 10 < age <= 60 :
    print('ticket = 250')
else :
    print('ticket = 200') 
