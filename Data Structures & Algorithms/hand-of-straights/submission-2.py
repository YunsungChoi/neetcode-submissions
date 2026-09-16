class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0: return False

        count = Counter(hand)
        sortedCount = sorted(count)
        
        for num in sortedCount:
            while count[num] > 0:
                for i in range(num, num + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        
        return True
