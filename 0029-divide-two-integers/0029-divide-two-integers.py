class Solution(object):
    def divide(self, dividend, divisor):

        max_int = 2**31 - 1
        min_int = -(2**31)

        if dividend == min_int and divisor == -1:
            return max_int

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp_d = divisor
            multiple = 1

            while dividend >= (temp_d << 1):
                temp_d <<= 1
                multiple <<= 1

            dividend -= temp_d
            quotient += multiple

        return -quotient if negative else quotient