powers = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512']
X = [str(2**i) for i in range(10,801)]
d = {x[:4]:x for x in X}
for i in range(int(input())):
    p, pow = input(), 0
    numb = len(p)
    for i in powers:
        pow += p.count(i)
    for i in range(numb):
        sq = p[i:i+4]
        if sq in d:
            pow2 = d[sq]
            if pow2 == p[i:i+len(pow2)]:
                pow+=1
    print(pow)
