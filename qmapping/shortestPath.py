from queue import Queue

def preState(M, state: list):

    pre = []
    for i in range(len(M[state[0]])):
        if M[state[0]][i] == 1:
            if i != state[1]:
                pre.append([i, state[1]])
    for i in range(len(M[state[1]])):
        if M[state[1]][i] == 1:
            if i != state[0]:
                pre.append([state[0], i])
    return pre;

def toStr(src: list):
    return str(src[0])+str(src[1])
def invStr(src: str):
    return [int(src[0]),int(src[1])]

def shortestPath(M, src, tar):
    q = Queue()
    q.put(src)
    flag = {}
    flag[toStr(src)] = 0
    while not q.empty():
        temp = q.get()
        cost = flag[toStr(temp)]
        # flag[str(temp[0])+str(temp[1])] = 1;
        p = preState(M,temp)
        for i in p:
            if i[1] < i[0]:
                i.reverse()
            if not flag.__contains__(toStr(i)):
                q.put(i)
                flag[toStr(i)] = cost + 1
            if (flag.__contains__(toStr(tar))):
                break
    #print(flag)
    path = []
    path.append(tar)
    while toStr(tar) != toStr(src):
        cost = flag[toStr(tar)]
        pre = preState(M,tar)
        for i in pre:
            if i[0] > i[1]:
                t = i[0]
                i[0] = i[1]
                i[1] = t
            if flag.__contains__(toStr(i)) and flag[toStr(tar)] - flag[toStr(i)] == 1:
                path.insert(0, i)
                tar = i
                break;
    res = []
    for i in range(len(path) - 1):
        dic = {}
        for j,k in zip(path[i],path[i+1]):
            if dic.__contains__(j):
                dic[j] = dic[j] + 1
            else:
                dic[j] = 1
            if dic.__contains__(k):
                dic[k] = dic[k] + 1
            else:
                dic[k] = 1
        temp = []
        for d in dic.items():
            if d[1] <= 1:
                temp.append(d[0])
        res.append(temp)
        #print('Q'+str(temp[0])+'-->'+'Q'+str(temp[1]))
    return res




