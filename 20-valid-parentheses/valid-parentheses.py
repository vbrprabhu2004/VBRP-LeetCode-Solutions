class Solution(object):

    def isValid(self, s):
        characters = []  
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        
        for item in s:
            if item in opening:
                characters.append(item)
            elif item in closing:
                pos = closing.index(item)
                if len(characters) > 0 and characters[-1] == opening[pos]:
                    characters.pop()
                else:
                    return False
        
        return len(characters) == 0