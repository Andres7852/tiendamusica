from datetime import datetime
from typing import List, Optional


class Transaction:
    SELL = 1
    SUPPLY = 2

    def __init__(self, transaction_type: int, copies: int):
        self.type = transaction_type
        self.copies = copies
        self.date = datetime.now()


class Disc:
    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid = sid
        self.title = title
        self.artist = artist
        self.sale_price = sale_price
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.transactions: List[Transaction] = []
        self.song_list: List[str] = []

    def add_song(self, song: str):
        self.song_list.append(song)

    def sell(self, copies: int) -> bool:
        if copies > self.quantity:
            return False
        self.quantity -= copies
        self.transactions.append(Transaction(Transaction.SELL, copies))
        return True

    def supply(self, copies: int):
        self.quantity += copies
        self.transactions.append(Transaction(Transaction.SUPPLY, copies))

    def copies_sold(self) -> int:
        return sum(transaction.copies for transaction in self.transactions if transaction.type == Transaction.SELL)

    def __str__(self) -> str:
        return f"SID: {self.sid}\nTitle: {self.title}\nArtist: {self.artist}\nSong List: {', '.join(self.song_list)}"


class MusicStore:
    def __init__(self):
        self.discs: dict[str, Disc] = {}

    def add_disc(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        if sid not in self.discs:
            self.discs[sid] = Disc(sid, title, artist, sale_price, purchase_price, quantity)

    def search_by_sid(self, sid: str) -> Optional[Disc]:
        return self.discs.get(sid, None)

    def search_by_artist(self, artist: str) -> List[Disc]:
        return [disc for disc in self.discs.values() if disc.artist == artist]

    def sell_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False
        return disc.sell(copies)

    def supply_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False
        disc.supply(copies)
        return True

    def worst_selling_disc(self) -> Optional[Disc]:
        if not self.discs:
            return None
        return min(self.discs.values(), key=lambda disc: disc.copies_sold(), default=None)
