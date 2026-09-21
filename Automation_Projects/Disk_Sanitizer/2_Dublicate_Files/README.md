# Directory Sanitizer

**Directory Sanitizer** is a Python automation script that scans a given directory, identifies duplicate files using **MD5 checksum**, removes duplicate copies, and generates a detailed log of the operation.

The script can also be configured to run periodically using a specified time interval.

## Below Instructions are Given for the Email Activity ------------- Important ------------------

## Features

- Scans files recursively inside a directory.
- Calculates **MD5 checksum** for each file.
- Identifies duplicate files based on checksum.
- Keeps the first copy and removes the duplicate copies.
- Records the complete path of deleted files.
- Records:
  - Directory scanned
  - Starting time
  - Completion time
  - Total files scanned
  - Total duplicate files found
  - Total duplicate files deleted
  - Deleted file paths
  - Errors encountered
- Supports command-line arguments.
- Supports periodic execution using the `schedule` module.
- Supports optional log-folder and email functionality.

## Requirements

- Python 3.x
- `schedule` module

Install the required module:

```bash
pip install schedule
```

## Usage

Basic command:

```bash
python DirectorySanitizer.py <TimeInterval> <DirectoryName>
```

Example:

```bash
python DirectorySanitizer.py 10 DemoFolder
```

This runs the duplicate-file removal operation every **10 seconds**.

### Optional Email

```bash
python DirectorySanitizer.py 10 DemoFolder receiver@gmail.com
```

### Optional Log Folder

```bash
python DirectorySanitizer.py 10 DemoFolder receiver@gmail.com DemoFolder
```

## Command-Line Arguments

| Argument       |           Description                   |
|----------------|-----------------------------------------
| `TimeInterval`    Time interval between two scans in Seconds
| `DirectoryName`   Directory to scan              
| `Email`           Optional email address for sending logs
| `LogFolder`       Optional folder for storing log files 

## Help

To display information about the project:

```bash
python DirectorySanitizer.py --h
```

To display usage examples:

```bash
python DirectorySanitizer.py --u
```

## How It Works

```text
Directory
    ↓
Scan Files
    ↓
Calculate MD5 Checksum
    ↓
Group Files With Same Checksum
    ↓
Identify Duplicate Files
    ↓
Keep First File
    ↓
Delete Duplicate Copies
    ↓
Generate Log
    ↓
Store / Send Log
```

## Example

If a directory contains:

```text
DemoFolder/
├── file1.txt
├── file1_copy.txt
├── file2.txt
└── file2_copy.txt
```

If `file1.txt` and `file1_copy.txt` have the same checksum, one copy is retained and the duplicate is removed.

The log records the deleted file's complete path.

## Important Note

Files deleted by this program are removed using Python's `os.remove()` and **are not moved to the Recycle Bin**.

Use the program carefully, especially when testing it on important directories.

## Project Purpose

This project demonstrates practical Python concepts including:

- File and directory handling
- `os.walk()`
- File hashing with `hashlib`
- Command-line arguments
- Exception handling
- Performance measurement
- Automation and scheduling
- Log generation
- File deletion

## For Email Sending ------------------------ Important -------------------------------------------------

 (*) YOU HAVE TO DO SOME CHANGES IN SCRIPT AS FOLLOWS :- 
    - 1. Assign your email to sender Variable.
            sender variable is present in the function SendMail it is None Write Now Assign your mail in Double Quotes to it.
    - 2. Assign your app password from the Google account to the Variable named AppPassword
            AppPassword variable is present in the function SendMail it is None Write Now Assign your mail in Double Quotes to it.

## Author

**Tanay Dherange**

---
**Directory Sanitizer — Automate. Detect. Clean. Log.**