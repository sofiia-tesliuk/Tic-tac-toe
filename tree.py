from board import Board
from tnode import Tnode


class Tree:
    def __init__(self):
        self._root = None

    def set_root(self, board):
        if isinstance(board, Board):
            self._root = Tnode(board)

