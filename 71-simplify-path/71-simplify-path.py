class Solution:
    def simplifyPath(self, path: str) -> str:
        clean = []
        for char in  path:
            if char =='/' and clean and clean[-1] == '/':
                continue
            clean.append(char)
        path = ''.join(clean)
        paths = [path for path in path.split('/') if path != '']
        stack = []
        for path in paths:
            if path == '..':
                if stack: 
                    stack.pop()
                    stack.pop()
            elif path == '.': continue
            else:
                stack.append('/')
                stack.append(path)
        return ''.join(stack) if stack else "/"
                
