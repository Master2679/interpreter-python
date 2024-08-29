import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # Uncomment this block to pass the first stage
    if file_contents:
        error = False
        i = 0
        line = 1
        while i < len(file_contents):
            c = file_contents[i]
            match c:
                case '(': print("LEFT_PAREN ( null")
                case ')': print("RIGHT_PAREN ) null")
                case '{': print("LEFT_BRACE { null")
                case '}': print("RIGHT_BRACE } null")
                case ',': print("COMMA , null")
                case '.': print("DOT . null")
                case '-': print("MINUS - null")
                case '+': print("PLUS + null")
                case ';': print("SEMICOLON ; null")
                case '*': print("STAR * null")
                case '!':
                    if i + 1 < len(file_contents) and file_contents[i+1] == '=':
                        print("BANG_EQUAL != null")
                        i += 1
                    else:
                        print("BANG ! null")
                case '=':
                    if i + 1 < len(file_contents) and file_contents[i+1] == '=':
                        print("EQUAL_EQUAL == null")
                        i += 1
                    else:
                        print("EQUAL = null")
                case '<':
                    if i + 1 < len(file_contents) and file_contents[i+1] == '=':
                        print("LESS_EQUAL <= null")
                        i += 1
                    else:
                        print("LESS < null")
                case '>':
                    if i + 1 < len(file_contents) and file_contents[i+1] == '=':
                        print("GREATER_EQUAL >= null")
                        i += 1
                    else:
                        print("GREATER > null")
                case '/':
                    if i + 1 < len(file_contents) and file_contents[i+1] == '/':
                        i+=1
                        while i < len(file_contents) and file_contents[i] != '\n':
                            i+=1
                        line += 1
                    else:
                        print("SLASH / null")
                case ' ' | '\t' | '\r':
                    pass
                case '\n':
                    line += 1
                case '"':
                    j = i
                    j += 1
                    while j < len(file_contents) and file_contents[j] != '"':
                        if file_contents[j] == '\n':
                            line += 1
                        j += 1
                    if j == len(file_contents):
                        print(f"[line {line}] Error: Unterminated string.", file=sys.stderr)
                        error = True
                    else:
                        print(f"STRING {file_contents[i:j+1]} {file_contents[i+1:j]}")
                    i = j
                # add cases for and, class, else, false, for, fun, if, nil, or, print, return, super, this, true, var, while.
                case 'a':
                    if i + 2 < len(file_contents) and file_contents[i:i+3] == 'and':
                        print("AND and null")
                        i += 2
                    else:
                        pass
                case 'c':
                    if i + 4 < len(file_contents) and file_contents[i:i+5] == 'class':
                        print("CLASS class null")
                        i += 4
                    else:
                        pass
                case 'e':
                    if i + 3 < len(file_contents) and file_contents[i:i+4] == 'else':
                        print("ELSE else null")
                        i += 3
                    else:
                        pass
                case 'f':
                    if i + 4 < len(file_contents) and file_contents[i:i+5] == 'false':
                        print("FALSE false null")
                        i += 4
                    elif i + 2 < len(file_contents) and file_contents[i:i+3] == 'for':
                        print("FOR for null")
                        i += 2
                    elif i + 2 < len(file_contents) and file_contents[i:i+3] == 'fun':
                        print("FUN fun null")
                        i += 2
                    else:
                        pass
                case 'i':
                    if i + 1 < len(file_contents) and file_contents[i:i+2] == 'if':
                        print("IF if null")
                        i += 1
                    else:
                        pass
                case 'n':
                    if i + 2 < len(file_contents) and file_contents[i:i+3] == 'nil':
                        print("NIL nil null")
                        i += 2
                    else:
                        pass
                case 'o':
                    if i + 1 < len(file_contents) and file_contents[i:i+2] == 'or':
                        print("OR or null")
                        i += 1
                    else:
                        pass
                case 'p':
                    if i + 4 < len(file_contents) and file_contents[i:i+5] == 'print':
                        print("PRINT print null")
                        i += 4
                    else:
                        pass
                case 'r':
                    if i + 5 < len(file_contents) and file_contents[i:i+6] == 'return':
                        print("RETURN return null")
                        i += 5
                    else:
                        pass
                case 's':
                    if i + 4 < len(file_contents) and file_contents[i:i+5] == 'super':
                        print("SUPER super null")
                        i += 4
                    elif i + 3 < len(file_contents) and file_contents[i:i+4] == 'self':
                        print("SELF self null")
                        i += 3
                    else:
                        pass
                case 't':
                    if i + 3 < len(file_contents) and file_contents[i:i+4] == 'this':
                        print("THIS this null")
                        i += 3
                    elif i + 3 < len(file_contents) and file_contents[i:i+4] == 'true':
                        print("TRUE true null")
                        i += 3
                    else:
                        pass
                case 'v':
                    if i + 2 < len(file_contents) and file_contents[i:i+3] == 'var':
                        print("VAR var null")
                        i += 2
                    else:
                        pass
                case 'w':
                    if i + 4 < len(file_contents) and file_contents[i:i+5] == 'while':
                        print("WHILE while null")
                        i += 4
                    else:
                        pass
                case _ if c.isdigit():
                    decimal = False
                    j = i
                    while j < len(file_contents) and file_contents[j].isnumeric():
                        j += 1
                    if j < len(file_contents) and file_contents[j] == '.':
                        j += 1
                        while j < len(file_contents) and file_contents[j].isnumeric():
                            decimal = True
                            j += 1
                    if decimal:
                        print(f"NUMBER {file_contents[i:j]} {float(file_contents[i:j])}")
                    else:
                        print(f"NUMBER {file_contents[i:j]} {file_contents[i:j]}.0")
                    i = j - 1
                case '_':
                    j = i
                    while j < len(file_contents) and (file_contents[j].isalnum() or file_contents[j] == '_'):
                        j += 1
                    print(f"IDENTIFIER {file_contents[i:j]} null")
                    i = j - 1
                case _ if c.isalpha():
                    j = i
                    while j < len(file_contents) and (file_contents[j].isalnum() or file_contents[j] == '_'):
                        j += 1
                    print(f"IDENTIFIER {file_contents[i:j]} null")
                    i = j - 1
                case _:
                    print(f"[line {line}] Error: Unexpected character: {c}", file=sys.stderr)
                    error = True
            i += 1

        print("EOF  null")
        if(error):
            exit(65)
    else:
        print("EOF  null") # Placeholder, remove this line when implementing the scanner


if __name__ == "__main__":
    main()
