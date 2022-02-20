class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        result = list(s)
        for ind, target, source in zip(indices, targets, sources):
            if not s.startswith(source, ind):
                continue
            else:
                result[ind] = target
                for i in range(ind+1, len(source)+ind):
                    result[i] = ''
        return ''.join(result)
    