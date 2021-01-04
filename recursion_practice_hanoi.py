def hanoi(l, s, e):
    if l == 1:
        print("{} {}".format(s, e))
        return

    nl = l-1
    hanoi(nl, s, 6 - (s + e))
    print("{} {}".format(s, e))
    hanoi(nl, 6 - (s + e), e)
    
num = int(input())
print(2 ** num - 1)
hanoi(num, 1, 3)
