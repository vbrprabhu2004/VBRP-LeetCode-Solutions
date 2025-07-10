class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5:
            return False
        
        five_dollars = 0
        ten_dollars = 0

        for x in bills:
            if x == 5:
                five_dollars += 1
            elif x == 10:
                if five_dollars > 0:
                    five_dollars -= 1
                else:
                    return False
                ten_dollars += 1
            else:
                if five_dollars > 0 and ten_dollars > 0:
                    five_dollars -= 1
                    ten_dollars -= 1
                elif five_dollars > 2:
                    five_dollars -= 3
                else:
                    return False
            print(five_dollars, ten_dollars)
        return True