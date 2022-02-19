class AllOne:

    def __init__(self):
        self.d={}

    def inc(self, key: str) -> None:
        if key in self.d:
            self.d[key]=self.d[key]+1      
        else:
            self.d[key]=1
            
    def dec(self, key: str) -> None:
        self.d[key]=self.d[key]-1
        if self.d[key]==0:
            del self.d[key]
            
    def getMaxKey(self) -> str:
        if len(self.d)==0:
            return ""
        else:
            a=max(self.d.values())
            for i in self.d:
                if self.d[i]==a:
                    return i 
    
    def getMinKey(self) -> str:
        if len(self.d)==0:
            return ""
        else:
            a=min(self.d.values())
            for i in self.d:
                if self.d[i]==a:
                    return i 
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()