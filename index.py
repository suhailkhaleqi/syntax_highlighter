import re
import tkinter as tk
from tkinter import scrolledtext


# --------------------------
# Lexical Analyzer (Tokenizer)
# --------------------------
def tokenize(code):
    token_specs = [
        ('NUMBER', r'\d+(\.\d+)?'),  # Integers or floats
        ('OPERATOR', r'[+\-*/=<>!&|^%]'),  # Operators
        ('PAREN', r'[()]'),  # Parentheses
        ('BRACE', r'[{}]'),  # Braces
        ('STRING', r'"[^"]*"|\'[^\']*\''),  # Strings
        ('KEYWORD', r'\b(if|else|for|while|return|def)\b'),  # Keywords
        ('COMMENT', r'#.*'),  # Comments
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Variables/functions
        ('SKIP', r'\s+'),  # Whitespace (ignored)
        ('UNKNOWN', r'.')  # Fallback
    ]
    tokens = []
    for kind, pattern in token_specs:
        for match in re.finditer(pattern, code):
            if kind != 'SKIP':
                tokens.append((kind, match.group(), match.start()))
    return tokens


# --------------------------
# Syntax Analyzer (Top-Down Parser)
# --------------------------
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else None

    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        try:
            self.parse_expression()
            return True  # Valid syntax
        except Exception as e:
            print(f"Syntax Error: {e}")
            return False  # Invalid syntax

    def parse_expression(self):
        self.parse_term()
        while self.current_token and self.current_token[0] == 'OPERATOR':
            self.advance()
            self.parse_term()

    def parse_term(self):
        if self.current_token[0] in ('NUMBER', 'IDENTIFIER'):
            self.advance()
        elif self.current_token[0] == 'PAREN' and self.current_token[1] == '(':
            self.advance()
            self.parse_expression()
            if self.current_token[1] != ')':
                raise ValueError("Missing closing parenthesis")
            self.advance()
        else:
            raise ValueError("Unexpected token")


# --------------------------
# GUI with Real-Time Highlighting
# --------------------------
class SyntaxHighlighter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Grammar-Based Syntax Highlighter")
        self.text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=25)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.text.bind('<KeyRelease>', self.highlight)
        self.setup_tags()

    def setup_tags(self):
        colors = {
            'NUMBER': '#B5CEA8',  # Greenish
            'OPERATOR': '#FF5555',  # Red
            'PAREN': '#9CDCFE',  # Blue
            'BRACE': '#FFD700',  # Gold
            'STRING': '#CE9178',  # Orange
            'KEYWORD': '#569CD6',  # Dark blue
            'COMMENT': '#6A9955',  # Gray-green
            'IDENTIFIER': '#DCDCAA',  # Light yellow
            'ERROR': '#FF0000'  # Red (for syntax errors)
        }
        for tag, color in colors.items():
            self.text.tag_config(tag, foreground=color)

    def highlight(self, event):
        code = self.text.get("1.0", tk.END)
        tokens = tokenize(code)

        # Clear previous tags
        for tag in self.text.tag_names():
            self.text.tag_remove(tag, "1.0", tk.END)

        # Apply highlighting
        for kind, value, start_pos in tokens:
            start = f"1.0 + {start_pos} chars"
            end = f"1.0 + {start_pos + len(value)} chars"
            self.text.tag_add(kind, start, end)

        # Validate syntax
        parser = Parser(tokens)
        is_valid = parser.parse()
        if not is_valid:
            self.text.tag_add('ERROR', "1.0", tk.END)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SyntaxHighlighter()
    app.run()