import argparse

def get_args(n,m,PT,MT,ni,means_m=1):
    parser = argparse.ArgumentParser()
    # params for FJSPF:
    parser.add_argument('--n', default=n, type=int, help='job number')
    parser.add_argument('--m', default=m, type=int, help='Machine number')
    parser.add_argument('--O_num', default=ni, type=list, help='Operation number of each job')
    parser.add_argument('--Processing_Machine', default=MT, type=list, help='processing machine of operations')
    parser.add_argument('--Processing_Time', default=PT, type=list, help='fuzzy processing machine of operations')
    parser.add_argument('--means_m', default=means_m, type=float, help='avaliable machine')

    # Params for Algorithms
    parser.add_argument('--pop_size', default=100, type=int, help='Population size of the genetic algorithm')
    parser.add_argument('--gene_size', default=100, type=int, help='generation size of the genetic algorithm')
    parser.add_argument('--pc_max', default=0.8, type=float, help='Crossover rate')
    parser.add_argument('--pm_max', default=0.05, type=float, help='mutation rate')
    parser.add_argument('--pc_min', default=0.7, type=float, help='Crossover rate')
    parser.add_argument('--pm_min', default=0.01, type=float, help='mutation rate')
    parser.add_argument('--p_GS', default=0.5, type=float, help='globel initial rate')
    parser.add_argument('--p_LS', default=0.3, type=float, help='Local initial rate')
    parser.add_argument('--p_RS', default=0.2, type=float, help='random initial rate')
    parser.add_argument('--T', default=10, type=int, help='the number of the weight vectors in the neighborhood of each weight vector')
    parser.add_argument('--H', default=16, type=int,
                        help='the number of divisions considered along each objective coordinate')
    parser.add_argument('--N_elite', default=2, type=int, help='Elite number')
    args = parser.parse_args()
    return args
