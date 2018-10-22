def multiply(D1,D2,D3,D4):
    res=[int(D1),int(D2),int(D3),int(D4)]
    for i in range(0,3):
        res[0]=res[0]+res[0]
        res[1]=res[1]+res[1]
        res[2]=res[2]+res[2]
        res[3]=res[3]+res[3]
    return res


def TestingSlideAdd(D1,D2,D3,D4):
    res=[int(D1),int(D2),int(D3),int(D4)]

    res[1]=res[1]+0.2*res[0]
    res[2]=res[2]+0.3*res[0]
    res[3]=res[3]+0.4*res[0]

    return res
