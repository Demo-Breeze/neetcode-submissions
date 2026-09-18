class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        operate = ["+","D","C"]
        for i in operations:
            if i not in operate:
                total.append(int(i))
            elif i =="+":
                c = total[-1]+total[-2]
                total.append(c)
            elif i == "C":
                total.pop(-1)
            elif i == "D":
                c = 2*total[-1]
                total.append(c)
            print(total)
        return sum(total)