import re


def minify(string):
    string = string.translate({ord('\t'): None})
    string = string.translate({ord('\n'): None})
    string = string.replace('  ', '')
    string = string.replace('> <', '><')
    return string


def beautify(string):
    string = minify(string)
    string = re.sub("<", "\n<", string)
    string = re.sub(">", ">\n", string)
    Lines = string.split("\n")
    string_output = ""

    def between(i, j, text):

        return re.findall(re.escape(i) + "(.*?)" + re.escape(j), text)

    o_tag = []
    c_tag = []
    count = -1
    f_close = False
    f_data = True
    for line in Lines:
        f_data = True
        f_close = False
        size = len(between('<', '>', line))

        if (len(line) == 0):
            continue
        if (size != 0):
            for tag in between('<', '>', line):
                f_data = False
                if ("/" in tag):
                    c_tag.append(tag)
                    f_close = True
                else:
                    o_tag.append(tag)
                    count += 1
        if (f_data):
            count += 1
        string_output = string_output + "    " * count + line + "\n"
        if (f_close or f_data):
            count = count - 1
    return string_output
