from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        
    def handle_starttag(self, tag, attrs):
        if tag in ['div', 'section', 'p', 'h1', 'h2', 'h3']:
            self.tags.append(tag)

    def handle_endtag(self, tag):
        if tag in ['div', 'section', 'p', 'h1', 'h2', 'h3']:
            if self.tags[-1] == tag:
                self.tags.pop()
            else:
                print(f"Mismatched tag: expected {self.tags[-1]}, found {tag}")

parser = MyHTMLParser()
with open('index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())
print("Open tags left:", parser.tags)
