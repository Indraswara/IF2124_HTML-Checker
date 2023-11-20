from bs4 import BeautifulSoup

def check_specific_tags(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        # Specific tags to check
        specific_tags = [
            'html', 'body', 'title', 'link', 'script', 'h1', 'h2', 'h3', 'h4', 'h5',
            'h6', 'p', 'br', 'em', 'b', 'abbr', 'strong', 'small', 'hr', 'div', 'a',
            'img', 'button', 'form', 'input', 'table', 'tr', 'td', 'th'
        ]

        tags_array = []

        for tag_name in specific_tags:
            tag = soup.find(tag_name)
            if tag:
                opening_tag = f"<{tag_name}>"
                closing_tag = f"</{tag_name}>"
                tags_array.append(opening_tag)
                tags_array.append(closing_tag)

        return tags_array

    except FileNotFoundError:
        return "File not found."

# Example usage
file_path = 'test.html'  # Replace this with your HTML file path
result = check_specific_tags(file_path)
print(result)
