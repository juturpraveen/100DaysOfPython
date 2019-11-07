import bs4, requests
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)
# print(noStarchSoup.select('div'))
print(noStarchSoup.select('input[name]'))