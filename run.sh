rm stp build dist -rf
python -m venv stp
source stp/bin/activate
pip install -r requirements.txt
pip install pip --upgrade
pyinstaller --onefile graph.py --icon resource/icon.ico --noconsole
