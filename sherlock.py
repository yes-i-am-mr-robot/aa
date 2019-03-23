s = input().strip()

letters = list(set(list(s)))

freq1 = s.count(letters[0])
freq2 = 0
count1 = 0
count2 = 0
flag = True

for l in letters:
    if s.count(l) == freq1:
        count1 += 1
    elif freq2 == 0:
        freq2 = s.count(l)
        count2 = 1
    elif s.count(l) == freq2:
        count2 += 1
    else:
        flag = False
        break
    
    if count1 > 1 and count2 > 1:
        flag = False
        break
    
        
if flag:
    print("YES")
else:
    print("NO")
        
