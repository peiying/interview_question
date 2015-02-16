class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits.reverse()
        for i in range(len(digits)):
            if digits[i] < 9:
                digits[i] += 1
                digits.reverse()
                return digits
            else:
                digits[i] = 0
        digits.append(1)
        digits.reverse()
        return digits
