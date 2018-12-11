a = []
while True:
    b = input()
    if b =='q':
        break
    elif b =='add':
        s1 = input()
        a.append(s1)
    elif b =='get':
        print(a)
    elif b =='remove':
        a.remove(input())
    print(a)




