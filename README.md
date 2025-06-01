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



##Highlighting updates in real-time:<br><br>
![demo1](https://github.com/user-attachments/assets/c3ac5f1b-9aa9-4a17-9f54-70f85f4f147c)
<br><br>
##Syntax Errors are highlighted in red:<br><br>
![demo2](https://github.com/user-attachments/assets/7853d2bc-cbdf-472e-849e-a87f2e80793d)




