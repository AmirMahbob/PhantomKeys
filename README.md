# PhantomKeys - Intelligent Keylogger 🔒

PhantomKeys is a smart and selective keylogger designed to monitor and log keyboard activities in specified applications. It provides multilingual support, including English and Persian, and ensures effective logging only when targeted programs are active.

---

## ✨ Features

- ⌚ **Selective Monitoring**: Logs keyboard activity exclusively for specified applications (e.g., Telegram, WhatsApp, Instagram).
- 📚 **Multilingual Support**: Detects the keyboard language (English or Persian) and translates inputs accordingly.
- 🔒 **Stealth Mode**: Operates discreetly without interfering with user activities.
- ⚖️ **Accurate Key Mapping**: Handles special keys and numeric inputs seamlessly.
- ⚡ **Real-Time Detection**: Activates logging dynamically when a target application is running.
- 🛠 **Robust Error Handling**: Manages unexpected inputs and program interruptions gracefully.

---

## ⚙️ Requirements

Ensure the following dependencies are installed:

- Python 3.7+
- Required libraries:
  - `psutil`
  - `pynput`
  - `pywin32`

Install dependencies using:

```bash
pip install psutil 
pip install pynput 
pip install pywin32
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/phantomkeys.git
   cd phantomkeys
   ```

2. Ensure dependencies are installed.

3. Run the application:
   ```bash
   python phantomkeys.py
   ```

---

## 🔧 Usage

1. Launch the script.
2. The program monitors the following applications by default:
   - Telegram
   - WhatsApp
   - Rubika
   - Instagram

3. Logs are saved to `keylogger.txt` in the same directory.

4. **Keyboard Language Detection:**
   - Automatically detects and logs the input language.
   - Persian keys are mapped accurately.

5. **Program-Specific Activation:**
   - Logging begins only when a target program is active.

---

## 🎨 Example Output

- **Input in Telegram (English):**
  ```
  Hello, how are you? [ENTER]
  ```
- **Input in Telegram (Persian):**
  ```
  سلام، حالت چطوره؟ [ENTER]
  ```

---

## 🗂 Project Structure

```
.
├── phantomkeys.py          # Main keylogger script
├── keylogger.txt           # Log file
└── README.md               # Documentation
```

---

## ⚠ Known Issues

- Requires administrator privileges on Windows to access keyboard events and processes.
- Ensure the targeted applications are listed correctly in `target_programs`.
- May not work correctly with virtual keyboards or certain input methods.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👍 Contributing

Contributions are welcome! Feel free to fork the repository, submit a pull request, or suggest new features.

---

