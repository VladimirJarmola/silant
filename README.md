<h1>Дипломный проект: реальный кейс от компании «Силант»</h1>

<h2>Запуск проекта локально</h2>

<p>Создайте виртуальное окружение для проекта:</p>
<pre>
<blockquote>mkdir [folder_name]</blockquote><blockquote>cd [folder_name]</blockquote><blockquote>python -m venv venv</blockquote><blockquote>venv/scripts/activate</blockquote></pre>

<p>Склонируйте репозиторий на локальную машину:</p>

<pre><blockquote>git clone https://github.com/VladimirJarmola/silant.git</blockquote></pre>

<p>Установите зависимости:</p>

<pre><blockquote>cd silant</blockquote><blockquote>pip install -r requirements.txt</blockquote></pre>

<p>Apply the migrations:</p>
 
<pre><blockquote>python manage.py migrate</blockquote></pre>

<p>Finally, run the development server:</p>
 
<pre><blockquote>python manage.py runserver</blockquote></pre>

<p>The site will be available at</p>
 
<pre><blockquote>127.0.0.1:8000</blockquote></pre>
