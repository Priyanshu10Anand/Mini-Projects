# 🔐 SecurePass - Ultimate Password Generator

Welcome to **SecurePass**, your all-in-one solution for generating strong and secure passwords! This project includes both a **modern web interface** and a **command-line tool**, designed for quick, customizable, and safe password generation.

---

## 🌐 Live HTML Version

A beautifully styled password generator built using HTML, CSS, and JavaScript.  
🔹 Supports numeric, alphabetic, and mixed-character passwords  
🔹 Fully client-side, **no data ever leaves your browser**  
🔹 Responsive design with animations and floating icons

> 📁 File: `password-generator/password_generator.html`

### ✨ Features
- Choose password type: Numbers, Letters, or Mixed
- Select length: 4 to 128 characters
- Instant generation and copy-to-clipboard support
- Secure and elegant UI

---

## 💻 CLI Version (Python)

A terminal-based password generator for users who prefer the command line.

> 📁 File: `password-generator/password_generator.py`

### 🔧 How It Works

1. Greets the user and prompts for a password type:
    - `1`: Only numbers  
    - `2`: Only letters  
    - `3`: Letters + numbers
2. Accepts password length from 4 to 128 characters
3. Generates a random password accordingly
4. Allows users to regenerate as many times as they like

### ▶️ Run It

```bash
python password_generator.py

