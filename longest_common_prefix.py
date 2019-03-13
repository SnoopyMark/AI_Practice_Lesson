class Solution:
    def longestCommonPrefix(strs: list):
    
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

if __name__ == "__main__":
    lists = ["dfgdj","dfkefg","dfmfgx","dfabcfg"]
    print(Solution.longestCommonPrefix(lists))
