class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def traverse(r: int, c: int,visited: set) -> int:
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            neighbours = [[r + 1, c],[r -1,c],[r,c + 1],[r,c - 1]]
            res = grid[r][c]
            for row, col in neighbours:
                res = max(res, grid[r][c] + traverse(row, col, visited))
            visited.remove((r,c))
            return res
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    res = max(res, traverse(r,c, set()))
                    
        return res
            
        
        
if __name__ == "__main__":
    sol = Solution()
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    result = sol.getMaximumGold(grid)
    print(result)