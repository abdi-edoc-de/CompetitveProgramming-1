class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        self.result = 0
        def insert(s):
            temp = trie
            for i in s:
                if i in temp:
                    temp = temp[i]
                else:
                    temp[i] = {}
                    temp = temp[i]
        n = len(bin(max(nums)).replace('0b',""))
        # print(n)
        arr = ["0"] * n

        op = {'0' :'1', '1':"0"}
        # print(arr, n)
        # print(str(["0","1"]))
        # print(''.join(['0','1']))
        def  check(s):
            temp = trie
            for i in range(n):
                bit = s[i]
                if op[bit] in temp:
                    arr[i] = '1'
                    temp = temp[op[bit]]
                else:
                    arr[i] = '0'
                    if bit not in temp: return
                    temp = temp[bit]
            # print(s,arr).
            self.result = max(self.result, int("".join(arr),2))
        for num in nums:
            s = bin(num).replace('0b',"")
            s = (n-len(s)) * "0" + s
            # print(s, 'this')
            check(s)
            insert(s)
        # print(trie["1"])
            
        
        return self.result
            
            