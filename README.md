🔐 Silent Keylogger with Timestamp Logging (Educational Use Only)
This is a stealth keylogger written in Python using the pynput library. It logs all keyboard input (including special keys) to a timestamped .txt file — completely silently, with no console messages or alerts.

⚠️ Warning — Use Responsibly
This software is provided strictly for educational and ethical purposes only.
Unauthorized use to monitor others without consent is illegal and unethical.
Always obtain explicit permission before running this script on any machine you do not personally own.

🧩 Features
✅ Logs all keypresses, including letters, numbers, symbols, and special keys
✅ Adds a timestamp to every key press
✅ Creates a new log file for every session (e.g., keylog_20250407_161042.txt)
✅ Operates in stealth mode – no window, messages, or alerts
✅ Automatically stops when Esc key is pressed
🔧 Requirements
Python 3.6 or higher
pynput module
Install pynput with:

pip install pynput
🚀 How to Use
Follow these steps to download, run, and stop the keylogger script:

✅ 1. Download or Clone the Repository
You have two options:

🔹 Option A: Download as ZIP (No Git Required)
Go to https://github.com/Ankur857/key

Click the green "Code" button and select "Download ZIP".

Extract the downloaded ZIP file.

Open a terminal and navigate into the extracted folder using:

cd path/to/extracted/keylogger-folder
Example (if extracted in Downloads): ```bash cd Downloads/keylogger-main

🔹 Option B: Clone with Git (Recommended) Open a terminal and run:

git clone https://github.com/Ankur857/key.git
cd keylogger
✅ 2. Make Sure Python is Installed To check if Python is installed, run:

python --version
or

python3 --version
If not installed, download it from: https://www.python.org/downloads

✅ Make sure to select “Add Python to PATH” during installation.
✅ 3. Install Required Packages The script uses the pynput library. To install it, run:

pip install pynput
If needed, try:

pip install --user pynput
✅ 4. Run the Script In the terminal, make sure you're inside the keylogger folder, then run:

python keylogger.py
Or, if using python3:

python3 keylogger.py

The keylogger will now start running in the background and begin logging keystrokes.

🛑 5. Stop the Keylogger To stop it, simply press the Esc key on your keyboard.

📁 Output
Each session creates a new log file in the current directory:

keylog_YYYYMMDD_HHMMSS.txt
Example contents:

[16:10:42] a
[16:10:43] b
[16:10:44] [Key.space]
[16:10:45] [Key.enter]
