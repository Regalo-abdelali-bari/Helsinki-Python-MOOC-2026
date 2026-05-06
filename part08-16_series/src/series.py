# Write your solution here:
class Series:
    def __init__(self , name : str , n_s : int , genre : list):
        self.title = name
        self.seasons = n_s
        self.genre = genre
        self.r = 0
        self.l = 0
        self.a = 0
    def rate(self,rating:int):
        self.r += rating
        self.l += 1 
        self.a = self.r / self.l

    def __str__(self):
        if self.l > 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genre)}\n{self.l} ratings, average {self.a:.1f} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genre)}\nno ratings"

def minimum_grade(rating: float, series_list: list):
    series_accept = []
    for serie in series_list:
        if serie.r >= rating:
            series_accept.append(serie)
    return series_accept

def includes_genre(genre: str, series_list: list):
    series_accept = []
    for serie in series_list:
        if genre in serie.genre:
            series_accept.append(serie)
    return series_accept




if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)