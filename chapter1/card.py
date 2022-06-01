import collections
from random import choice

Card = collections.namedtuple("card", ["rank", "flowers"])


class MyCard:

    ranks = [str(x) for x in range(2, 11)] + list("JQKA")
    flowers = ["spade", "heart", "diamond", "club"]
    flower_value = dict(spade=3, heart=2, diamond=1, club=0)

    def __init__(self):
        self._cards = [Card(r, f) for r in self.ranks for f in self.flowers]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def get_rank_value(self, _card):
        value = self.ranks.index(_card.rank)
        return value * len(self.flower_value) + self.flower_value[_card.flowers]

    def sort_card(self):
        return [c for c in sorted(self._cards, key=self.get_rank_value)]

