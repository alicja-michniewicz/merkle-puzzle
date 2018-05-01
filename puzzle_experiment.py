import os

from cipher import AesCBC128
from party import Sender, Receiver

CONSTANT = os.urandom(4)
SECRET_SIZE = 1
CIPHER = AesCBC128()
PUZZLE_COUNT = 1 << 20

alice = Sender(CONSTANT, SECRET_SIZE, CIPHER, PUZZLE_COUNT)
bob = Receiver(CONSTANT, SECRET_SIZE, CIPHER, PUZZLE_COUNT)

data, puzzles = alice.generate_puzzles()

print("alice: generated {} puzzles".format(PUZZLE_COUNT))

id, key = bob.solve_puzzles(puzzles)

print("bob: id {}, key {}".format(id, key))
print("alice: id {}, key {}".format(id, data[id].key))
assert data[id].key == key
