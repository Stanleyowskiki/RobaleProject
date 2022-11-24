from abc import ABC, abstractmethod
from array import *
from enum import Enum


class RobalEnum(Enum):
    K = 0
    M = 1
    P = 2
    Z = 3


class Robal(ABC):
    lastID = 0

    @abstractmethod
    def __init__(self, side):
        self.move = 0
        self.attack = 0
        self.toughness = 0
        self.army = None
        self.side = side
        self.field = None

        self.short_name = ""
        self.validMoves = []
        self.invalidMoves = []
        self.moveToExamine = []

        self.state = "moved"  # "to move", "won't move"

    def recruitNeighbours(self):
        for field in self.field.getNeighbours():
            if field is not None and field.bug is not None and field.bug.side == self.side and field.bug.army is None:
                self.army.addBug(field.bug)
                field.bug.recruitNeighbours()

    def setField(self, field):
        self.field = field

    def moveBugTo(self, field):
        if self.field is not None:
            self.field.bug = None
        self.field = field
        self.field.bug = self

    def clone(self):
        clone = self.__class__.__init__(self.side)
        return clone

    def hasEnemyInSurrounding(self):
        for field in self.field.getNeighbours():
            if field is not None and field.bug is not None and field.bug.side != self.side:
                return True
        return False

    def setMove(self, move):
        self.move = move


class Konik(Robal):

    def __init__(self, side):
        self.max_move = 3
        self.move = 3
        self.attack = 0
        self.toughness = array('i', [1])
        self.side = side
        self.army = None
        self.field = None
        self.short_name = RobalEnum.K
        self.validMoves = []
        self.invalidMoves = []
        self.moveToExamine = []


class Mrowka(Robal):

    def __init__(self, side):
        self.max_move = 4
        self.move = 4
        self.attack = 1
        self.toughness = array('i', [3, 4])
        self.side = side
        self.army = None
        self.field = None
        self.short_name = RobalEnum.M
        self.validMoves = []
        self.invalidMoves = []
        self.moveToExamine = []


class Pajak(Robal):

    def __init__(self, side):
        self.max_move = 4
        self.move = 4
        self.attack = 3
        self.toughness = array('i', [1, 2, 3])
        self.side = side
        self.army = None
        self.field = None
        self.short_name = RobalEnum.P
        self.validMoves = []
        self.invalidMoves = []
        self.moveToExamine = []


class Zuk(Robal):

    def __init__(self, side):
        self.max_move = 2
        self.move = 2
        self.attack = 5
        self.toughness = array('i', [4, 5, 6])
        self.side = side
        self.army = None
        self.field = None
        self.short_name = RobalEnum.Z
        self.validMoves = []
        self.invalidMoves = []
        self.moveToExamine = []
