import queue
################################
################################
###########1번 문제 풀이#########
################################
################################
class Node1:
    def __init__(self,level,weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include

def kp_BFS():
    global maxProfit
    global bestset
    global queue_size
    global count_node
    global find_second  
    
    q = queue.Queue()
    v = Node1(-1, 0, 0, n*[0])
    count_node += 1
    q.put(v)
    while not q.empty():
        if queue_size < q.qsize():
            queue_size = q.qsize()
            
        v = q.get()
        u = Node1(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1], v.include[:])
        count_node += 1
        u.include[u.level] = 1
        find_second.append(u)

        if u.weight <= W and u.profit > maxProfit:
            maxProfit = u.profit
            bestset = u.include[:]
        if compBound1(u) > maxProfit:
            q.put(u)
        
        u = Node1(v.level + 1, v.weight, v.profit, v.include[:])
        count_node += 1
        find_second.append(u)

        if compBound1(u) > maxProfit:
            q.put(u)

def compBound1(u):
    global W
    global w
    global n
    global p

    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level+1
        totweight = u.weight
        while j < n and totweight + w[j] <= W:
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if k< n:
            result += (W-totweight)*p[k]/w[k]
        return result

###################################
############데이터 입력#############
n=4
W=5
p=[30,36,18,10]
w=[3,4,3,2]
include=[0]*n
maxProfit =0
bestset=n*[0]

###################################
###################################

queue_size = 0
count_node = 0
find_second = list()
kp_BFS()

print("----- 1번 문제 -----")
print("(가) 생성된 상태공간트리의 총 노드의 개수 : " + str(count_node))
print("(나) queue에 저장되어 있는 데이터 개수의 최댓값 : " + str(queue_size))
print("(다) 최댓값을 주는 해 : " + str(bestset) + ", 이익 : " +str(maxProfit))

second_max = 0
second_bound = 0
index = 0
prelevel = 0
for i in range(count_node-1):
    if find_second[i].level != prelevel:
        second_bound = 0
    if compBound1(find_second[i]) >= second_bound and find_second[i].profit >= second_max and find_second[i].profit < maxProfit:
        second_bound = compBound1(find_second[i])
        second_max = find_second[i].profit
        index = i
    prelevel = find_second[i].level
print("     두 번째로 좋은 해 : " + str(find_second[index].include) + ", 이익 : " + str(find_second[index].profit))



################################
################################
###########2번 문제 풀이#########
################################
################################
import queue
class Node2:
    def __init__(self,level,weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include
    def __lt__(self, other):
        return self.bound < other.bound

def kp_Best_FS():
    global maxProfit2
    global bestset2
    
    temp2 = n2*[0]
    v2 = Node2(-1,0,0, 0.0,temp2)
    q2 = queue.PriorityQueue()
    v2.bound = compBound2(v2)
    q2.put((v2.bound,v2))
    
    while not q2.empty():
            
        v2 = q2.get()[1]
        if v2.bound < maxProfit2:
            u2 = Node2(v2.level + 1, v2.weight + w2[v2.level + 1], v2.profit + p2[v2.level + 1],0.0, v2.include[:])
            u2.include[u2.level] = 1
            
            if u2.weight <= W2 and u2.profit > maxProfit2:
                maxProfit2 = -u2.profit
                bestset2 = u2.include[:]
            u2.bound = compBound2(u2)
            if u2.bound < maxProfit2:
                q2.put((u2.bound, u2))
    
            u2 = Node2(v2.level + 1, v2.weight, v2.profit,0.0, v2.include[:])
            u2.bound = compBound2(u2)
            
            if u2.bound < maxProfit2:
                q2.put((u2.bound, u2))

def compBound2(u):
    global W2
    global w2
    global n2
    global p2

    if u.weight >= W2:
        return 0
    else:
        result2 = u.profit
        j2 = u.level+1
        totweight2 = u.weight
        while j2 < n2 and totweight2 + w2[j2] <= W2:
            totweight2 += w2[j2]
            result2 += p2[j2]
            j2 += 1
        k2 = j2
        if k2< n2:
            result2 += (W2-totweight2)*p2[k2]/w2[k2]
        return -result2


###################################
############데이터 입력#############
n2=4
W2=5
p2=[30,36,18,10]
w2=[3,4,3,2]
include2=[0]*n2
maxProfit2 =0
bestset2 = n2*[0]
###################################
###################################


kp_Best_FS()
print()
print("----- 2번 문제 -----")
print("최댓값을 주는 해 : " + str(bestset2) + ", 이익 : " +str(maxProfit2))
second_max2 = 0
second_bound2 = 0
index2 = 0
prelevel2 = 0

