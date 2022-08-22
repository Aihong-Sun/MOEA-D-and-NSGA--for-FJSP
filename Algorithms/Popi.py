
from Env_JSP_FJSP.Job_Shop import Job_shop

class Popi:
    def __init__(self,args,CHS,J_site=None,len1=0,len2=0):
        self.args=args
        self.J_site=J_site
        self.l1=len1
        self.CHS=CHS
        self.JS=Job_shop(args)
        if self.args.means_m>1:
            self.fitness=list(self.decode1())   # bi-objective
        else:
            self.fitness =list(self.decode0())  # bi-objective

    def decode0(self):
        for i in self.CHS:
            self.JS.decode(i,0)
        return self.JS.C_max,self.JS.load,self.JS.max_load

    def decode1(self):
        for i in range(self.l1):
            O_num=self.JS.Jobs[self.CHS[i]].cur_op
            m_idx=self.J_site.index((self.CHS[i],O_num))
            self.JS.decode(self.CHS[i],self.CHS[m_idx+self.l1])
        return self.JS.C_max,self.JS.load,self.JS.max_load

