import re
from bs4 import BeautifulSoup
#
# a = 'xxyy123'
# b = re.findall('x.?', a)
# print(b)

# old_url = 'http://www.ttplus.cn/?pageNum=2'
# total_page = 20
#
# for i in range(2, total_page+1):
#     new_link = re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
#     print(new_link)
#

#headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Mobile Safari/537.36'}
html = ""
soup = BeautifulSoup(open('a.html'),'html.parser')
print(soup.prettify())


html2 = 'http://example.com/tillie'