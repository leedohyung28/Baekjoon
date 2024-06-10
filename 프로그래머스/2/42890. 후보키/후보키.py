from itertools import combinations

def solution(relation) :
    r = len(relation)
    c = len(relation[0])

    l = [k for k in range(c)]
    t = 1
    aa = []

    while t <= len(l) :
        for i in combinations(l, t) :
            s = []
            ans = True
            for k in range(r) :
                m = []
                for j in i :
                    m.append(relation[k][j])
                if m in s :
                    ans = False
                    break
                else :
                    s.append(m)
            if ans :
                caught = False
                for a in aa :
                    la = len(a)
                    for i1 in a :
                        for i2 in i :
                            if i1 == i2 :
                                la -= 1
                                if la == 0 :
                                    caught = True
                                    break
                    if caught:
                        break
                if not caught :
                    aa.append(list(i))

        t += 1
    return len(aa)