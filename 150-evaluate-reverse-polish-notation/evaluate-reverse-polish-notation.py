class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack=[]

        for c in tokens:
            if c == "+":
                myStack.append(int(myStack.pop() + myStack.pop()))
            elif c == "-":
                a,b=myStack.pop(),myStack.pop()
                myStack.append(int(float(b-a)))

            elif c == "*":
                myStack.append(int(myStack.pop() * myStack.pop()))
            elif c == "/":
                a,b=myStack.pop(),myStack.pop()
                myStack.append(int(float(b/a)))
            else:
                myStack.append(int(c))
        return myStack[-1]


