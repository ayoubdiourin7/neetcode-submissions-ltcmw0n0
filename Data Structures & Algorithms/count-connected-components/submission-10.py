class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        seen = {}
        res = 0

        for i, e in enumerate(edges):

            if not (e[0] in seen or e[1] in seen):
                res += 1
                index = i

            elif e[0] in seen and e[1] in seen and seen[e[0]] != seen[e[1]]:
                res -= 1

                a = seen[e[0]]
                b = seen[e[1]]
                index = min(a, b)
                old = max(a, b)

                # update all nodes belonging to old component
                for k in seen:
                    if seen[k] == old:
                        seen[k] = index

            elif e[0] in seen:
                index = seen[e[0]]

            else:
                index = seen[e[1]]

            seen[e[0]] = index
            seen[e[1]] = index

        return res + n - len(seen)