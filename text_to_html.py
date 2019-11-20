import sys
import Parser
import os

"""
    Parse a text file into an html file
    
    Usage:
        python text_to_html.py <input_filepath> <output_filepath>
"""


def main():
    if len(sys.argv) == 3:
        if sys.argv[2][sys.argv[2].rfind("."):] != '.html':
            raise TypeError("Error! Second argument isn't an html file")

        if os.path.exists(sys.argv[1]):
            if os.path.exists(sys.argv[2]):
                opt = ""
                while opt.upper() != 'Y' and opt.upper() != 'N':
                    opt = raw_input("Output file already exists, do you want to overwrite it? (Y/N):    ")
                if opt.upper() == 'N':
                    exit()

            # Read txt file, process it and render results on: argv[2]
            p = Parser.Parser(sys.argv[1], sys.argv[2])
            whole_txt = p.read_file()
            p.process_information(whole_txt)
            p.render_result()
        else:
            raise IOError("Input file doesn't exist!")
    else:
        raise TypeError("Incorrect number of arguments!! , expected 3 got {0}".format(len(sys.argv)))


if __name__ == '__main__':
    try:
        main()
        print("Conversion was successful! - "+sys.argv[2]+" created !!")
    except TypeError as e:
        print(e)
    except IOError as e:
        print(e)
    except NameError as e:
        print(e)
    except Exception as e:
        print(e)
        raise





