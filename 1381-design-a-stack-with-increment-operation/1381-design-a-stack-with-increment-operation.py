class CustomStack:

    def __init__(self, maxSize: int):
        self.n=maxSize
        self.l=[]
        

    def push(self, x: int) -> None:
        if len(self.l)<self.n:
            self.l.append(x)
        

    def pop(self) -> int:
        if len(self.l)==0:
            return -1
        else:
            return self.l.pop()
        

    def increment(self, k: int, val: int) -> None:
        if k>len(self.l):
            for i in range(len(self.l)):
                self.l[i]=self.l[i]+val
        else:
            for i in range(k):
                self.l[i]=self.l[i]+val
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)