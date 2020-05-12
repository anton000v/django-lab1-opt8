# django-lab1-opt8
Django| The first laboratory. Questions and answers. 8-th option
# Task:
Реалізувати веб-сайт з наступними сторінками: адміністративна сторінка для додавання / видалення / коригування питань на сайті; призначена для користувача сторінка для відображення випадкових питань і можливості введення відповідей; адміністративна сторінка для виведення статистики по числу правильних / неправильних відповідей на кожне питання. 

# Start Instruction in russian:
После копирования проекта, создай python виртуальное окружение (python -m venv venv). Активируй его, и в корне проекта выполни команду pip install -r requirements.txt (Она установит все необходимые для проекта зависимости). Так же, по заданию нужно было делать все на mysql, создай у себя локально бд с названием "django_lab1_var8" , логином "root" и паролем "root". (Если что, можно назвать как угодно и потом заменить в файле Lab1_engine/Lab1_engine/settings.py под свои данные). Дальнейшие действия будут проихводиться в папке Lab1_engine/Lab1. Выполни команду " python manage.py makemigrations Lab1 " и после нее " python manage.py migrate ". После этого выполни команду " python manage.py createsuperuser " . Вводи какие хочешь данные. Они тебе будут нужны для перехода на администрирование сайта по URL адресу "localhost:8000/admin.py". Дальше выполни команду " python manage.py runserver ". Если все прошло без ошибок, переходи по ссылке, которая будет в командной строке и щелкай лабу.

# [ Если появились проблемы с установкой и подключением данной лабораторной работы к mysql]
Перейди в Lab1_engine/Lab1_engine/settings.
Найти вот такие строчки: #' DATABASES = { #' 'default': { #' 'ENGINE': 'django.db.backends.sqlite3', #' 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #' } #' } DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'django_lab1_var8', 'USER': 'root', 'PASSWORD': 'root', } }
Выдели их и вставь вместо них это: DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), } } #' DATABASES = { #' 'default': { #' 'ENGINE': 'django.db.backends.mysql', #' 'NAME': 'django_lab1_var8', #' 'USER': 'root', #' 'PASSWORD': 'root', #' } #' }
Выполни команду из инструкции по установке " manage.py makemigrations Lab1Files " и следуй дальнейшим инструкциям из установки. Это создаст Sqlite базу данных. Это, конечно, не подходит по заданию лабораторной работы, но может тебе повезет и этого не обнаружат :)
P.S. Так же, в папке Screens лежат скрины для отчета
