pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput