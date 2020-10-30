#import wikipedia
import sys
import re
import urllib.request


def get_wikipedia_page(title, lang='en'):
    url = 'https://'+lang+'.wikipedia.org/wiki/'+(title.replace(' ', '_'))
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

title = 'List of Formula One Grands Prix'

try:
    print('process: '+title)
    th = get_wikipedia_page(title)
    r1 = re.findall(r'href="/wiki/[\d][\d][\d][\d]_[\w]*_Grand_Prix"',th)
    list_of_GP = list(set(r1))
except:
    print("Unexpected error:", sys.exc_info()[0])

titles = sorted(list(map(lambda x: x[12: -1].replace('_', ' '), list_of_GP)), reverse=True)


for title in titles:
    try:
        print('process: '+title)
        th = get_wikipedia_page(title)
        with open('texts/'+title+'.txt', 'w', encoding='utf8') as the_file:
            the_file.write(th)
            the_file.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
