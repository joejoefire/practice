#点をn個打つ

import random as rad

num = int(input('何個点を打つか'))

x = []
y = []

for i in range(num):
    x.append(rad.random())
    y.append(rad.random())


xy = list(zip(x,y))


#各点までの距離を求め、円の中ならリストへ

from scipy.spatial import distance

origin = (0,0)
inside = []

for i in range(num):
    dis = distance.euclidean(origin,xy[i])
    if dis <= 1:
        inside.append(dis)


#円の中の点の数を数え、円周率を求める。

inside_num = len(inside)
π = 4 * inside_num / num

print('円周率は'+str(π)+'です'+'/n円の中の点は'+str(num)+'個中'+str(inside_num)+'個でした。')