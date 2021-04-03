# write your code here

def print_help():
    print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
    print('Special commands: !help !done')


def plain(text):
    global huge_texts
    huge_texts.append(text)
    print_huge_texts()


def bold(text):
    global huge_texts
    huge_texts.append(f'**{text}**')
    print_huge_texts()


def italic(text):
    global huge_texts
    huge_texts.append(f'*{text}*')
    print_huge_texts()


def inline_code(text):
    global huge_texts
    huge_texts.append(f'`{text}`')
    print_huge_texts()


def link(label, url):
    global huge_texts
    huge_texts.append(f'[{label}]({url})')
    print_huge_texts()


def header(level, text):
    global huge_texts
    hashes = '#' * level
    huge_texts.append(f'{hashes} {text}\n')
    print_huge_texts()


def new_line():
    global huge_texts
    huge_texts.append('\n')
    print_huge_texts()


def ordered_list(rows):
    for x in range(1, rows + 1):
        input_text = input(f'- Row #{x}:')
        huge_texts.append(f'{x}. {input_text}\n')
    print_huge_texts()


def unordered_list(rows):
    for x in range(1, rows + 1):
        input_text = input(f'- Row #{x}:')
        huge_texts.append(f'* {input_text}\n')
    print_huge_texts()


def print_huge_texts():
    global huge_texts
    for line in huge_texts:
        print(line, end='')
    print('')


def done():
    res = open('output.md', 'w', encoding='utf-8')
    res.writelines(huge_texts)
    res.close()


huge_texts = []

formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'unordered-list', 'ordered-list', 'new-line']

while True:
    input_string = input('- Choose a formatter:')
    if input_string == '!done':
        done()
        break
    elif input_string == '!help':
        print_help()
    elif input_string not in formatters:
        print('unknown formatting type or command')
    elif input_string == 'header':
        level = int(input('- Level:'))
        text = input('- Text:')
        header(level, text)
    elif input_string == 'link':
        label = input('- Label:')
        url = input('- URL:')
        link(label, url)
    elif input_string == 'new-line':
        new_line()
    elif input_string == 'ordered-list':
        while True:
            rows = int(input('- Number of rows:'))
            if rows < 1:
                print('The number of rows should be greater than zero')
            else:
                ordered_list(rows)
                break
    elif input_string == 'unordered-list':
        while True:
            rows = int(input('- Number of rows:'))
            if rows < 1:
                print('The number of rows should be greater than zero')
            else:
                unordered_list(rows)
                break
    else:
        text = input('- Text:')
        if input_string == 'plain':
            plain(text)
        elif input_string == 'bold':
            bold(text)
        elif input_string == 'italic':
            italic(text)
        elif input_string == 'inline-code':
            inline_code(text)
