# Problem 2: First Non-Repeating Character
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def firstNonRepeatingChar(self, s):
        frequency = {}

        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        for char in s:
            if frequency[char] == 1:
                return char

        return -1


solution = Solution()
s = input("Enter a string: ")
print(solution.firstNonRepeatingChar(s))
