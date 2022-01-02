class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result , line, width = [] , [] , 0
        def justify():
            if len(line) == 1: return line[0] + ' ' * (maxWidth - width)
            else:
                space = maxWidth - (width )
                loc = len(line) - 1
                assigns = [space//loc] * loc
                for i in range(space % loc):
                    assigns[i] += 1
                result = ""
                for i in range(loc):
                    result += line[i] + " " * (assigns[i])
                result += line[-1]
                return result
        for w in words: 
            if width + len(w) + len(line) <= maxWidth:
                width += len(w)
                line.append(w)
            else:
                result.append(justify())
                line , width = [w] , len(w)
        result.append(' '.join(line) + (" " * (maxWidth - (width+len(line)) + 1)))
        return result
        