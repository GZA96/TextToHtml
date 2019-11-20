"""
    This module is responsible for the html formatting of the elements
    and the full html structure of the document
"""


def to_html_list(lines):
    """ Format a list block of txt into an html list"""
    list_elements = ["\t<li>\n\t\t"+line+"\n\t</li>\n" for line in lines]
    return "<ul>\n"+"".join(list_elements)+"</ul>\n"


def to_html_paragraph(block):
    """ Format a paragraph into an html paragraph"""
    return "<p>\n"+block+"\n</p>\n"


def to_html_header(header):
    """ Format a header block of txt into an html header"""
    return "<h1>"+header+"</h1>\n"


def to_html_new_line():
    """ Return an html new line """
    return "<br />\n"


def to_html_url(url):
    """ Format a url block of txt into an html url"""
    return "<a href=\""+url+"\">"+url+"</a>"


def to_html_title(title):
    """ Format a document title into an html title"""
    return "<title>\n\t"+title+"</title>\n"


class HtmlDocument:
    """ This class represents the full html document structure """
    extension = '.html'

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __str__(self):
        top_part = "<!DOCTYPE html>\n<html>\n"
        doc_head = "<head>\n"+str(self.title)+"</head>\n"
        doc_body = "<body>\n"+"".join([str(x) for x in self.body])+"</body>"
        end_part = "\n</html>"
        return top_part+doc_head+doc_body+end_part
