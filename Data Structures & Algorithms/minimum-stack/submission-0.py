class MinStack:

    def __init__(self):
        self.inputs = []
        

    def push(self, val: int) -> None:
        self.inputs.insert(0,val)

    def pop(self) -> None:
        self.inputs.pop(0)
        

    def top(self) -> int:
        s = self.inputs[0]
        return s
        

    def getMin(self) -> int:
         b = min(self.inputs)
         return b
        
