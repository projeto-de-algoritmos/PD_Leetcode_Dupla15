# 22. Generate Parentheses

class Solution(object):
    result = []

    def valid(self, arrange):
        check_sequence = 0

        for char in arrange:
            if char != '(': check_sequence -= 1
            else: check_sequence += 1
            if check_sequence < 0: return False

        return check_sequence == 0


    def generate_sequence(self, result, size, arrange = []):
        if len(arrange) == 2 * size:
            if self.valid(arrange):
                result.append("".join(arrange))
                return result
        else:
            arrange.append('(')
            self.generate_sequence(result, size, arrange)
            arrange.pop()
            arrange.append(')')
            self.generate_sequence(result, size, arrange)
            arrange.pop()


    def generateParenthesis(self, size):
        self.result = []
        self.generate_sequence(self.result, size)
        return self.result


solve = Solution()
print(solve.generateParenthesis(int(input('Digite o número de parenteses: '))))
