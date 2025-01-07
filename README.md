# FILE-INTEGRITY-CHECKER

**COMPANY**: CODTECH IT SOLUTIONS PVT. LTD  
**NAME**: DEVANG AVINASH KENI  
**INTERN ID**: CT08FRA  
**DOMAIN**: Cyber Security & Ethical Hacking  
**BATCH DURATION**: December 25th, 2024 to January 25th, 2025  
**MENTOR NAME**: NEELA SANTOSH  

---

## DESCRIPTION

Welcome to the **File Integrity Checker** repository! This is my first cybersecurity tool, created as part of my internship at CODTECH IT SOLUTIONS PVT. LTD. The goal of this project is to help ensure the integrity of your important files by monitoring changes using hash values. Let me walk you through what this tool does, how to set it up, and how you can use it effectively.

### **What Does This Tool Do?**

Imagine you have critical files that must remain unchanged, but you’re worried about tampering or corruption. This tool calculates and monitors hash values of files to detect if any changes have occurred. It uses the reliable `hashlib` library in Python to generate SHA-256 hashes, which are unique identifiers for your files. If a file is modified, its hash changes—and the tool immediately flags it, letting you know something’s up.

### **Key Features**
- **File Monitoring:** Check the integrity of a file by comparing its hash before and after modifications.
- **Automation:** I've created a `.bat` file (Windows batch file) so you can run this tool just like an app, without needing to manually type commands in the terminal.
- **Logs:** The tool logs all results into a text file, so you can keep a record of file integrity checks.
- **Ease of Use:** Simple input prompts to make it beginner-friendly, even for those who aren't tech-savvy.

---

## SETUP INSTRUCTIONS

### 1. Install Python
- Download and install Python from [python.org](https://www.python.org/). Ensure you check the option to add Python to your system PATH during installation.

### 2. Install Required Libraries
- Open your terminal and run the following command to install the required library:
  ```bash
  pip install hashlib
  ```
  *(Note: `hashlib` is part of Python’s standard library, so you don’t need to install it separately.)*

### 3. Clone the Repository
- Clone this repository to your system using:
  ```bash
  git clone https://github.com/yourusername/file-integrity-checker.git
  ```

### 4. Windows Batch File Setup
- For convenience, I’ve created a `.bat` file that allows you to run the tool like a standalone app.
- Just double-click the `run_checker.bat` file in the repository to launch the tool. This eliminates the need to manually type `python file_integrity_checker.py` in the terminal. *(Batch file is designed specifically for this purpose.)*

---

## HOW TO USE

### 1. Run the Tool
- If you're using the `.bat` file, simply double-click `run_checker.bat` to start the tool.
- If you prefer the manual way, open your terminal, navigate to the project folder, and run:
  ```bash
  python file_integrity_checker.py
  ```

### 2. Provide File Path
- When prompted, enter the full path of the file you want to monitor. For example:
  ```plaintext
  C:\Users\Devang\Documents\example.txt
  ```

### 3. Modify the File
- Make changes to the file (e.g., edit it and save).

### 4. Check for Integrity
- Press Enter when prompted to check if the file has been modified.

### 5. Logs
- All results are saved in a `logs/integrity_check_log.txt` file for your reference.

---

## PRECAUTIONS

- **Use Trusted Files Only:** Ensure the files you’re monitoring are not corrupted to begin with.
- **Administrator Permissions:** If you're running the tool on system-protected files, you may need admin permissions.
- **Batch File Compatibility:** The `.bat` file works on Windows only. If you're using another OS, run the Python script directly.

---

## OUTPUT

![output1](https://github.com/user-attachments/assets/a115c343-ed6e-46c4-80ae-eeb384fb4aa9)

