# With extra space(N)
class MinStack:
    def __init__(self):
        self.stack=[]
        self.mini=float('inf')

    def push(self,val):
        if not self.stack:
            self.stack.append(val)
            self.mini=val
        else:
            if val>self.mini:
                self.stack.append(val)
            else:
                self.stack.append(2*val-self.mini)
                self.mini=val
    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1]<self.mini:
            self.mini=2*self.mini-self.stack[-1]
        self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        if self.stack[-1]<self.mini:
            return self.mini
        return self.stack[-1]

    def getMin(self):
        return self.mini

class MinStack2:
    def __init__(self):
        self.stack=[]

    def push(self,val):
        if not self.stack:
            self.stack.append((val,val))


        else:
            self.stack.append((val,min(val,self.stack[-1][1])))
    def pop(self):
        if not self.stack:
            return None
        self.stack.pop()
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]
    def getMin(self):
        if not self.stack:
            return None
        return self.stack[-1][1]


if __name__=="__main__":
    pass