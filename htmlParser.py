import re

def parse_html_tags(html):
    pattern = re.compile(r'<\s*([a-zA-Z0-9]+)(\s+[^>]*)?\s*>')

    matches = pattern.findall(html)

    tags = [match[0] for match in matches]

    return tags

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
