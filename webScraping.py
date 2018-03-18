import bs4
import urllib.request

raw_html = urllib.request.urlopen("http://news.ycombinator.com").read()
soup = bs4.BeautifulSoup(raw_html, "html.parser")

print("Links :\n\n")
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

print("Images :\n\n")
images = soup .find_all("img")
for image in images:
    print(image.get("src"))

