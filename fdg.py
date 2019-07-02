def reverse(m1):
    return m1[::-1]
n2 = input()
count = 0
a3 = []
if n2==reverse(n2):
    print(0)
else:
    for i in range(len(n2)):
        for j in range(len(n2),i+1,-1):
            a3 = n2[i:j]
            if (reverse(a3)==a3):
                length = len(a3)
                if count<length:
                    count = length
    print(len(n2)-count)
