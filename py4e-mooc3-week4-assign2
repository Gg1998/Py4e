def finder(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    
    i = 1
    for tag in tags:
        if i == 18:
            x = tag.get('href', None)
        i = i+1
        
    return x
    
url = input("enter the url")
j =1
while j < 8:
    url = finder(url)
    print(url)
    j = j+1   
