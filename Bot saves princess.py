def displayPathtoPrincess(n, grid):
    # Find the bot and princess positions
    bot_pos = None
    princess_pos = None
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_pos = (i, j)
            elif grid[i][j] == 'p':
                princess_pos = (i, j)
    
    # Calculate vertical and horizontal moves
    vertical_moves = princess_pos[0] - bot_pos[0]
    horizontal_moves = princess_pos[1] - bot_pos[1]
    
    # Generate moves
    moves = []
    
    # Vertical moves
    if vertical_moves > 0:
        moves.extend(['DOWN'] * abs(vertical_moves))
    elif vertical_moves < 0:
        moves.extend(['UP'] * abs(vertical_moves))
    
    # Horizontal moves
    if horizontal_moves > 0:
        moves.extend(['RIGHT'] * abs(horizontal_moves))
    elif horizontal_moves < 0:
        moves.extend(['LEFT'] * abs(horizontal_moves))
    
    return moves

# Example usage and testing
def main():
    # Test case from the problem statement
    n = 3
    grid = [
        ['−', '−', '−'],
        ['−', 'm', '−'],
        ['p', '−', '−']
    ]
    
    # Get and print moves
    path = displayPathtoPrincess(n, grid)
    for move in path:
        print(move)

# Uncomment to test
# if __name__ == "__main__":
#     main()


1. The function `displayPathtoPrincess` first finds the positions of the bot ('m') and the princess ('p') in the grid.

2. It then calculates the vertical and horizontal moves needed to reach the princess:
   - Vertical moves depend on the difference in row indices
   - Horizontal moves depend on the difference in column indices

3. The moves are generated based on the direction:
   - Positive vertical difference means moving DOWN
   - Negative vertical difference means moving UP
   - Positive horizontal difference means moving RIGHT
   - Negative horizontal difference means moving LEFT

4. The number of moves for each direction is the absolute value of the difference.

5. The moves are collected in a list and returned.

For the given sample input:
- The bot is at (1, 1)
- The princess is at (2, 0)
- This requires one DOWN move and one LEFT move

The solution ensures:
- Minimal number of moves to reach the princess
- Moves are either UP, DOWN, LEFT, or RIGHT
- Works for any valid grid configuration where the princess is in one of the four corners

Time complexity is O(n²) due to finding the positions, and space complexity is O(1) as the grid size is limited.

