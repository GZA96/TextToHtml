import Parser
import html_formatter
import unittest


class TestTextToHtml(unittest.TestCase):
    def test_is_list(self):
        ex_list = "         - Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        ex_list2 = "            -                   Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        ex_list3 = "                               Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        self.assertTrue(Parser.is_list(ex_list))
        self.assertTrue(Parser.is_list(ex_list2))
        self.assertFalse(Parser.is_list(ex_list3))

    def test_is_header(self):
        h1 = "Lorem ipsum dolor sit amet"
        h2 = "Lorem ipsum dolor sit amet:"
        h3 = "Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        self.assertTrue(Parser.is_header(h1))
        self.assertFalse(Parser.is_header(h2))
        self.assertFalse(Parser.is_header(h3))

    def test_is_url(self):
        u1 = "htttp://google.com"
        u2 = "http://google.com"
        u3 = "http://www.google.com"
        u4 = "https://docs.python.org/2/library/re.html"
        u5 = "https:/@/docs.python.org/2/library/re.html"
        self.assertFalse(Parser.is_url(u1))
        self.assertTrue(Parser.is_url(u2))
        self.assertTrue(Parser.is_url(u3))
        self.assertTrue(Parser.is_url(u4))
        self.assertFalse(Parser.is_url(u5))

    def test_find_urls(self):
        ex_text1 = "Praesent aliquet htttp://google.com gravida ex. Phasellus posuere massa nibh, http://www.google.com eget finibus lorem imperdiet a. Suspendisse viverra maximus tortor. Mauris facilisis vestibulum tellus at aliquet. Nunc eu odio nec velit vestibulum iaculis sed ut libero. Vestibulum efficitur elit a nibh accumsan, non pellentesque dui hendrerit. Pellentesque in eros vitae augue finibus fringilla. Aliquam ornare ante non ex finibus, ac tincidunt libero vestibulum. Sed tellus turpis, malesuada vitae ultrices quis, ultricies eu risus. Etiam in magna metus. Sed porttitor sagittis ligula nec fermentum. Donec tortor velit, porttitor et fermentum eu, euismod sed sapien. Ut et dolor ante."
        ex_text2 = "Praesent aliquet gravida ex. https://www.youtube.com/watch?v=hHW1oY26kxQ Phasellus posuere massa nibh, http://www.google.com eget finibus lorem imperdiet a. Suspendisse viverra maximus tortor. Mauris facilisis vestibulum tellus at aliquet. Nunc eu odio nec velit vestibulum iaculis sed ut libero. Vestibulum efficitur elit a nibh accumsan, non pellentesque dui hendrerit. Pellentesque in eros vitae augue finibus fringilla. Aliquam ornare ante non ex finibus, ac tincidunt libero vestibulum. Sed tellus turpis, malesuada vitae ultrices quis, ultricies eu risus. Etiam in magna metus. Sed porttitor sagittis ligula nec fermentum. Donec tortor velit, porttitor et fermentum eu, euismod sed sapien. Ut et dolor ante."
        ex_text3 = "Praesent  aliquet gravida ex. Phasellus posuere massa nibh, http://www.google eget finibus lorem imperdiet a. Suspendisse viverra maximus tortor. Mauris facilisis vestibulum tellus at aliquet. Nunc eu odio nec velit vestibulum iaculis sed ut libero. Vestibulum efficitur elit a nibh accumsan, non pellentesque dui hendrerit. Pellentesque in eros vitae augue finibus fringilla. Aliquam ornare ante non ex finibus, ac tincidunt libero vestibulum. Sed tellus turpis, malesuada vitae ultrices quis, ultricies eu risus. Etiam in magna metus. Sed porttitor sagittis ligula nec fermentum. Donec tortor velit, porttitor et fermentum eu, euismod sed sapien. Ut et dolor ante."

        self.assertListEqual(Parser.find_urls(ex_text1), ['http://www.google.com'])
        self.assertListEqual(Parser.find_urls(ex_text2),
                             ['https://www.youtube.com/watch?v=hHW1oY26kxQ', 'http://www.google.com'])
        self.assertListEqual(Parser.find_urls(ex_text3), [])

    def test_process_information(self):
        ex_text = """This is a header.\n-               List element 1.\n- List element 2.\n"""
        ex_result = ["<h1>This is a header.</h1>\n",
                     "<ul>\n\t<li>\n\t\t-               List element 1.\n\t</li>\n"
                     "\t<li>\n\t\t- List element 2.\n\t</li>\n</ul>\n",
                     "<br />\n"]
        p = Parser.Parser("", "")
        p.process_information(ex_text)
        self.assertListEqual(p.processed_list, ex_result)

    def test_to_html_list(self):
        ex_list = ["- First element", "- Second element", "- Third element", "- Fourth element"]
        result = "<ul>\n\t<li>\n\t\t- First element\n\t</li>\n" \
                 "\t<li>\n\t\t- Second element\n\t</li>\n" \
                 "\t<li>\n\t\t- Third element\n\t</li>\n" \
                 "\t<li>\n\t\t- Fourth element\n\t</li>\n</ul>\n"
        self.assertEqual(html_formatter.to_html_list(ex_list), result)

    def test_to_html_paragraph(self):
        ex_par = "This is an example paragraph for a testing function, this is an example paragraph for a testing" \
             " function, this is an example paragraph for a testing function"
        result = "<p>\nThis is an example paragraph for a testing function, this is an example paragraph for a testing" \
                 " function, this is an example paragraph for a testing function\n</p>\n"
        self.assertEqual(html_formatter.to_html_paragraph(ex_par), result)

    def test_to_html_header(self):
        ex_head = "This is an example header for testing purposes"
        result = "<h1>This is an example header for testing purposes</h1>\n"
        self.assertEqual(html_formatter.to_html_header(ex_head), result)

    def test_to_html_url(self):
        ex_url = "http://www.google.com"
        result = "<a href=\"http://www.google.com\">http://www.google.com</a>"
        self.assertEqual(html_formatter.to_html_url(ex_url), result)


if __name__ == '__main__':
    unittest.main()
