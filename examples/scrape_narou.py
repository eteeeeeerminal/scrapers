import os
from scrapers import NarouScraper

i = 1
while os.path.exists(save_dir:=f"data/narou{i}"):
    i += 1

narou = NarouScraper(save_dir)
narou.get_books_thegenre("301-302-303-304-305-403", novel_n=1000, parts_per_novel=10)
narou.save()