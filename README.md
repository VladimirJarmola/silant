<h1>Дипломный проект: реальный кейс от компании «Силант»</h1>

<h2>Запуск проекта локально</h2>

<p>Создайте виртуальное окружение для проекта:</p>
<pre>
<blockquote>mkdir [folder_name]</blockquote><blockquote>cd [folder_name]</blockquote><blockquote>python -m venv venv</blockquote><blockquote>venv/scripts/activate</blockquote></pre>

<p>Склонируйте репозиторий на локальную машину:</p>

<pre><blockquote>git clone https://github.com/VladimirJarmola/silant.git</blockquote></pre>

<p>Установите зависимости:</p>

<pre><blockquote>cd silant</blockquote><blockquote>pip install -r requirements.txt</blockquote></pre>

<h3>База данных</h3>
<p>По умолчанию проект работает с базой данных PostgreSQl. Для создания базы данных воспользуйтесь программой pgAdmin4, SQL Shell или введите в консоль следующие команды: </p>
 
<pre><blockquote>psql -U postgres

"C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres (для Windows, если psql не добавлена в переменную PATH)</blockquote></pre>

<p>И введите пароль для входа в бд</p>
<p>Далее необходимо создать юзера silant:</p>
 
<pre><blockquote>CREATE ROLE silant WITH LOGIN SUPERUSER CREATEDB CREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 PASSWORD 'silant';</blockquote></pre>

<p>И базу данных silant:</p>
 
<pre><blockquote>CREATE DATABASE silant WITH OWNER = silant ENCODING = 'UTF8' LOCALE_PROVIDER = 'libc' CONNECTION LIMIT = -1 IS_TEMPLATE = False;</blockquote></pre>

<p>Создадим миграции:</p>
 
<pre><blockquote>python manage.py makemigrations</blockquote></pre>

<p>И применим их:</p>
 
<pre><blockquote>python manage.py migrate</blockquote></pre>

<p>Подгружаем фикстуры:</p>
 
<pre><blockquote>python manage.py loaddata fixtures/db.json</blockquote></pre>

<h3>Запускаем сервер:</h3>
<pre><blockquote>python manage.py runserver</blockquote></pre>