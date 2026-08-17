class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        print(tokens)
        stack = []

        for token in tokens:
            if not token or token == ".":
                continue
            if token == '..':
                if stack:
                    stack.pop()
                continue
            
            stack.append(token)
        
        output_path = ''

        for token in stack:
            output_path += f'/{token}'
        
        if not stack:
            output_path = '/'

        return output_path
        