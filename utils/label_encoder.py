class LabelEncoder:
    def __init__(self):
        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.,:/()"
        self.char2idx = {char: idx + 1 for idx, char in enumerate(self.characters)}  # 0 is reserved for blank
        self.idx2char = {idx + 1: char for idx, char in enumerate(self.characters)}
        self.blank_label = 0

    def encode(self, text):
        return [self.char2idx[char] for char in text if char in self.char2idx]

    def decode(self, indices):
        return ''.join([self.idx2char.get(idx, '') for idx in indices if idx != self.blank_label])

    def get_vocab_size(self):
        return len(self.char2idx) + 1  # +1 for blank
