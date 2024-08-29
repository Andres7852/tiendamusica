from datetime import datetime
import datetime
from typing import List, Any


class Transaction:
    SELL = 1
    SUPPLY = 2

    def _init_(self, type: int, copies: int):
        self.type = type
        self.copies = copies
        self.date = datetime.datetime.now()


class Disc:
    def _init_(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid = sid
        self.title = title
        self.artist = artist
        self.sale_price = sale_price
        self.purchase_price = purchase_price
        self.quantity = quantity
        self.transactions = []
        self.song_list = []

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
        return sum(t.copies for t in self.transactions if t.type == Transaction.SELL)

    def _str_(self) -> str:
        return f"SID: {self.sid}\nTitle: {self.title}\nArtist: {self.artist}\nSong List: {', '.join(self.song_list)}"


class MusicStore:
    def _init_(self):
        self.discs = {}

    def add_disc(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        if sid not in self.discs:
            self.discs[sid] = Disc(sid, title, artist, sale_price, purchase_price, quantity)

    def search_by_sid(self, sid: str) -> 'Disc | None':
        return self.discs.get(sid)

    def search_by_artist(self, artist: str) -> list['Disc']:
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

    def worst_selling_disc(self) -> 'Disc | None':
        if not self.discs:
            return None
        return min(self.discs.values(), key=lambda disc: disc.copies_sold())
