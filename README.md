## Installation

###Install requirement
run command in terminal
```language
	pip install -r requirement.txt
```

###Edit settings file
copy file settings_sample.py and rename its to settings.py
```commandline
	cp settings_sample.py settings.py
```
edit MySQL database information in **setting.py**
```language
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'betting_api',
	        'USER': 'root',
	        'PASSWORD': '',        
	    }
	}
```

###Migrate database
```language
	python manage.py migrate
```

###Run server
```language
	python manage.py runserver
```

###Local Connect Information If Neccessary
````language
  AUTH_SERVER=http://localconnect.garena.vn
  AUTH_CLIENT_ID=ca86063d4ced2e6dd72a5bae88b5e7c3
````
Set host:
````language
  45.119.240.111 localconnect.garena.vn
````
