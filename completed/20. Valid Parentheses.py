class Solution:
    def isValid(self, s: str) -> bool:
        """accepted"""
        opening = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        expected_closing_bracket = ""
        for char in s:
            print(char)
            if char in opening:
                stack.append(char)
                expected_closing_bracket = opening.get(char)
                print("\t", stack)
                print(stack)
                continue
            if char != expected_closing_bracket:
                return False
            del stack[-1]
            expected_closing_bracket = opening.get(stack[-1]) if stack else ""
            print("\t", stack)
        print(s)
        print(stack)
        if stack:
            return False
        return True


if __name__ == "__main__":
    S = Solution()
    inp = "()[]{}"
    inp = "(]"
    inp = "{[]}"
    print(S.isValid(inp))