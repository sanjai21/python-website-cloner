import urllib.request , sys
output = open("clone.html", 'w')
def clone(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode()
    return html

user_input = input("Enter the link of the website you want to clone : ")

print(clone(user_input), file=output)
print("website cloned successfully, check clone.html :)")
