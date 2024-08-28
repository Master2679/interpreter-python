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
                case _ if c.isdigit():
                    j = i
                    while j < len(file_contents) and file_contents[j].isnumeric():
                        j += 1
                    if j < len(file_contents) and file_contents[j] == '.':
                        j += 1
                        while j < len(file_contents) and file_contents[j].isnumeric():
                            j += 1
                    print(f"NUMBER {file_contents[i:j]} {file_contents[i:j]}")
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
