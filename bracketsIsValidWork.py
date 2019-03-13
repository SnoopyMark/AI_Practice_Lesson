class Solution:
    def isValid(self, s: str) -> bool:
        bracketsdict = {"(":")","[":"]","{":"}"}
        stack = ""
        for ch in s:
            if ch in ["(", "[", "{"]:
                stack += ch
            else:
                t = stack[-1]
                if ch != bracketsdict[t]:
                    return False
                stack = stack[:-1]
            print(ch)
        if stack:
            return False
        return True

if __name__ == "__main__":
    so = Solution( )
    s = "()"
    ky = so.isValid(s)
    print(ky)
