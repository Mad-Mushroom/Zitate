import re

file_in = "zitate.txt"
file_out_html = "zitate.html"
file_out_raw = "zitate_raw.txt"

def generate_html(inp, out):
    try:
        new = []
        with open(inp, 'r') as file:
            for line in file:
                newline = re.sub(r'=(.*?)=', r'<h4>\1</h4>', line)
                newline = re.sub(r'"(.*?)"', r'<q>\1</q><br>', newline)
                new.append(newline)
        with open(out, 'w') as file:
            file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Zitate</title>\n</head>\n<body>\n")
            file.writelines(new)
            file.write("</body>\n</html>")
    except FileNotFoundError:
        print(f"The file {inp} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_raw(inp, out):
    try:
        new = []
        with open(inp, 'r') as file:
            for line in file:
                newline = line.replace('"', '')
                if newline[0] != '=':
                    new.append(newline)
        with open(out, 'w') as file:
            file.writelines(new)
    except FileNotFoundError:
        print(f"The file {inp} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

generate_html(file_in, file_out_html)
generate_raw(file_in, file_out_raw)