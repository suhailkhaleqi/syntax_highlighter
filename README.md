# Real-Time Grammar-Based Syntax Highlighter with GUI


A real-time syntax highlighter that performs lexical and syntax analysis using a formal grammar, implemented with a Tkinter GUI. Highlights 8+ token types and validates syntax against a context-free grammar (CFG).

---

## 📌 Features
- **Lexical Analysis**: Tokenizes code into 8+ types (keywords, strings, numbers, etc.).
- **Syntax Analysis**: Top-down parser for arithmetic/logical expressions.
- **Real-Time Highlighting**: Instantly colorizes code in the GUI.
- **Error Detection**: Underlines syntax errors (e.g., missing parentheses).
- **Grammar-Compliant**: Follows a defined CFG for validation.

### Supported Token Types
| Token        | Example      | Color       |
|--------------|--------------|-------------|
| Keywords     | `if`, `else` | `#569CD6`   |
| Numbers      | `42`, `3.14` | `#B5CEA8`   |
| Strings      | `"Hello"`    | `#CE9178`   |
| Operators    | `+`, `==`    | `#FF5555`   |
| Parentheses  | `()`, `{}`   | `#9CDCFE`   |

---

## 🚀 Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/syntax-highlighter.git
   cd syntax-highlighter
