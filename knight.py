import sys


n = int(input().strip())
for a in range(1, n):
    for b in range(1,n):
        min_moves = {}
        def BFSfunction():
            origin = 1, 1
            end = n, n
            line = [origin]
            min_moves[origin] = 0

            while len(line):
                current = line[0]
                line.pop(0)
                if current == end:
                    print(min_moves[current], end=' ')
                    return
                for move in [(a, b), (b, a), (-a, -b), (-b, -a), (a, -b), (-a, b), (-b, a), (b, -a)]:
                    plus = current[0] + move[0], current[1] + move[1]
                    if plus[0] > end[0] or plus[1] > end[1] or plus[0] < 1 or plus[1] < 1:
                        continue
                    if plus not in min_moves:
                        min_moves[plus] = min_moves[current] + 1
                        line.append(plus)
            else:
                print(-1, end=' ')

        BFSfunction()
    print()
    
