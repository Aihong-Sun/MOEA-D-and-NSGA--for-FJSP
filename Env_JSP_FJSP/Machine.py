

class Machine:
    def __init__(self, idx):
        self.idx = idx
        self.start = []
        self.end = []
        self._on = []

    def update(self, s, e, Job):
        self.start.append(s)
        self.start.sort()
        self.end.append(e)
        self.end.sort()
        idx = self.start.index(s)
        self._on.insert(idx, Job)

    def find_start(self, s, o_pt):
        if self.end == []:
            return max(s, 0)
        else:
            if s > self.end[-1]:
                return s
            else:
                o_s = self.end[-1]
                l = len(self.end) - 2
                while l >= 0:
                    if s + o_pt > self.start[l + 1]:
                        break
                    if self.end[l] > s and self.end[l] + o_pt <= self.start[l + 1]:
                        o_s = self.end[l]
                    elif self.end[l] < s and s + o_pt <= self.start[l + 1]:
                        o_s = s
                    l -= 1
                return o_s