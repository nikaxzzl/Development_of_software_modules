cd ~/Development_of_software_modules/student-tools2
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate

python -m pip freeze > requirements.txt

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m app.main
# → Средний результат: 4.40
python -m pytest -v
# → 3 passed