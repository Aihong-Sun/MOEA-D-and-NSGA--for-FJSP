from Env_JSP_FJSP.Job import Job
from Env_JSP_FJSP.Machine import Machine

class Job_shop:
    def __init__(self,args):
        self.n= args.n
        self.m=args.m
        self.O_num=args.O_num
        self.PM = args.Processing_Machine
        self.PT = args.Processing_Time
        self.reset()

    def reset(self):
        self.C_max = 0      #makespan
        self.load=0         # Total load of machines
        self.max_EndM=None  # the last end machine
        self.mac_load=[0]*self.m    # load of each machine
        self.Jobs=[]
        for i in range(self.n):
            Ji=Job(i,self.PM[i],self.PT[i])
            self.Jobs.append(Ji)
        self.Machines=[]
        for j in range(self.m):
            Mi=Machine(j)
            self.Machines.append(Mi)

    # decode of chs[i]
    def decode(self,Job,Machine):
        Ji=self.Jobs[Job]
        # obtain processing time/start time/processing machine of current operation
        o_pt, s,M_idx = Ji.get_next_info(Machine)
        Mi=self.Machines[M_idx-1]
        start=Mi.find_start(s,o_pt)     # obtatin real start time on machine
        end=start+o_pt
        self.load+=o_pt
        self.mac_load[Mi.idx]+=o_pt
        Mi.update(start, end, [Ji.idx, Ji.cur_op])  # update machine state
        Ji.update(start,end,Mi.idx)     #update Job state
        if end>self.C_max:  # update makespan
            self.C_max=end
            self.max_EndM=Mi
        self.max_load = max(self.mac_load)  #update max_load of machine