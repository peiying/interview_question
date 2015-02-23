class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        numList = []
        if numerator * denominator < 0:
            numList.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)
        numList.append(str(numerator / denominator))
        r = numerator % denominator
        if r == 0:
            return "".join(numList[:])
        numList.append('.')
        map = {}
        count = 0
        temp = []
        while True:
            if r == 0:
                break
            if r in map:
                break
            map[r] = count
            count += 1
            r *= 10
            temp.append(str(r / denominator))
            r %= denominator
        if r != 0:
            for j in xrange(map[r]):
                numList.append(temp[j])
            numList.append('(')
            for j in xrange(map[r], len(temp)):
                numList.append(temp[j])
            numList.append(')')
        else:
            for j in xrange(len(temp)):
                numList.append(temp[j])
        return "".join(numList[:])
            
