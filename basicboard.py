class BasicBoard:
    WIN_POINTS = 1
    LOSE_POINTS = -100
    DRAW_POINTS = 0

    def analyse_state(self):
        """
        Analysing current state.
        If there is winning combinations or no more steps.
        :return: points of analysing
        """
        # list of list of combinations
        cells = [[(i, j) for j in range(3)] for i in range(3)]
        cells += [[(j, i) for j in range(3)] for i in range(3)]
        cells += [[(i, i) for i in range(3)]]
        cells += [[(i, 2 - i) for i in range(3)]]
        for combination in cells:
            value = set()
            for i, j in combination:
                value.add(self.state[i][j])
            if len(value) == 1:
                if True in value:
                    self.last_state = True
                    return self.WIN_POINTS
                elif False in value:
                    self.last_state = True
                    return self.LOSE_POINTS
        if not self.free_cells:
            self.last_state = True
        return self.DRAW_POINTS

    @staticmethod
    def number_cell_to_state_indexes(number):
        """
        :param number: number of cell in board
        :return: cell as indexes in state
        """
        return (number - 1) // 3, (number - 1) % 3

    def __str__(self):
        """
        Example:
         -----------
        | 1 | 2 | X |
        |---+---+---|
        | 4 | X | 6 |
        |---+---+---|
        | 7 | 8 | O |
         -----------
        """
        result = []
        for i, row in enumerate(self.state):
            row_str = []
            for j, col in enumerate(row):
                row_str.append(str(col) if col is not None else str(i * 3 + j + 1))
            result.append('\t| ' + ' | '.join(row_str) + ' |')
        return '\t {} \n{} \n\t {} '.format('-' * 11,
                                            '\n\t|---+---+---|\n'.
                                            join(result), '-' * 11)