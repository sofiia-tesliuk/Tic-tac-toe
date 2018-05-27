from tree import Tree


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
        tree = Tree(self._state, self._last_move)

    def analyse_state(self):
        # list of list of combinations
        cells = [[(i, j) for j in range(3)] for i in range(3)]
        cells += [[(j, i) for j in range(3)] for i in range(3)]
        cells += [[(i, j) for j in [i, 3 - i]] for i in range(3)]
        print('cells: {}'.format(cells))
        for combination in cells:
            value = set()
            for i, j in combination:
                value.add(self._state[i][j])
            if len(value) == 1:
                if value.pop() is True:
                    return 1
                elif value.pop() is False:
                    return -1
        return 0

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
