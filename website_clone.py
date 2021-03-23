import urllib.request , sys
c = open("clone.html", 'w')
def clone(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode()
    print(html, file=c)

clone(sys.argv[1])