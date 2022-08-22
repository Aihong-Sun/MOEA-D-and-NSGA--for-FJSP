
import numpy as np
import matplotlib.pyplot as plt
import pickle
from mpl_toolkits.mplot3d import Axes3D

def Instance(file):
    '''
    :param file: Instance of FJSP
    example:
    n,m=3, 3 jobs, 3 machines
    PT=[[   # jobs 1
            [1,2],  # operation 1:  [1,2] indicatas for the first and second available machine's processing time
            [1,3]],
        [   # jobs 2
            [2,3],
            [3,2],]]
    MT=[[   # jobs 1
            [1,3], # operation 1:  [1,2] indicatas for the first and second available machine's index
            [3,2]],
        [   # jobs 2
            [1,2],
            [2,3]]]
    ni=[2,2] # the first job has 2 operations, the second job has 2 operations
    '''

    with open(file,"rb") as fb:
        I=pickle.load(fb)
    n,m,PT,MT,ni=I['n'],I['m'],I['processing_time'],I['Processing machine'],I['Jobs_Onum']

    return n,m,PT,MT,ni

def Tchebycheff(x, z, lambd):
    '''
    :param x: Popi
    :param z: the reference point
    :param lambd: a weight vector
    :return: Tchebycheff objective
    '''
    Gte = []
    for i in range(len(x.fitness)):
        Gte.append(np.abs(x.fitness[i]-z[i]) * lambd[i])
    return np.max(Gte)

# 根据权重向量λ计算T个邻居存入B
# return B->二维list [第一维代表种群中的个体list 第二维代表个体的T个邻居list]
def Neighbor(lambd, T):
    B = []
    for i in range(len(lambd)):
        temp = []
        for j in range(len(lambd)):
            # 计算二维欧氏距离
            distance = np.sqrt((lambd[i][0] - lambd[j][0])**2 + (lambd[i][1] - lambd[j][1])**2)
            temp.append(distance)
        res = np.argsort(temp)  # 下标排序
        B.append(res[:T])  # 取前T个近的邻居加入B
    return B

# 获取种群的最小f值作为参考点-min
# input 种群P->一维list
# return z->一维list
def BestValue(P):
    z = [P[0].f[i] for i in range(len(P[0].f))]  # 初始化
    for i in range(1, len(P)):
        for j in range(len(P[i].f)):
            if P[i].f[j] < z[j]:
                z[j] = P[i].f[j]
    return z

# bi-objective
def Dominate(Pop1,Pop2):
    '''
    :param Pop1:
    :param Pop2:
    :return: If Pop1 dominate Pop2, return True
    '''
    if (Pop1.fitness[0]<Pop2.fitness[0] and Pop1.fitness[1]<Pop2.fitness[1]) or \
        (Pop1.fitness[0] <= Pop2.fitness[0] and Pop1.fitness[1] < Pop2.fitness[1]) or \
        (Pop1.fitness[0] < Pop2.fitness[0] and Pop1.fitness[1] <= Pop2.fitness[1]):
        return True
    else:
        return False

# bi-objective
def Plot_NonDominatedSet(EP,Instance,Algo_name,cpu_t):
    x = []
    y = []
    for i in range(len(EP)):
        x.append(EP[i].fitness[0])
        y.append(EP[i].fitness[1])
    plt.plot(x, y, '*')
    plt.xlabel('makespan')
    plt.ylabel('Total Machine Load')
    plt.title('Instance: '+Instance+' '+'Algo_name: '+Algo_name+' '+'CPU(s): '+str(cpu_t))

# 3-objective
def Tri_Dominate(Pop1,Pop2):
    '''
    :param Pop1:
    :param Pop2:
    :return: If Pop1 dominate Pop2, return True
    '''
    if (Pop1.fitness[0]<Pop2.fitness[0] and Pop1.fitness[1]<Pop2.fitness[1] and Pop1.fitness[2]<Pop2.fitness[2]) or \
        (Pop1.fitness[0] <= Pop2.fitness[0] and Pop1.fitness[1] < Pop2.fitness[1] and Pop1.fitness[2]<Pop2.fitness[2]) or \
        (Pop1.fitness[0] < Pop2.fitness[0] and Pop1.fitness[1] <= Pop2.fitness[1] and Pop1.fitness[2]<Pop2.fitness[2]) or \
            (Pop1.fitness[0] < Pop2.fitness[0] and Pop1.fitness[1] <Pop2.fitness[1] and Pop1.fitness[2]<=Pop2.fitness[2]) or \
            (Pop1.fitness[0] <= Pop2.fitness[0] and Pop1.fitness[1] <= Pop2.fitness[1] and Pop1.fitness[2]<Pop2.fitness[2]) or \
            (Pop1.fitness[0] < Pop2.fitness[0] and Pop1.fitness[1] <= Pop2.fitness[1] and Pop1.fitness[2]<=Pop2.fitness[2]) or \
            (Pop1.fitness[0] <=Pop2.fitness[0] and Pop1.fitness[1] < Pop2.fitness[1] and Pop1.fitness[2]<=Pop2.fitness[2]):
        return True
    else:
        return False

# 3-objective
def TriPlot_NonDominatedSet(ax,color,EP,Instance,Algo_name,cpu_t):
    x = []
    y = []
    z=[]
    for i in range(len(EP)):
        x.append(EP[i].fitness[0])
        y.append(EP[i].fitness[1])
        z.append(EP[i].fitness[2])

    # 绘制散点图
    ax.scatter(x, y, z,color=color,label=str(Algo_name))
    # 添加坐标轴(顺序是Z, Y, X)
    ax.set_zlabel('Max Machine Load', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Total Machine Load', fontdict={'size': 15, 'color': 'red'})
    ax.set_xlabel('Makespan', fontdict={'size': 15, 'color': 'red'})
    plt.title('Instance: '+Instance+' '+'Algo_name: '+Algo_name+' '+'CPU(s): '+str(cpu_t))

def fast_non_dominated_sort(Pop):
    S=[[] for i in range(len(Pop))]
    front = [[]]
    n=[0 for i in range(len(Pop))]
    rank = [0 for i in range(len(Pop))]

    for p in range(len(Pop)):
        S[p]=[]
        n[p]=0
        for q in range(len(Pop)):
            if Tri_Dominate(Pop[p],Pop[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif Tri_Dominate(Pop[q],Pop[p]):
                n[p] = n[p] + 1
        if n[p]==0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)
    i = 0
    while(front[i] != []):
        Q=[]
        for p in front[i]:
            for q in S[p]:
                n[q] =n[q] - 1
                if( n[q]==0):
                    rank[q]=i+1
                    if q not in Q:
                        Q.append(q)
        i = i+1
        front.append(Q)
    del front[len(front) - 1]
    NDSet=[]
    for Fi in front:
        NDSeti=[]
        for pi in Fi:
            NDSeti.append(Pop[pi])
        NDSet.append(NDSeti)
    return NDSet

#Function to calculate crowding distance
def crowding_distance(NDSet):
    Distance=[0]*len(NDSet)
    NDSet_obj={}
    for i in range(len(NDSet)):
        NDSet_obj[i]=NDSet[i].fitness
    ND=sorted(NDSet_obj.items(),key=lambda x:x[1][0])
    Distance[ND[0][0]]=1e+20
    Distance[ND[-1][0]] = 1e+20
    for i in range(1,len(ND)-1):
        if Distance[ND[i][0]]==0:
            Distance[ND[i][0]]=abs(ND[i+1][1][0]-ND[i-1][1][0])+abs(ND[i+1][1][1]-ND[i-1][1][1])+abs(ND[i+1][1][2]-ND[i-1][1][2])
    distance=dict(enumerate(Distance))
    New_distance=sorted(distance.items(),key=lambda x:x[1],reverse=True)
    L=[_[0] for _ in New_distance]
    return L

# generate weight for three objective
def Tri_VGM(H):
    delta=1/H   # a uniform spacing
    w=[]
    w1=0
    while w1<=1:
        w2=0
        while w2+w1<=1:
            w3=1-w1-w2
            w.append([w1,w2,w3])
            w2+=delta
        w1+=delta
    return w

def bi_VGM(Pop_size):
    delta=1/Pop_size
    w=[]
    w1=0
    while w1<=1:
        w2=1-w1
        w.append([w1,w2])
        w1+=delta
    return w



