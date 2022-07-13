class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=tokens
        stack = []
        for i in s:
            if i != "+" and i != "-" and i != "*" and i != "/":
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(b-a)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(int(b/a))
                
        return (stack[0])
