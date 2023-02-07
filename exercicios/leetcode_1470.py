# 1470. Shuffle the Array

class Solution:
    result = []
    def shuffle(self, nums, n):
        self.result = []
        for i in range(2 * n):
            self.result.append(0)

        for i in range(n):
            self.result[2 * i] = nums[i]
            self.result[2 * i + 1] = nums[n + i]

        return self.result


solve = Solution()
print(solve.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))

# // [x1, x2, x3, y1, y2, y3]
# // [0, 1, 2, 3, 4, 5]
