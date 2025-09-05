For development and testing purposes use the test database in the repository: json_files/input.json

use the following commands for this:
python manage.py loaddata json_files/input.json
python manage.py makemigrations  
python manage.py migrate
