from lxml import html

def html_minify(html_code):
    dom = html.fromstring(html_code)
    html_code = html.tostring(dom, method='xml')

    minified_lines = []
    for line in html_code.split('\n'):
        minified_line = line.strip()
        if minified_line:
            minified_lines.append(minified_line)

    return "".join(minified_lines)