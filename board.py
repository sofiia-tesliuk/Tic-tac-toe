class Board:
    def __init__(self, player, computer):
        self._state = [[None] * 3] * 3
        self._last_step = (None, None)
        self._player = player
        self._computer = computer
        self.free_cells = [i + 1 for i in range(9)]

    def player_move(self, cell):
        pass

    def computer_move(self):
        pass

    def state_result(self):
        pass

    def __str__(self):
        result = []
        for i, row in enumerate(self._state):
            row_str = []
            for j, col in enumerate(row):
                row_str.append(col if col else str(i * 3 + j + 1))
            result.append('\t| ' + ' | '.join(row_str) + ' |')
        return '\t {} \n{} \n\t {} '.format('-' * 11,
                                            '\n\t|---+---+---|\n'.
                                            join(result), '-' * 11)


class GameOver(Exception):
    pass
