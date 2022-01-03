class Solution:
    def numberToWords(self, num: int) -> str:
        # print(len(str(1234567891)))
        number = str(num)
        n = len(number)
        if num == 0:return 'Zero'
        self.first = {"0":"","1":"One", "2":"Two", "3": "Three" ,"4":"Four" ,"5":"Five", "6":"Six" ,"7":"Seven" ,"8":"Eight","9": "Nine"} 
        self.second = {"0":"Ten","1": "Eleven" ,"2":"Twelve" ,"3": "Thirteen" ,"4":"Fourteen"
                       ,"5":"Fifteen" ,"6":"Sixteen","7": "Seventeen" ,"8":"Eighteen","9": "Nineteen"}
        self.third = {"0":"","2":"Twenty", "3":"Thirty", "4":"Forty",
                      "5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty" ,"9":"Ninety"}
        result = []
        self.levels = {1: 'Thousand', 2:"Million",3:"Billion"}
        self.check = {'Thousand', "Million","Billion"}
        self.dfs(number[:max(n-3, 0)], number[max(n-3,0):],result, 1)
        # print(result)
        return ' '.join(x for x in result[::-1] if x != '').strip()
    def dfs(self,number, num,result , l):
        n = len(num)
        num= list(num)[::-1]
        for i in range(n):
            if i == 0:
                if num[0] == '0':continue
                result.append(self.first[num[i]])
            elif i == 1:
                if num[i] == "1":
                    if num[0] !="0":
                        result.pop()
                    result.append(self.second[num[i - 1]])
                else:
                    if num[i] == '0':continue
                    result.append(self.third[num[i]])
            elif i == 2:
                if num[i] == "0":continue
                result.append('Hundred')
                result.append(self.first[num[i]])
        n = len(number)
        if n == 0:return 
        if result and result[-1] in self.check:
            result[-1] = self.levels[l]
        else:
            result.append(self.levels[l])
        self.dfs(number[:max(n-3, 0)], number[max(n-3,0):],result, l+1)
                
            
                
        