class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        cols = [0] * n
        rows = [0] * m
        no_odds_col ,no_even_col ,no_odds_row ,no_even_row = 0, n, 0, m
        for r, c in indices:
            cols[c] += 1
            rows[r] += 1
        for i in range(n):
            no_odds_col += int(cols[i] % 2 != 0)
            no_even_col -= int( not cols[i] % 2 == 0)
        for i in range(m):
            # print(rows[i])
            no_odds_row += int(rows[i] % 2 != 0)
            no_even_row -= int(not rows[i] % 2 == 0)
        # print(rows, cols)
        # print(int(1 % 2 == 0))
        # print(no_odds_row, no_even_col , no_odds_col, no_even_row)
        return (no_odds_row * no_even_col) + (no_odds_col * no_even_row)
