# this is a solution for a question in LeetCode named "count and say"
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return ""
        if n == 1:
            return "1"
        pre_str = self.countAndSay(n-1)
        ans_str = ""
        x = 0
        while x < len(pre_str):
            c = pre_str[x]
            count = 1
            while x+1 < len(pre_str) and pre_str[x+1] == c:
                count += 1
                x += 1
            x += 1
            ans_str += str(count)+c
        return ans_str

if __name__ == "__main__":
    kk = Solution()
    s = kk.countAndSay(2)
    print(s)
