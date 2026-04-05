class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m, n = len(s1), len(s2)

        if m > n:
            return False

        perms1 = {}
        perms2 = {}

        for i in range(m):
            perms1[s1[i]] = perms1.get(s1[i], 0) + 1
            perms2[s2[i]] = perms2.get(s2[i], 0) + 1

        if perms1 == perms2:
            return True

        for i in range(m, n):

            perms2[s2[i]] = perms2.get(s2[i], 0) + 1
            perms2[s2[i-m]] -= 1

            if perms2[s2[i-m]] == 0:
                del perms2[s2[i-m]]

            if perms1 == perms2:
                return True

        return False