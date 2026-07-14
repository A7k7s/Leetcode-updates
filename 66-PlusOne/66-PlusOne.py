# Last updated: 7/14/2026, 2:05:21 PM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] += 1  # If last digit is less than 9, simply add 1
        else:
            # In case last digit is 9, we need to propagate the carry
            n = 1  # Start with carry of 1
            for i in range(len(digits) - 1, -1, -1):  # Start from the last digit
                digits[i] += n  # Add the carry (1)
                if digits[i] == 10:  # If we get 10, carry over
                    digits[i] = 0
                    n = 1  # Continue carrying
                else:
                    n = 0  # No more carry needed
                    break  # Break if no further carry is needed

            if n == 1:  # If carry is still 1, prepend 1 to the list
                digits.insert(0, 1)

        return digits