# Django Ecommerce Website

<br>

## Installation
* Clone project.
<pre>
git clone https://github.com/namnd-repo/dj-ecommerce.git
</pre>

* Create virtual environment if you want to. Install requirements (upgrade pip might solve some installation errors).
<pre>
pip install -r requirements.txt
</pre>

* Create a database name 'ecommerce'. You can change it on settings.py. Run these commands in terminal:
<pre>
cd ecommerce
py manage.py createsuperuser
py manage.py migrate
</pre>

* Run project:
<pre>
py manage.py runserver
</pre>
