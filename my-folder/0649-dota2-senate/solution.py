class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQ = []
        dQ = []
        n = len(senate)

        for i, char in enumerate(senate):
            if char == 'R':
                rQ.append(i)
            else:
                dQ.append(i)

        while rQ and dQ:
            if(rQ[0] < dQ[0]):
                rQ.append(rQ[0] + n)
            else:
                dQ.append(dQ[0] + n)

            rQ.pop(0)
            dQ.pop(0)

        return "Radiant" if rQ else "Dire"
