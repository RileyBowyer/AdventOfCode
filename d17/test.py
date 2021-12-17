def addtuples(a, b): return tuple(map(sum, zip(a, b)))
minx, maxx, miny, maxy = map(int, re.findall(r'x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', content)[0])
hits = 0; biggest_y = miny
for x in range(1, maxx * 3):
    for y in range(-(maxy - miny) * 3, (maxy - miny) * 3):
        top = miny
        p = (0,0); v = (x,y)
        while p[0] < maxx and p[1] > miny:
            p = addtuples(p, v)
            v = addtuples(v, (-1 if v[0] > 0 else 0, -1))
            top = max(top, p[1])
            if minx <= p[0] <= maxx and miny <= p[1] <= maxy:
                hits += 1
                biggest_y = max(biggest_y, top)
                break
print([biggest_y, hits])