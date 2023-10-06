from abc import ABC, abstractmethod


class Roll:
    def __init__(self, pins: int):
        self.pins = pins


class Frame(ABC):
    def __init__(self):
        self.next_frame: Frame = None
        self.rolls: list[Roll] = []

    @abstractmethod
    def add_roll(self, pins: int):
        pass

    @abstractmethod
    def score(self) -> int:
        pass

    def is_strike(self) -> bool:
        if self.rolls[0].pins == 10:
            return True

    def is_spare(self) -> bool:
        if self.rolls[0].pins + self.rolls[1].pins == 10:
            return True


class NormalFrame(Frame):
    def __init__(self):
        super().__init__()

    def add_roll(self, pins: int):
        self.rolls.append(Roll(pins))

    def score(self) -> int:

        if self.is_spare():
            return 10 + self.next_frame.rolls[0].pins
        elif self.is_strike():
            return 10 + self.next_frame.rolls[0].pins + self.next_frame.rolls[1].pins
        else:
            return self.rolls[0].pins + self.rolls[1].pins


class TenthFrame(Frame):
    def __init__(self):
        super().__init__()
        self.extra_roll: Roll = None

    def add_roll(self, pins: int):
        self.rolls.append(Roll(pins))

    def score(self) -> int:
        if self.is_strike():
            return self.rolls[0].pins + self.rolls[1].pins + self.extra_roll.pins
        elif self.is_spare():
            return self.rolls[0].pins + self.rolls[1].pins + self.extra_roll.pins


class Game:
    def __init__(self):
        self.frames: list[Frame] = []

    def roll(self, pins: int):
        pass

    def score(self) -> int:
        pass



