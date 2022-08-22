from Algorithms.Algorithm import *
from Algorithms.Params import get_args

def Algo_Solver(f):
    fig = plt.figure(figsize=(14, 8), facecolor='w')
    ax = plt.axes(projection='3d')
    file = r'.\Instance\FJSP_Instance' + '/'+f
    import time
    t1 = time.time()
    n, m, PT, MT, ni = Instance(file)
    mm = 2
    args = get_args(n, m, PT, MT, ni, mm)
    Algo = Algorithms(args)
    EP = Algo.MOEAD_main()
    t2 = time.time()
    print('the CPU(s) time of MOEA/D', t2 - t1)
    TriPlot_NonDominatedSet(ax,'blue',EP,f.split('.')[0],'MOEA/D',round(t2 - t1,2))
    EP=Algo.NSGA_main()
    t3 = time.time()
    print('the CPU(s) time of NSGA', t3 - t2)
    TriPlot_NonDominatedSet(ax,'red',EP, f.split('.')[0],'NSGA',round(t3 - t2,2))
    plt.legend()
    plt.savefig(r'Tri_obj_result/'+f.split(',')[0]+'.png')
    plt.close()

if __name__=="__main__":
    for i in range(10):
        if i<9:f = 'Mk0'+str(i+1)+'.pkl'
        else:f = 'Mk'+str(i+1)+'.pkl'
        Algo_Solver(f)
