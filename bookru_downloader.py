import urllib.request
from PIL import Image

#Number of pages in ypur book
pages_count = 0

#Insert token of your book here
token = ""

# Retrieving the resource located at the URL
# and storing it in the file name a.png
for i in range(1, pages_count+1, 1):
    url = "https://reader.new.book.ru/api/books/page_view/"+str(i)+"/" + token
    urllib.request.urlretrieve(url, "page"+str(i)+".png")
    img = Image.open(r"page"+str(i)+".png")
    img.save(r"page"+str(i)+".png")
    print("Картинок загружено:" + str(i))