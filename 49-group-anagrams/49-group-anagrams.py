class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        
        for word in strs:
            chars = list(word)
            chars.sort()
            dict[''.join(chars)].append(word)
        return [value for _, value in dict.items()]
        