import random

import os
from math import log2, ceil

from cipher import Cipher
from puzzle import Puzzle, PuzzleData


class Party:
    def __init__(self, constant, secret_size: int, cipher: Cipher, puzzle_count: int):
        self.secret_size = secret_size
        self.cipher = cipher
        self.puzzle_count = puzzle_count
        self.constant = constant
        self.constant_length = len(constant)
        self.id_length = int(ceil(log2(puzzle_count)))


class Sender(Party):
    def generate_puzzles(self):
        data = {}

        for i in range(self.puzzle_count):
            data[i] = PuzzleData(i, self)

        puzzles = [Puzzle(puzzleData) for puzzleData in data.values()]
        random.shuffle(puzzles)

        return data, puzzles


class Receiver(Party):

    def solve_puzzles(self, puzzles: [Puzzle]):
        puzzle = random.choice(puzzles)
        return self.solve_puzzle(puzzle)

    def solve_puzzle(self, puzzle: Puzzle):

        possible_secrets = 1 << (self.secret_size * 8)

        for possible_secret in range(possible_secrets):
            try:
                padded_secret = int(possible_secret).to_bytes(self.secret_size, "big") + bytearray(
                    puzzle.secret_padding)
                plaintext = self.cipher.decrypt(padded_secret, puzzle.encrypted_message)

                if plaintext[:self.constant_length] == self.constant:
                    id = int.from_bytes(plaintext[self.constant_length:self.constant_length + self.id_length], "big")
                    key = plaintext[self.constant_length + self.id_length:]
                    return id, key
            except ValueError:
                # guessed key is wrong
                continue

        raise Exception("Puzzle cannot be solved")
