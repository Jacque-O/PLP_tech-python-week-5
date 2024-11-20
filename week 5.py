# Parent Class: Book
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
    
    def describe_book(self):
        return f"'{self.title}' by {self.author} ({self.year}) is a {self.genre} novel."

# Child Class: RomanceNovel
class RomanceNovel(Book):
    def __init__(self, title, author, year, protagonist, love_interest):
        super().__init__(title, author, year, genre="Contemporary Romance")
        self.protagonist = protagonist
        self.love_interest = love_interest
    
    def romantic_summary(self):
        return f"In {self.title}, {self.protagonist} finds love with {self.love_interest} in the streets of Paris."

# Example Usage
novel = RomanceNovel(
    title="Love in Paris",
    author="Jacque Odhiambo",
    year=2024,
    protagonist="Marie, a single mother",
    love_interest="Léon, a street musician"
)

print(novel.describe_book())
print(novel.romantic_summary())
