class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indices)
        all = []
        for i in range(n):
            all.append([indices[i] , sources[i], targets[i]])
        def is_substring(sub,ind):
            nsub,ns = len(sub), len(s)
            # print(ind, sub,s)
            for i in range(nsub):
                if ind+i > ns or s[ind+i] != sub[i]:return False
            return True
        offset = 0
        all.sort()
        for i in  range(n):
            ind, sub , target = all[i]
            ind += offset
            if is_substring(sub, ind):
                s = s[:ind] + target + s[ind+len(sub):]
                offset += len(target) - len(sub)
                print(ind, sub ,s)
            
        return s
            
            
        
        