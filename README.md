# Optimized Port Scanner

A multithreaded Python-based TCP port scanner that detects open ports on single or multiple IP addresses.

## Features

- Scan single or multiple IPs
- Custom port range support
- Default scan range: 1-1000
- Uses socket timeout for faster scanning
- Multithreaded for performance
- Color-coded output
- Displays message if no open ports found

## Usage

Scan default ports:
python3 scanner.py 192.168.1.1

Scan custom range:
python3 scanner.py 192.168.1.1 -p 20-200

Scan multiple targets:
python3 scanner.py 192.168.1.1,192.168.1.10 -p 1-500

## Technologies Used

- Python
- Socket Programming
- Threading
- Colorama

