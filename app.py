import requests
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from html import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url_string = None
    text = None
    message = None
    url_chars = []
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            # Remove unsupported elements
            for tag in soup(['script', 'style', 'iframe', 'object', 'embed']):
                tag.decompose()

            # Extract text from the soup
            b_tags = soup.find_all('b', class_="ref")
            if b_tags:
                for b in b_tags:
                        val = b.get('value')
                        if val:
                            url_chars.append(val)
                url_string = ''.join(url_chars)
                if url_string:
                    hidden_url_response = requests.get(url_string, timeout=10)
                    hidden_soup = BeautifulSoup(hidden_url_response.text, 'lxml')
                    message = escape(hidden_soup.get_text(separator=' ', strip=True))
            else:
                # Add fallback for when no <b> tags are found
                content = escape(soup.get_text(separator=' ', strip=True))
                max_length = 2000
                if len(content) > max_length:
                    text = content[:max_length] + '...'
                else:
                    text = content

        except Exception as e:
            url_string = f"Error fetching or parsing the URL: {e}"
            text = f"Error fetching or parsing the URL: {e}"
    return render_template('index.html', text=text, url_string=url_string, message=message)

if __name__ == '__main__':
    app.run(debug=True)
