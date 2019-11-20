import re
import html_formatter
"""
    This module's objective is to read the file and parse it's different blocks (paragraph, lists, title, headers...)
    and then pass them to the language formatter of desire. (HTML in this case)     
"""

# Regular expressions needed to identify blocks
rules = {
    'list': re.compile(r"^\s*-"),
    'url': re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
}


def is_list(block):
    """ Checks whether a block is a list using the appropriate regEx """
    if re.match(rules['list'], block):
        return True
    else:
        return False


def is_header(txt):
    """ Tests whether txt is a header or not """
    if len(txt) < 70 and not is_url(txt) and txt.rfind(":") != len(txt)-1:
        return True
    return False


def is_url(txt):
    """ Tests whether txt is a url or not """
    if re.match(rules['url'], txt):
        return True
    return False


def find_urls(txt):
    """ Finds every occurrence of a url that matches the url pattern stored in rules={...} found in txt"""
    return re.findall(rules['url'], txt)


class Parser:

    def __init__(self, in_file_path, o_file_path):
        self.file_path = in_file_path
        self.output_path = o_file_path
        self.processed_list = list()

    def read_file(self):
        """ Reads a file and returns the text in string form"""
        with open(self.file_path, "r+") as f:
            whole_txt = f.read()
        return whole_txt

    def process_information(self, txt):
        """ Processes and classifies each block found in txt argument """
        blocks = txt.split("\n")
        reading_list = False
        storing = None

        for b in blocks:
            # First of all we evaluate if it's a list
            if is_list(b):
                # We flag that we are reading a list
                reading_list = True
                if storing is None:
                    storing = [b, ]
                else:
                    storing.append(b)
            else:
                # If we were reading a list... -> Flag down - store the list - List = None
                if reading_list is True:
                    reading_list = False
                    formatted_list = html_formatter.to_html_list(storing)
                    self.processed_list.append(formatted_list)
                    storing = None

                # Once we know it's not a list, we evaluate the remaining possibilities
                if b == "":
                    formatted_newline = html_formatter.to_html_new_line()
                    self.processed_list.append(formatted_newline)
                    continue

                if is_header(b):
                    formatted_header = html_formatter.to_html_header(b)
                    self.processed_list.append(formatted_header)
                else:
                    if is_url(b):
                        formatted_url = html_formatter.to_html_url(b)+"\n"
                        self.processed_list.append(formatted_url+html_formatter.to_html_new_line())
                        continue
                    # If it reaches this, it's a paragraph
                    formatted_paragraph = html_formatter.to_html_paragraph(b)
                    self.processed_list.append(formatted_paragraph)

        # Lastly we find the urls lying around the elements
        for idx, item in enumerate(self.processed_list):
            if is_url(self.processed_list[idx]):
                continue
            urls = find_urls(item)
            if len(urls) > 0:
                for u in urls:
                    self.processed_list[idx] = item.replace(u, html_formatter.to_html_url(u))

    def render_result(self):
        """
            Prints the converted content to the given output_filepath
        """
        if is_header(self.processed_list[0]):
            title = html_formatter.to_html_title(self.processed_list[0])
        else:
            title = ""
        result = html_formatter.HtmlDocument(title, self.processed_list)
        with open(self.output_path, "w") as f:
            f.write(result.__str__())

