class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        counters = 1
        countert = 1

        for i in range(len(s)):
            sLetter = s[i]
            tLetter = t[i]

            if sLetter not in sMap:
                sMap[sLetter] = counters
                counters += 1

            if tLetter not in tMap:
                tMap[tLetter] = countert
                countert += 1

            if sMap[sLetter] != tMap[tLetter]:
                print(sMap,tMap)
                return False

        print(sMap,tMap)
        return True