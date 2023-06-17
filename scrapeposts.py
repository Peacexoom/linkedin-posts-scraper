from bs4 import BeautifulSoup

with open("linkedin.html", errors="ignore") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

span_element = soup.find_all("span", class_="break-words")
 
i = 1
with open("posts.docx", "w") as f:
    for span_text in span_element:
        f.write(str(i) + ". " + span_text.text + "\n")
        i = i + 1