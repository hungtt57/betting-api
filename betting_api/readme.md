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