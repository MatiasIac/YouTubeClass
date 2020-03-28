
a = 20

if a == 20:
    print "Es verdadero"
elif True:
    print "Es falso"
    if 10 == 10:
        print "Dentro del otro if"

a = [2, 4, 6, 10]

for target_list in a:
    print target_list

for target_list in range(1, 11):
    print target_list
    if target_list == 5:
        break

while True:
    a += 1
    print a
    if a == 5:
        break
