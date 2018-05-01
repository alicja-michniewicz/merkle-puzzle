import os


class PuzzleData:

    def __init__(self, id: int, party) -> None:
        self.id = id
        self.secret = os.urandom(party.secret_size)
        self.secret_padding = bytearray(party.cipher.get_key_size() - party.secret_size)
        self.key = party.cipher.generate_key()
        self.message = party.constant + self.id.to_bytes(party.id_length, "big") + self.key
        self.encrypted_message = party.cipher.encrypt(self.secret + self.secret_padding, self.message)


class Puzzle:

    def __init__(self, puzzle: PuzzleData) -> None:
        self.encrypted_message = puzzle.encrypted_message
        self.secret_padding = puzzle.secret_padding
