class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Helper function to perform DFS
        def dfs(i, j):
            # If the current position is out of bounds or is water ('W'), return
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            
            # Mark the current land as visited (by turning it into water 'W')
            grid[i][j] = 'W'
            
            # Explore all 4 possible directions: up, down, left, right
            dfs(i - 1, j)  # up
            dfs(i + 1, j)  # down
            dfs(i, j - 1)  # left
            dfs(i, j + 1)  # right
        
        # Count the number of distinct islands
        island_count = 0
        
        # Loop through the entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # When an unvisited land is found, it's a new island
                if grid[i][j] == 'L':
                    island_count += 1
                    # Start DFS to mark all connected land as visited
                    dfs(i, j)
        
        return island_count


# Test cases
if __name__ == "__main__":
    # Test case 1: One large island
    grid1 = [
        ["L", "L", "L", "L", "W"],
        ["L", "L", "W", "L", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"]
    ]
    solution = Solution()
    print(solution.getTotalIsles(grid1))  # Expected Output: 1

    # Test case 2: Three separate islands
    grid2 = [
        ["L", "L", "W", "W", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "L", "W", "W"],
        ["W", "W", "W", "L", "L"]
    ]
    solution = Solution()
    print(solution.getTotalIsles(grid2))  # Expected Output: 3
