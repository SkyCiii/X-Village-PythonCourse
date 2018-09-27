from requests_html import HTMLSession

url = 'http://quotes.toscrape.com/'
session = HTMLSession()
response = session.get(url)
elements = response.html.find('.text')[1]
print (type(elements))
print (elements)
print (elements.text)
print (elements.attrs)

elements_2 = response.html.find('.tag')[0]
print (type(elements_2))
print (elements_2)
print (elements_2.attrs['href'])
print (elements_2.text)

session = HTMLSession()

i = 0
response_3 = session.get(url)
elements_3 = response_3.html.find('nav a')[0]
print (type(elements_3.attrs['href']))
print (elements_3.attrs['href'])
url= 'http://quotes.toscrape.com' + elements_3.attrs['href']

while i < 8 :
    response_3 = session.get(url)
    elements_3 = response_3.html.find('nav a')[1]
    elements_4 = response_3.html.find('.text')
    for element in elements_4 :
        print (element.text)
    print (type(elements_3.attrs['href']))
    print (elements_3.attrs['href'])
    print ()
    url= 'http://quotes.toscrape.com' + elements_3.attrs['href']
    i = i + 1
# for element in elements :
#     print (element.text)