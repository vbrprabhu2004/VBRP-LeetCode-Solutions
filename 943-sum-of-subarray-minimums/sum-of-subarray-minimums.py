''' My understanding code
class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        total = 0
        for start in range(n):
            for end in range(start, n):
                subarray = arr[start : end+1]
                total += min(subarray)
        return total
'''
class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        
        # Arrays to store the number of elements greater before and after
        stack = []
        prev_less = [0] * n
        next_less = [0] * n

        # Previous Less Element count
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            prev_less[i] = count
            stack.append((arr[i], count))
        
        stack = []
        # Next Less Element count
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            next_less[i] = count
            stack.append((arr[i], count))
        
        # Calculate result using contributions
        result = 0
        for i in range(n):
            result += arr[i] * prev_less[i] * next_less[i]
            result %= MOD
        
        return result
