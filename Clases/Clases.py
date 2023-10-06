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
        pass

    def is_spare(self) -> bool:
        pass


class NormalFrame(Frame):
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
    extra_roll: Roll = None

    def add_roll(self, pins: int):
        self.rolls.append(Roll(pins))

    def score(self) -> int:
        pass


class Game:
    def __init__(self):
        self.frames: list[Frame] = []

    def roll(self, pins: int):
        pass

    def score(self) -> int:
        pass



