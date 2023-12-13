
# Build the project
echo "Building the project..."
pip install -r requirements.txt


# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear