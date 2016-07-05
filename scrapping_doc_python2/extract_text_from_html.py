#! Python3

import html2text

h = html2text.HTML2Text()

#html_page = open("python_doc/index.html", "r")
html_page = open("python_doc/docs.python.org/2/tutorial/introduction.html", "r")

f = html_page.read()

w = open("out.txt", "wb")
w.write(html2text.html2text(f).encode('utf-8'))

html_page.close()
w.close()


h.ignore_links = False

#print h.handle('<p>Hello, <a href="http://earth.google.com/">world</a>!')
print(h.handle(f))
