class stack:
    def __init__(self):
        self.data=[]

    def push(self,val):
        return self.data.append(val)
    
    def peek(self):
        return self.data[-1]
    
    def pop(self,val=0):
        return self.data.pop(val)
    
    def if_empty(self):
        return len(self.data)==0

    def size(self):
        return len(self.data)
    

s=stack()
s.push(3),s.push(7),s.push(2)
print(s.peek())
print(s.pop())
print(s.if_empty())
print(s.size())