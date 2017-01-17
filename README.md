~/.local/bin/django-admin.py startproject socialnet
python manage.py migrate
python manage.py startapp perfis
python manage.py runserver

#to create from Profile
python manage.py makemigrations

#to migrate to sqllite3
python manage.py migrate

#to save on DB on terminal
python manage.py shell
/home/castor/.local/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py:63: RuntimeWarning: SQLite received a naive datetime (2017-01-16 10:25:16.135114) while time zone support is active.
  RuntimeWarning)

Python 2.7.13 (default, Dec 18 2016, 20:19:42) 
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: from profiles.models import Profile

In [2]: profile = Profile(name='Lucio', email ='luciomoraes@gmail.com', phone='n\na', company='My own')

In [3]: profile.save
Out[3]: <bound method Profile.save of <Profile: Profile object>>

In [4]: profile.save()


In [5]: profile_find = Profile.objects.get(id=1)

In [6]: profile_find.name
Out[6]: u'Lucio'

In [7]: profile_find.company
Out[7]: u'My own'

In [8]: profile_find.phone
Out[8]: u'n\na'

In [9]: profile_find.email


Out[9]: u'luciomoraes@gmail.com'

In [10]: profile_find.name='Lucio Moraes'

In [11]: profile_find.save()

In [12]: profile_find.name
Out[12]: 'Lucio Moraes'



#to see DDL 
python manage.py sqlmigrate profiles 0001_initial


