class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        '''
        # collections.Counter() is used to count the occurrences of characters in the string
        c = collections.Counter()
        # groupby(colors) function groups consecutive characters in the string
        for x, t in groupby(colors):
            c[x] += max(len(list(t)) - 2, 0)

        if c['A'] > c['B']:
            return True
        return False
       
        a_score = 0
        b_score = 0
        for i in range(1, len(colors) - 1):
            curr_color = colors[i]
            prev_color = colors[i-1]
            next_color = colors[i+1]

            if curr_color == 'A' and prev_color == 'A' and next_color == 'A':
                a_score += 1
            elif curr_color == 'B' and prev_color == 'B' and next_color == 'B':
                b_score += 1
        return a_score > b_score
        '''
        if len(colors) < 3:
            return False

        A_groups = colors.split("B")
        B_groups = colors.split("A")

        Alice_moves = 0
        Bob_moves = 0

        for A_group, B_group in zip(A_groups, B_groups):
            if len(A_group) >= 3:
                move = len(A_group) - 3 + 1
                Alice_moves += move
            if len(B_group) >= 3:
                move = len(B_group) - 3 + 1
                Bob_moves += move

        return Alice_moves > Bob_moves
