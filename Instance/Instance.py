import pickle

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