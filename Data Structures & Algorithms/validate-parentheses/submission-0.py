class Solution:
    def isValid(self, s: str) -> bool:
        openers = []
        closers = {')': '(', ']': '[', '}': '{'}

        for bracket in s:
            # If the bracket is not an opener, try to close last bracket opened
            if bracket in closers:
                if not openers or openers.pop() != closers[bracket]:
                    return False
            
            # Else, add the bracket as the last opener
            else:
                openers.append(bracket)

        # If the openers stack is empty, the string if valid    
        return not openers
        