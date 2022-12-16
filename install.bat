@echo off

pip install -r requirements.txt
pyinstaller --onefile graph.py --icon icon.ico --noconsole

PAUSE