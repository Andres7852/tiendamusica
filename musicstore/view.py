import sys

from musicstore.model import MusicStore


class UIConsole:
    
    def __init__(self):
        self.music_store = MusicStore()
        self.options = {
            '1': self.add_disc,
            '2': self.add_songs,
            '3': self.sell_disc,
            '4': self.supply_disc,
            '5': self.search_by_sid,
            '6': self.search_by_artist,
            '7': self.worst_seller,
            '0': self.exit
        }

    def print_menu(self):
        print("====================================")
        print('Bookstore App Menu')
        print('1. Add disc')
        print('2. Add songs')
        print('3. Sell disc')
        print('4. Supply disc')
        print('5. Search by SID')
        print('6. Search by artist')
        print('7. Worst seller')
        print('0. Exit')
        print("====================================")
    
    def run(self):
        while True:
            self.print_menu()
            option = input('Enter option: ')
            action = self.options.get(option)
            if action:
                action()
            else:
                print('Invalid option')
    
    def add_disc(self):
        print(">>> Add disc ========================")
        sid = input('Enter SID: ')
        title = input('Enter title: ')
        artist = input('Enter artist: ')
        sale_price = float(input('Enter sale price: '))
        purchase_price = float(input('Enter purchase price: '))
        quantity = int(input('Enter quantity: '))
        self.music_store.add_disc(sid, title, artist, sale_price, purchase_price, quantity)
    
    def add_songs(self):
        print(">>> Add songs ========================")
        sid = input('Enter SID: ')
        disc = self.music_store.search_by_sid(sid)
        if not disc:
            print('Disc not found')
            return
        
        songs = input('Enter songs separated by comma: ')
        for song in songs.split(','):
            disc.add_song(song.strip())
    
    def sell_disc(self):
        print(">>> Sell disc ========================")
        isbn = input('Enter SID: ')
        quantity = int(input('Enter quantity: '))
        if not self.music_store.sell_disc(isbn, quantity):
            print('Disc not found or not enough quantity')
        else:
            print('Disc sold successfully')
    
    def supply_disc(self):
        print(">>> Supply disc ========================")
        isbn = input('Enter SID: ')
        quantity = int(input('Enter quantity: '))
        if not self.music_store.supply_disc(isbn, quantity):
            print('Disc not found')
        else:
            print('Disc supplied successfully')
    
    def search_by_sid(self):
        print(">>> Search by SID ========================")
        sid = input('Enter SID: ')
        disc = self.music_store.search_by_sid(sid)
        if disc:
            print(disc)
        else:
            print('Disc not found')
    
    def search_by_artist(self):
        print(">>> Search by artist ========================")
        artist = input('Enter artist: ')
        discs = self.music_store.search_by_artist(artist)
        if discs:
            for disc in discs:
                print(disc)
        else:
            print('No discs found')
    
    def worst_seller(self):
        print(">>> Worst seller ========================")
        disc = self.music_store.worst_selling_disc()
        if disc:
            print(disc)
        else:
            print('No disc sold yet')
    
    def exit(self):
        print("\nGoodbye!")
        sys.exit(0)

