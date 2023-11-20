import re

def parse_html_tags(html):
    # Regular expression to find HTML tags
    pattern = re.compile(r'<\s*([a-zA-Z0-9]+)(\s+[^>]*)?\s*>')

    # Find all matches of the pattern in the HTML content
    matches = pattern.findall(html)

    # Extract tag names from the matches
    tags = [match[0] for match in matches]

    return tags

# Example HTML content
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sample HTML</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>This is a sample HTML document.</p>
    <div>
        <tr> 
            <td> 
            </td>
        </tr>
        <p>Nested paragraph.</p>
    </div>
</body>
</html>
'''

tags_found = parse_html_tags(html_content)
print("HTML Tags found:", tags_found)
