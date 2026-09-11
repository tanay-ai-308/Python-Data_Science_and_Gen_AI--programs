# Marvellous Directory Automation

A Python automation script that periodically scans a directory, logs file information, and automatically deletes empty files.

## 🚀 Features :----------------------------------------------------------------

- Scans directories recursively.
- Finds and deletes **empty (0-byte) files**.
- Creates a log file containing file names and sizes.
- Runs automatically every **10 seconds**.
- Supports command-line arguments.

## 🛠️ Requirements :------------------------------------------------------------

- Python 3
- `schedule` module

Install the module:

```bash
pip install schedule
```

## ▶️ Usage :------------------------------------------------------------

Run the script with the directory path:

```bash
python DirectoryScanner.py "D:\Projects\Test"
```

Use `--h` for help:

```bash
python DirectoryScanner.py --h
```

Use `--u` for usage information:

```bash
python DirectoryScanner.py --u
```

## 📋 How It Works :------------------------------------------------------------

```text
Directory Path
      ↓
Check Directory
      ↓
Scan Files
      ↓
Check File Size
      ↓
0 Bytes → Delete
      ↓
Create Log
      ↓
Wait 10 Seconds
      ↓
Scan Again
```

The script uses `os.walk()` to scan subdirectories and `schedule` to repeat the operation every 10 seconds.

> ⚠️ **Warning:** Empty files are permanently deleted. Test the script on a sample directory first.

## 👨‍💻 Author :------------------------------------------------------------

**Tanay Suresh Dherange**