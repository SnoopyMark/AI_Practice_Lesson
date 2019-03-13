class Solution:
    def isValid(self, s: str) -> bool:
        bracketsdict = {"(":")","[":"]","{":"}"}
        stack = ""
        for ch in s:
            if ch == "(" or "[" or "{":# dosent work ,实际上是一个三元运算符
                stack += ch
            else:
                if ch != bracketsdict[pop(stack)]:
                    return False
            print(ch)
        if stack:
            print(stack)
            return False
        return True
        
    def pop(s: str):# 此为形参，不改变传入参数
        if s == "":
            return None
        t = s[-1]
        s = s[:-1]
        return t

if __name__ == "__main__":
    testcode = "()"
    solution = Solution( )
    k = solution.isValid(testcode)
    print(k)
    if solution.isValid(testcode):
        print("True")
