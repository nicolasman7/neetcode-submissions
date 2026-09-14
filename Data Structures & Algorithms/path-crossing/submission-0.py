class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        seen.add((0,0))
        current = [0,0]
        for i in path:
            if i == 'E':
                current[0] += 1
            elif i == 'W':
                current[0] -= 1
            elif i == 'N':
                current[1] += 1
            else:
                current[1] -= 1
            if tuple(current) in seen:
                return True
            seen.add(tuple(current))
        return False