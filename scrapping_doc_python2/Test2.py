import os
import html2text

for file in os.listdir("/python_doc"):
    if file.endswith(".html"):
        html_page = open(file, "r").read()
        #print file
        print html2text.HTML2Text().handle(html_page)
