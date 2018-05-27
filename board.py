class Board:
    def __init__(self, state=[[None] * 3] * 3, last_move=(None, None)):
        self._state = state
        # Last step: (if computer move, number of cell)
        self._last_move = last_move
        self.free_cells = []
        for i, row in enumerate(state):
            for j, el in enumerate(row):
                if el is None:
                    self.free_cells.append(i * 3 + j + 1)

    def player_move(self, cell):
        self._state[(cell - 1) // 3][cell % 3] = False
        self.free_cells.remove(cell)
        self._last_move = (False, cell)

    def computer_move(self):
        raise NotImplementedError

    def analyse_state(self):
        raise NotImplementedError

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
        for i, row in enumerate(self._state):
            row_str = []
            for j, col in enumerate(row):
                row_str.append(col if col else str(i * 3 + j + 1))
            result.append('\t| ' + ' | '.join(row_str) + ' |')
        return '\t {} \n{} \n\t {} '.format('-' * 11,
                                            '\n\t|---+---+---|\n'.
                                            join(result), '-' * 11)
