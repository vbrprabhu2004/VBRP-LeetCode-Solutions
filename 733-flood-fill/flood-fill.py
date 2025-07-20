class Solution(object):
    def floodFill(self, image, sr, sc, color):

        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]

        # If the starting pixel already has the new color, no need to process
        if original_color == color:
            return image

        def dfs(r, c):
            # Check bounds and if the pixel is the original color
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original_color:
                return

            # Change the color
            image[r][c] = color

            # Recursive calls in all four directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        dfs(sr, sc)
        return image
