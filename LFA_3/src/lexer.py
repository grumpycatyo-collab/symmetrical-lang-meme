import re


# Regular expressions for matching tokens
t_PLUS = r'\+'
t_MINUS = r'-'

# Function for handling image formats
def t_IMG_FORMAT(data,pos):
    match = re.match('(png|jpg|jpeg|gif|bmp|tiff|webp)',data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

def t_DIR_NAV_COMMANDS(data,pos):
    match = re.match('(cd|touch|pwd|cd..)',data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos
# Function for handling image paths
def t_IMAGE_PATH(data, pos):
    match = re.match(r'"(?:[a-zA-Z]:\\|/)?(?:[^"/\\]+[\\/])*[^"/\\]*\.(png|jpg|jpeg|gif|bmp|tiff|webp)"', data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

# Function for handling folder paths
def t_PATH(data, pos):
    match = re.match(r'"(?:[a-zA-Z]:\\|/)?(?:[^"/\\]+[\\/])+[^"/\\]*/?"', data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

# Function for handling commands
def t_COMMAND(data, pos):
    match = re.match(r'\b(imp|crop|sudo|dnf|pacman|apt|update)\b', data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

# Function for handling flags
def t_FLAG(data, pos):
    match = re.match(r'--\w+', data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

# Function for handling identifiers and keywords (modify for your language)
def t_IDENTIFIER(data, pos):
    match = re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

# Function for handling integers
def t_INTEGER(data, pos):
    match = re.match(r'\d+', data[pos:])
    if match:
        return int(match.group()), pos + len(match.group())
    return None, pos

# Ignore whitespace
def t_ignore(data, pos):
    while pos < len(data) and data[pos] in ' \t':
        pos += 1
    return pos

# Error handling (optional, can be improved)
def t_error(data, pos):
    print("Illegal character '%s'" % data[pos])
    return pos + 1

def t_ASSIGN(data, pos):
    match = re.match(r'\=', data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

# Function for handling semicolon ';'
def t_SEMICOLON(data, pos):
    match = re.match(r'\;', data[pos:])
    if match:
        return match.group(), pos + len(match.group())
    return None, pos

def tokenize(data):
    tokens = []
    pos = 0
    while pos < len(data):
        found_token = False
        for token_type in [t_PLUS, t_MINUS, t_ASSIGN, t_SEMICOLON, t_INTEGER, t_IMAGE_PATH, t_PATH, t_FLAG, t_COMMAND, t_DIR_NAV_COMMANDS, t_IMG_FORMAT, t_IDENTIFIER]:
            if callable(token_type):  
                token_value, new_pos = token_type(data, pos)
                if token_value is not None:
                    tokens.append((token_type.__name__[2:], token_value))
                    pos = new_pos
                    found_token = True
                    break
        if not found_token:
            # Handle exceptions for specific characters
            current_char = data[pos]
            if current_char in ['"', "'", ' ', '\t', '\n']:
                pos += 1
            else:
                unknown_token = data[pos]
                tokens.append(("UNKNOWN", unknown_token))
                pos += 1
    return tokens
