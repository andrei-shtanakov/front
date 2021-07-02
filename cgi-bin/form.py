#!/usr/bin/env python3
import cgi
from apiclient import APIClient



class MyClient(APIClient):

    def list_documents(self):
        url = "http://192.168.1.26:8000/api/docs/"
        return self.get(url)

    def add_document(self, document_info):
        url = "http://192.168.1.26:8000/api/docs/"
        return self.post(url, data=document_info)

client = MyClient()
docs = client.list_documents()



#form = cgi.FieldStorage()
#text1 = form.getfirst("TEXT_1", "не задано")
#text2 = form.getfirst("TEXT_2", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
for doc in docs:
    print("<p>TEXT_1: {}</p>".format(doc))
#print("<p>TEXT_1: {}</p>".format(text1))
#print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")

